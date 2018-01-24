"""
编写1个程序，有2个功能：1.获取键盘数据，并将其发送给指定方，2.接收数据并显示。进行选择以上的2个功能调用
"""
'''
@Time    : 2018/1/21 下午4:53
@Author  : scrappy_zhang
@File    : net03_udp_chat.py
'''

import socket


def send_message():
    send_data = input('请输入要发送的消息：\n')
    send_ip = input('请输入要发送的ip：\n')
    send_port = input('请输入要发送的端口:\n')
    send_address = (send_ip, int(send_port))
    sock.sendto(send_data.encode('utf-8'), send_address)


def recv_message():
    recv_data = sock.recvfrom(1024)  # 接收数据
    print('从', recv_data[1], '接收的数据为：', recv_data[0].decode('utf-8'))


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    address = ('192.168.234.1', 8888)  # 地址：设定服务器要使用端口8888
    sock.bind(address)  # 绑定端口

    # 功能菜单显示
    print('*' * 30)
    print('1、发送数据')
    print('2、接收数据')
    print('*' * 30)
    fun_num = input('请选择并输入指定数字：\n')  # 获取键盘选项数据

    # 输入判断
    if fun_num == '1':
        send_message()
    elif fun_num == '2':
        recv_message()
    else:
        print('您输入的数据有误！程序结束')
