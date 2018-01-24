"""多线程实现udp聊天"""
'''
@Time    : 2018/1/22 下午3:11
@Author  : scrappy_zhang
@File    : net03_udp_threading_chat.py
'''
import threading
import socket


def send_message():
    send_ip = input('请输入要发送的ip：\n')
    send_port = input('请输入要发送的端口:\n')
    send_address = (send_ip, int(send_port))
    while True:
        send_data = input('请输入要发送的消息：\n')
        sock.sendto(send_data.encode('utf-8'), send_address)


def recv_message(udp_sock):
    while True:
        recv_data = udp_sock.recvfrom(1024)  # 接收数据
        print('从', recv_data[1], '接收的数据为：', recv_data[0].decode('utf-8'))


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    address = ('localhost', 8888)  # 地址：设定服务器要使用端口8888
    sock.bind(address)  # 绑定端口

    td1 = threading.Thread(target=recv_message, args=(sock, ))
    td1.start()

    send_message()

