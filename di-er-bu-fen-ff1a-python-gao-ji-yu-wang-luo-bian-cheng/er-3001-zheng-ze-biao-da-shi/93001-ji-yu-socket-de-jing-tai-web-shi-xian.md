# 9 基于socket的静态web服务器

前面8章我们学习了网络编程最基础的概念和在python中的使用方法。为了更充分的体现这些基础概念的重要性，本节综合所有基础知识带大家一同使用学习到的知识来实践编写一个静态web服务器——python web server,简称PWB。

## 9.1 显示固定页面的web服务器

这一节为了更好的理解静态web服务器的搭建过程，我们先来搭建一个只能显示固定页面内容的web服务器。如何实现呢？通过面向对象的思维，我们可以先创建一个web服务器类HTTPServer，然后实例化调用运行即可。一般情况下web服务器都是一直在运行并处理客户端请求，因此我们的这个web服务器类除了初始化\_\_init\_\_方法外，还需要一个永久运行监听客户端\(浏览器\)连接的方法serve\_forever和一个连接成功后向客户端\(浏览器\)发送响应数据的方法handlerequest。代码框架如下：

```py
import socket

SERVER_ADDR = (HOST, PORT) = '', 8888  # 服务器地址
VERSION = 1.0  # web服务器版本号


class HTTPServer():
    def __init__(self, server_address):
        """初始化服务器TCP套接字"""
        pass

    def serve_forever(self):
        """永久运行监听接收连接"""
        pass

    def handlerequest(self, client_socket):
        """客户端请求处理，发送响应数据"""
        pass


def run():
    """运行服务器"""
    pwb = HTTPServer(SERVER_ADDR)
    print('web server:PWB %s on port %d...\n' % (VERSION, PORT))
    pwb.serve_forever()


if __name__ == '__main__':
    run()
```

运行一下，可以看到终端输出一下信息提示web服务器在8888端口运行，由于它并没有任何功能，所以仅仅是提示信息。

```
web server:PWB 1.0 on port 8888...
```

接下来我们需要做的就是将代码框架中的空缺部分一一填满。

根据TCP服务器的搭建过程，我们知道，HTTPServer类的初始化方法中应当实现这些功能：TCP服务套接字的创建、地址绑定并启动监听。

```py
    def __init__(self, server_address):
        """初始化服务器TCP套接字"""
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_socket.bind(server_address)
        self.tcp_socket.listen(128)
```

永久运行监听接收连接的方法serve\_forevet主要功能是实现连接上客户端，并调用客户端请求处理方法self.handlerequest。

```py
    def serve_forever(self):
        """永久运行监听接收连接"""
        while True:
            client_socket, client_address = self.tcp_socket.accept()
            print(client_address, '向服务器发起了请求')
            self.handlerequest(client_socket)
```

客户端请求处理方法handlerequest则需要获取客户端\(浏览器\)发送来的请求数据，并经过解析后向浏览器发送一组包括响应头和响应体的数据。这里由于我们是返回一个固定的内容hello PWB，因此我们只要接收到了浏览器的请求，便可以发送固定的响应成功头和固定的响应体hello PWB给浏览器。

```py
    def handlerequest(self, client_socket):
        """客户端请求处理，发送响应数据"""
        # 收取浏览器请求信息，并在服务器端打印显示
        request_data = client_socket.recv(2048).decode('utf-8')
        request_header_lines = request_data.splitlines()
        for line in request_header_lines:
            print(line)

        # 响应信息：本例显示固定内容：响应成功 + hello PWB
        resp_headers = "HTTP/1.1 200 OK\r\n"  # 200代表响应成功并找到资源
        resp_headers += "Server: PWB" + str(VERSION) + '\r\n'  # 告诉浏览器服务器
        resp_headers += '\r\n'  # 空行隔开body
        resp_body = 'hello PWB\r\n'  # 固定的显示内容
        resp_data = resp_headers + resp_body

        # 发送相应数据至浏览器
        client_socket.send(resp_data.encode('utf-8'))
        client_socket.close()  # HTTP短连接，请求完即关闭TCP连接
```

