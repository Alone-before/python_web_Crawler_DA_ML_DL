"""
实现文件下载的TCP服务端
"""
'''
@Time    : 2018/1/21 下午6:15
@Author  : scrappy_zhang
@File    : net02_tcp_server_file_download.py
'''
import socket


def get_file(filename):
    """获取文件的内容"""
    try:
        with open(filename, 'rb') as file_download:
            content = file_download.read()
    except:
        print('没有这个文件', filename)
        content = 1
    finally:
        return content


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    address = ('localhost', 8888)
    tcp_server_socket.bind(address)

    tcp_server_socket.listen()
    while True:
        client_socket, client_address = tcp_server_socket.accept()

        recv_data = client_socket.recv(1024)
        print(client_address[0], ':', client_address[1], '想要下载的文件为', recv_data.decode('utf-8'))

        send_file_data = get_file(recv_data.decode('utf-8'))
        if send_file_data == 1:
            client_socket.send('1'.encode('utf-8'))
        else:
            client_socket.send(send_file_data)

        client_socket.close()

    tcp_server_socket.close()
