"""
实现文件下载的TCP客户端
"""
'''
@Time    : 2018/1/21 下午6:17
@Author  : scrappy_zhang
@File    : net02_tcp_client_file_download.py
'''

import socket

if __name__ == '__main__':

    tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = input('请输入文件服务器ip:')
    server_port = input('请输入文件服务器端口：')
    server_address = (server_ip, int(server_port))

    tcp_client_sock.connect(server_address)

    send_data = input('请输入要下载的文件名（带后缀）：')
    tcp_client_sock.send(send_data.encode('utf-8'))

    recv_data = tcp_client_sock.recv(1024)

    if recv_data:
        if recv_data == '1'.encode('utf-8'):
            print('服务器无此文件')
        else:
            with open('./file_path/' + send_data, 'wb') as download_file:
                download_file.write(recv_data)
            print('下载', send_data, '完毕')

    tcp_client_sock.close()
