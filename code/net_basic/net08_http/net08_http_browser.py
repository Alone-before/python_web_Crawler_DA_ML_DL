"""通过socket建立的TCP模拟浏览器请求百度主页，并将网页内容保存到本地"""
'''
@Time    : 2018/1/23 下午8:59
@Author  : scrappy_zhang
@File    : net08_http_browser.py
'''

import socket

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_sock.connect(('www.baidu.com', 80))  # http默认端口80

# 模拟浏览器GET内容
request_line = "GET / HTTP/1.1\r\n"  # 请求行
request_header = "Host: www.baidu.com\r\n"  # 请求行

# 请求数据
request_data = request_line + request_header + '\r\n'
# 发送请求
tcp_sock.send(request_data.encode('utf-8'))

# 收取服务器响应数据
resp_data = tcp_sock.recv(4096).decode('utf-8')

# 解析响应数据
index = resp_data.find('\r\n\r\n')  # 找到空行,空行后面就是响应body，即网页内容
resp_headers = resp_data[:index + 1]  # 响应头和响应行
html_data = resp_data[index + 4:]  # 响应body
print(resp_headers)  # 显示服务器响应信息

# 保存网页到到本地文件baidu.html
with open('baidu.html', 'wb') as html_file:
    html_file.write(html_data.encode())
