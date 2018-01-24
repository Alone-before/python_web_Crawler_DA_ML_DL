"""linux平台 epoll 实现web服务器  多线程"""
'''
@Time    : 2018/1/24 下午4:12
@Author  : scrappy_zhang
@File    : net09_web_PWB7.py
'''

import socket
import select
import re
import threading

SERVER_ADDR = (HOST, PORT) = '', 8888  # 服务器地址
VERSION = 7.0  # web服务器版本号
STATIC_PATH = './static/'


class HTTPServer():
    def __init__(self, server_address):
        """初始化服务器TCP套接字"""
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_socket.bind(server_address)
        self.tcp_socket.listen(128)
        self.tcp_socket.setblocking(False)  # 将套接字设置为非阻塞模式
        self.epoll = select.epoll()  # 创建一个epoll对象
        self.epoll.register(self.tcp_socket.fileno(), select.EPOLLIN | select.EPOLLET) # 将服务套接字注册
        self.connections = {}
        self.addresses = {}

    def serve_forever(self):
        """永久运行监听接收连接"""
        while True:
            epoll_list = self.epoll.poll()
            for fd, events in epoll_list:
                if fd == self.tcp_socket.fileno():
                    new_client_socket, new_client_address = self.tcp_socket.accept()
                    print(new_client_address, '向服务器发起了请求')
                    self.connections[new_client_socket.fileno()] = new_client_socket # 存入客户连接事件文件描述符
                    self.addresses[new_client_socket.fileno()] = new_client_address
                    # 向epoll中则侧新socket的可读事件
                    self.epoll.register(new_client_socket.fileno(), select.EPOLLIN | select.EPOLLET)
                elif events == select.EPOLLIN:
                    td = threading.Thread(target=self.handlerequest, args=(fd,))
                    td.start()

    def handlerequest(self, fd):
        """客户端请求处理，发送响应数据"""
        # 收取浏览器请求信息，并在服务器端打印显示
        request_data = self.connections[fd].recv(2048).decode('utf-8')
        # 数据为空代表客户端关闭了连接，则在监听中除去响应的文件描述符
        if not request_data:
            self.epoll.unregister(fd)
            self.connections[fd].close()  # server侧主动关闭连接fd
            print("%s---offline---" % str(self.addresses[fd]))
            del self.connections[fd]
            del self.addresses[fd]
        # 若存在数据，则按照正常的事件处理
        else:
            request_header_lines = request_data.splitlines()
            # for line in request_header_lines:
            #     print(line)

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
                self.connections[fd].send(resp_data)
                # HTTP短连接，请求完即关闭TCP连接，并除去相应事件的文件描述符
                self.epoll.unregister(fd)
                self.connections[fd].close()  # server侧主动关闭连接fd
                print("%s--web请求响应完毕-offline---" % str(self.addresses[fd]))
                del self.connections[fd]
                del self.addresses[fd]


def run():
    """运行服务器"""
    pwb = HTTPServer(SERVER_ADDR)
    print('web server:PWB %s on port %d...\n' % (VERSION, PORT))
    pwb.serve_forever()


if __name__ == '__main__':
    run()
