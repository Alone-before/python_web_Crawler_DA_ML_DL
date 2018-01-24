"""
scoket 简单实现tcp服务端
"""
'''
@Time    : 2018/1/21 下午5:48
@Author  : scrappy_zhang
@File    : net02_tcp_server.py
'''

import socket

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置为地址复用，告诉操作系统可以立即使用某个端口
tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
'''
我们在进行在之前的UDP和现在的TCP学习时经常会遇到以下错误提示：
  tcp_server_socket.bind(address)
OSError: [Errno 48] Address already in use
这是因为之前运行的程序结束后，操作系统还没有来得及释放端口造成
通过上面地址复用的设置语句可以立即从操作系统获得端口，就不会再报错
'''

address = ('192.168.234.1', 8888)
tcp_server_socket.bind(address)

tcp_server_socket.listen()

client_socket, client_address = tcp_server_socket.accept()

recv_data = client_socket.recv(1024)
print('从', client_address[0], ':', client_address[1], '接收到的数据为', recv_data.decode('utf-8'))

client_socket.send('thank you, tcp client'.encode('utf-8'))

client_socket.close()