这样子，我们的代码框架就根据需求功能填充完毕了。

完整代码如下：

```py
'''net09_web_PWB1.py'''
import socket

SERVER_ADDR = (HOST, PORT) = '', 8888  # 服务器地址
VERSION = 1.0  # web服务器版本号


class HTTPServer():
    def __init__(self, server_address):
        """初始化服务器TCP套接字"""
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_socket.bind(server_address)
        self.tcp_socket.listen(128)

    def serve_forever(self):
        """永久运行监听接收连接"""
        while True:
            client_socket, client_address = self.tcp_socket.accept()
            print(client_address, '向服务器发起了请求')
            self.handlerequest(client_socket)

    def handlerequest(self, client_socket):
        """客户端请求处理，发送响应数据"""
        # 收取浏览器请求信息，并在服务器端打印显示
        request_data = client_socket.recv(2048).decode('utf-8')
        request_header_lines = request_data.splitlines()
        for line in request_header_lines:
            print(line)

        # 响应信息：本例显示固定内容：响应成功 + hello PWB
        resp_headers = "HTTP/1.1 200 OK\r\n"  # 200代表响应成功并找到资源
        resp_headers += "Server: PWB" + str(VERSION) + '\r\n'  # 告诉浏览器服务器
        resp_headers += '\r\n'  # 空行隔开body
        resp_body = 'hello PWB'  # 固定的显示内容
        resp_data = resp_headers + resp_body

        # 发送相应数据至浏览器
        client_socket.send(resp_data.encode('utf-8'))
        client_socket.close()  # HTTP短连接，请求完即关闭TCP连接


def run():
    """运行服务器"""
    pwb = HTTPServer(SERVER_ADDR)
    print('web server:PWB %s on port %d...\n' % (VERSION, PORT))
    pwb.serve_forever()


if __name__ == '__main__':
    run()
```

运行服务器程序，并在浏览器中输入localhost:8888来访问web服务器，我们可以看到显示的内容为hello PWB。打开检查，我们可以对比查看浏览器中显示的各项请求响应信息和我们web服务器打印显示的请求信息，完全一致。

由于我们的请求处理中无论接收到什么信息，都是向浏览器发送hello PWB，因此当我们输入localhost:8888/11时也是显示hello PWB。这就是固定内容显示的web服务器。

![](/assets/websocket1.png)

细心的读者可能会发现，浏览器还请求了一个名叫favicon.ico的文件。这个文件一般为网站标识图片，即网页标签页顶部显示的图片，如下图所示。

![](/assets/websocket2.png)

## 9.2 显示指定需要内容的web服务器

一个WEB服务器不可能只显示一个页面，肯定有特定需求的特定页面显示，怎么实现呢？。读者在上一节很清楚的看到**GET 后的信息类似我们常见的资源文件夹那样的路径一样**。是的，这就是静态资源的路径。我们可以通过判断这里来识别浏览器请求的是哪个静态资源。那我们就需要在HTTPServer类中的**handlerequest方法修改代码来解析浏览器请求头并返回不同的响应体**。

_注：在讲解演示之前，我们在代码同文件夹目录下创建了一个static文件夹，里面有baidu.html、oschina.html和gitee.html三个html文件。它们分别是百度、开源中国和码云三个网站的首页源码。读者可以通过我们之前的并发下载网页的源码经过适当调整来下载生成这三个html文件；也可以直接在浏览器中分别打开相应的主页，将网页源码拷贝在本地建立三个html文件。本节将讲解根据浏览器输入URL的不同来请求获取这三个html，就像访问真正的三个网站一样。_

首先我们需要解析请求信息。请求信息的第一行get内容为请求文件的路径，通过正则表达式便可以将其抓取出来。代码如下：

```py
        pattern = r'[^/]+(/[^ ]*)'
        request_html_name = re.match(pattern, request_header_lines[0]).group(1)
```

