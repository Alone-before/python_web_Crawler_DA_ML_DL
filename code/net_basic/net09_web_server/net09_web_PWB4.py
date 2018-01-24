"""PWB4.0 多进程静态web服务器"""
'''
@Time    : 2018/1/24 下午3:04
@Author  : scrappy_zhang
@File    : net09_web_PWB4.py
'''

import socket
import re
import multiprocessing

SERVER_ADDR = (HOST, PORT) = '', 8888  # 服务器地址
VERSION = 4.0  # web服务器版本号
STATIC_PATH = './static/'


class HTTPServer():
    def __init__(self, server_address):
        """初始化服务器TCP套接字"""
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_socket.bind(server_address)
        self.tcp_socket.listen(128)

    def serve_forever(self):
        """永久运行监听接收连接"""
        while True:
            client_socket, client_address = self.tcp_socket.accept()
            print(client_address, '向服务器发起了请求')
            processes = multiprocessing.Process(target=self.handlerequest, args=(client_socket,))
            processes.start()
            client_socket.close()

    def handlerequest(self, client_socket):
        """客户端请求处理，发送响应数据"""
        # 收取浏览器请求头，并在服务器端打印显示
        request_data = client_socket.recv(2048).decode('utf-8')
        request_header_lines = request_data.splitlines()
        # print(request_header_lines[0])  # 第一行为请求头信息
        # 解析请求头，获取具体请求信息
        pattern = r'[^/]+(/[^ ]*)'
        request_html_name = re.match(pattern, request_header_lines[0]).group(1)
        # 根据解析到的内容补全将要读取文件的路径
        if request_html_name == '/':
            request_html_name = STATIC_PATH + 'baidu.html'
        else:
            request_html_name = STATIC_PATH + request_html_name

        # 根据文件情况来返回相应的信息
        try:
            html_file = open(request_html_name, 'rb')
        except FileNotFoundError:
            # 文件不存在，则返回文件不存在，并返回状态码404
            resp_headers = 'HTTP/1.1 404 not found\r\n'
            resp_headers += "Server: PWB" + str(VERSION) + '\r\n'
            resp_headers += '\r\n'
            resp_body = '==== 404 file not found===='.encode('utf-8')
        else:
            # 文件存在，则读取文件内容，并返回状态码200
            resp_headers = "HTTP/1.1 200 OK\r\n"  # 200代表响应成功并找到资源
            resp_headers += "Server: PWB" + str(VERSION) + '\r\n'  # 告诉浏览器服务器
            resp_headers += '\r\n'  # 空行隔开body
            resp_body = html_file.read()  # 显示内容为读取的文件内容
            html_file.close()
        finally:
            resp_data = resp_headers.encode('utf-8') + resp_body  # 结合响应头和响应体
            # 发送相应数据至浏览器
            client_socket.send(resp_data)
            client_socket.close()  # HTTP短连接，请求完即关闭TCP连接


def run():
    """运行服务器"""
    pwb = HTTPServer(SERVER_ADDR)
    print('web server:PWB %s on port %d...\n' % (VERSION, PORT))
    pwb.serve_forever()


if __name__ == '__main__':
    run()