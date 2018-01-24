"""socketserver tcp服务器示例"""
'''
@Time    : 2018/1/24 下午4:27
@Author  : scrappy_zhang
@File    : net10_tcp_server_sample.py
'''

from socketserver import TCPServer as TCP
from socketserver import BaseRequestHandler as BRH
from time import ctime

HOST = 'localhost'
PORT = 8888
ADDR = (HOST, PORT)


class MyRequestHandler(BRH):
    """自定义请求处理类，继承BaseRequestHandler"""
    def handle(self):
        """重载handle方法"""
        print('...connected from:', self.client_address)
        self.data = self.request.recv(1024).strip()  # 读取数据
        cli_data = self.data.decode()
        print('%s send data: %s' % (self.client_address, cli_data))
        self.request.send(('[%s] %s' % (ctime(), cli_data)).encode('utf-8'))  # 发送数据


if __name__ == '__main__':
    tcpServ = TCP(ADDR, MyRequestHandler) # 创建TCP服务器实例对象，并调用自定义请求处理子类
    print('waiting for connection...')
    tcpServ.serve_forever() # 调用TCPServer的serve_forever来永久运行TCP服务器
