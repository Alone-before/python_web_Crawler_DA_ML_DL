"""PWB1.0 实现显示固定内容"""
'''
@Time    : 2018/1/23 下午9:49
@Author  : scrappy_zhang
@File    : net09_web_PWB1.py
'''

import socket

SERVER_ADDR = (HOST, PORT) = '', 8888  # 服务器地址
VERSION = 1.0  # web服务器版本号


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
            self.handlerequest(client_socket)

    def handlerequest(self, client_socket):
        """客户端请求处理，发送响应数据"""
        # 收取浏览器请求信息，并在服务器端打印显示
        request_data = client_socket.recv(2048).decode('utf-8')
        request_header_lines = request_data.splitlines()
        for line in request_header_lines:
            print(line)

        # 响应信息：本例显示固定内容：响应成功 + hello PWB
        resp_headers = "HTTP/1.1 200 OK\r\n"  # 200代表响应成功并找到资源
        resp_headers += "Server: PWB" + str(VERSION) + '\r\n'  # 告诉浏览器服务器
        resp_headers += '\r\n'  # 空行隔开body
        resp_body = 'hello PWB'  # 固定的显示内容
        resp_data = resp_headers + resp_body

        # 发送相应数据至浏览器
        client_socket.send(resp_data.encode('utf-8'))
        client_socket.close()  # HTTP短连接，请求完即关闭TCP连接


def run():
    """运行服务器"""
    pwb = HTTPServer(SERVER_ADDR)
    print('web server:PWB %s on port %d...\n' % (VERSION, PORT))
    pwb.serve_forever()


if __name__ == '__main__':
    run()
