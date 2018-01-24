"""udp客户端，发送数据给8080端口的服务器"""
'''
@Time    : 2018/1/20 下午9:33
@Author  : scrappy_zhang
@File    : net01_udp_client.py
'''

import socket  # 导入模块

address = ('192.168.234.129', 8080)  # 服务器地址为192.168.234.129，端口号为8080
# address = ('192.168.234.1', 8888) # 和net02_udp_server服务器进行通信
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建套接字

send_data = 'net01_udp_client.py'
print('要发送的数据为', send_data)

sock.sendto(send_data.encode('utf-8'), address)  # 发送数据为bytes类型

recv_data = sock.recvfrom(1024) # 接收到的数据为两部分，recv_data[1]为数据发送端的地址，recv_data[2]为接收到的数据
print(recv_data[1], '传送回来的数据为：', recv_data[0].decode('utf-8'))

sock.close()
