"""从客户端收到一条数据后，在数据头增加’来自服务器‘字符串，然后一起转发回客户端，然后关闭服务器套接字。"""
'''
@Time    : 2018/1/21 下午4:12
@Author  : scrappy_zhang
@File    : net02_udp_server.py
'''

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ('192.168.234.1', 8888)  # 地址：设定服务器要使用端口8888
sock.bind(address)  # 绑定端口

recv_data = sock.recvfrom(1024)  # 接收数据
send_data = '来自服务器' + recv_data[0].decode()  # 数据处理，增加'来自服务器'
sock.sendto(send_data.encode('utf-8'), recv_data[1])  # 发送数据

sock.close()  # 关闭套接字
