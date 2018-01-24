"""
scoket 简单实现tcp客户端
"""
'''
@Time    : 2018/1/21 下午5:37
@Author  : scrappy_zhang
@File    : net02_tcp_client.py
'''

import socket

tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 创建TCP客户端套接字

server_ip = input('请输入服务器ip:')
server_port = input('请输入服务器端口：')
server_address = (server_ip, int(server_port))

tcp_client_sock.connect(server_address) # 连接用户输入的服务器

send_data = input('请输入要发送的数据：')
tcp_client_sock.send(send_data.encode('utf-8')) # 发送用户输入的数据给服务器

recv_data = tcp_client_sock.recv(1024) # 接收服务端数据
print('接收到的数据为：', recv_data.decode('utf-8'))

tcp_client_sock.close() # 关闭TCP客户端套接字