一般web服务器都会在静态资源URL的基础之上来添加一些路径来实现避免被用户访问到不该访问的内容。后面我们会看到本例中URL为localhost：8888/baidu.html，实际上调用的是./static/baidu.html文件。假如我们作为web服务器放一个非常机密的文件password.txt，这种常见的文件名称和类型，很容易会被黑客等直接通过localhost：8888/password.txt获取到并造成数据泄露。所以一般web服务器内部都会对静态资源路径有一套编码解码机制来加密。这里我们假设我们的默认页面就是baidu.html。即localhost:8888、localhost:8888/、localhost:8888/baidu.html显示的内容一致。

```py
        if request_html_name == '/':
            request_html_name = STATIC_PATH + 'baidu.html'
        else:
            request_html_name = STATIC_PATH + request_html_name
```

至此，我们就已经获悉了用户请求的具体文件情况，我们只需根据相应文件名来读取相应文件并设置为响应体发送给浏览器即可。

```py
html_file = open(request_html_name, 'rb')
resp_body = html_file.read()  # 显示内容为读取的文件内容
html_file.close()
```

完整的代码如下：

```py
'''net09_web_PWB2.py'''
import socket
import re

SERVER_ADDR = (HOST, PORT) = '', 8888  # 服务器地址
VERSION = 2.0  # web服务器版本号
STATIC_PATH = './static/'


class HTTPServer():
    def __init__(self, server_address):
        """初始化服务器TCP套接字"""
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_socket.bind(server_address)
        self.tcp_socket.listen(128)

    def serve_forever(self):
        """永久运行监听接收连接"""
        while True:
            client_socket, client_address = self.tcp_socket.accept()
            print(client_address, '向服务器发起了请求')
            self.handlerequest(client_socket)

    def handlerequest(self, client_socket):
        """客户端请求处理，发送响应数据"""
        # 收取浏览器请求头，并在服务器端打印显示
        request_data = client_socket.recv(2048).decode('utf-8')
        request_header_lines = request_data.splitlines()
        # print(request_header_lines[0])  # 第一行为请求头信息
        # 解析请求头，获取具体请求信息
        pattern = r'[^/]+(/[^ ]*)'
        request_html_name = re.match(pattern, request_header_lines[0]).group(1)
        # 根据解析到的内容补全将要读取文件的路径
        if request_html_name == '/':
            request_html_name = STATIC_PATH + 'baidu.html'
        else:
            request_html_name = STATIC_PATH + request_html_name

        # 根据文件情况来返回相应的信息
        try:
            html_file = open(request_html_name, 'rb')
        except FileNotFoundError:
            # 文件不存在，则返回文件不存在，并返回状态码404
            resp_headers = 'HTTP/1.1 404 not found\r\n'
            resp_headers += "Server: PWB" + str(VERSION) + '\r\n'
            resp_headers += '\r\n'
            resp_body = '==== 404 file not found===='.encode('utf-8')
        else:
            # 文件存在，则读取文件内容，并返回状态码200
            resp_headers = "HTTP/1.1 200 OK\r\n"  # 200代表响应成功并找到资源
            resp_headers += "Server: PWB" + str(VERSION) + '\r\n'  # 告诉浏览器服务器
            resp_headers += '\r\n'  # 空行隔开body
            resp_body = html_file.read()  # 显示内容为读取的文件内容
            html_file.close()
        finally:
            resp_data = resp_headers.encode('utf-8') + resp_body  # 结合响应头和响应体
            # 发送相应数据至浏览器
            client_socket.send(resp_data)
            client_socket.close()  # HTTP短连接，请求完即关闭TCP连接


def run():
    """运行服务器"""
    pwb = HTTPServer(SERVER_ADDR)
    print('web server:PWB %s on port %d...\n' % (VERSION, PORT))
    pwb.serve_forever()


if __name__ == '__main__':
    run()
```

可以看到，当输入localhost:8888时，返回的是我们本地的baidu.html 。同样可以在浏览器里看到我们设置的web服务器版本PWB2.0了。

![](/assets/websocket4.png)

当输入localhost:8888/gitee.html时，返回的是我们本地的gitee.html。

![](/assets/webserver5.png)

当输入localhost:8888/22时，返回的是404错误信息。

![](/assets/webser6.png)

## 9.3 多线程、多进程、协程实现web服务器



