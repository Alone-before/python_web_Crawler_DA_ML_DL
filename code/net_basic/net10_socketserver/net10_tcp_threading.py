"""ThreadingTCPServer sample"""
'''
@Time    : 2018/1/24 下午11:01
@Author  : scrappy_zhang
@File    : net10_tcp_threading.py
'''

from socketserver import ThreadingTCPServer as TCP
from socketserver import BaseRequestHandler as BRH
import re

HOST = 'localhost'
PORT = 8888
ADDR = (HOST, PORT)
VERSION = 8.0  # web服务器版本号
STATIC_PATH = './static/'


class MyRequestHandler(BRH):
    """自定义请求处理类，继承BaseRequestHandler"""

    def handle(self):
        """重载handle方法"""
        print(self.client_address, '连接了服务器')
        request_data = self.request.recv(2048).decode('utf-8')
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
            self.request.send(resp_data)
            self.request.close()  # HTTP短连接，请求完即关闭TCP连接


if __name__ == '__main__':
    tcpServ = TCP(ADDR, MyRequestHandler)  # 创建TCP服务器实例对象，并调用自定义请求处理子类
    print('web server:PWB %s on port %d...\n' % (VERSION, PORT))
    tcpServ.serve_forever()  # 调用TCPServer的serve_forever来永久运行TCP服务器
