## 3.1 TCP

### 3.1.1 TCP定义

TCP（Transmission Control Protocol 传输控制协议）是一种**面向连接的、可靠的、基于字节流**的传输层通信协议，由IETF的RFC 793定义。

### 3.1.2 TCP特性

#### 1. 面向连接

TCP通信需要经过创建连接、数据传送、终止连接三个步骤。TCP通信模型中，在通信开始之前，一定要先建立相关的链接，才能发送数据，类似于生活中，"打电话"。通信双方必须先建立连接（打通电话）才能进行数据的传输（交流），双方都必须为该连接分配必要的系统内核资源，以管理连接的状态和连接上的传输。双方间的数据传输都可以通过这一个连接进行。完成数据交换后，双方必须断开此连接（挂掉电话），以释放系统资源。这种连接是一对一的，因此TCP不适用于广播的应用程序，基于广播的应用程序请使用UDP协议。

![](/assets/dadianhua.png)

#### 2. 可靠传输

**1）TCP采用发送应答机制**  
TCP发送的每个报文段都必须得到接收方的应答才认为这个TCP报文段传输成功  
**2）超时重传**  
发送端发出一个报文段之后就启动定时器，如果在定时时间内没有收到应答就重新发送这个报文段。TCP为了保证不发生丢包，就给每个包一个序号，同时序号也保证了传送到接收端实体的包的按序接收。然后接收端实体对已成功收到的包发回一个相应的确认（ACK）；如果发送端实体在合理的往返时延（RTT）内未收到确认，那么对应的数据包就被假设为已丢失将会被进行重传。  
**3）错误校验**  
TCP用一个校验和函数来检验数据是否有错误；在发送和接收时都要计算校验和。  
**4\) 流量控制和阻塞管理**  
流量控制用来避免主机发送得过快而使接收方来不及完全收下。

### 3.1.3 TCP通信的三次握手和四次挥手

#### 连接建立

TCP是因特网中的传输层协议，使用三次握手协议建立连接。当主动方发出SYN连接请求后，等待对方回答SYN+ACK，并最终对对方的 SYN 执行 ACK 确认。这种建立连接的方法可以防止产生错误的连接，TCP使用的流量控制协议是可变大小的滑动窗口协议。

**TCP三次握手**的过程如下：  
客户端发送SYN（SEQ=x）报文给服务器端，进入SYN\_SEND状态。  
服务器端收到SYN报文，回应一个SYN （SEQ=y）ACK\(ACK=x+1）报文，进入SYN\_RECV状态。  
客户端收到服务器端的SYN报文，回应一个ACK\(ACK=y+1）报文，进入Established状态。  
**三次握手完成，TCP客户端和服务器端成功地建立连接，可以开始传输数据了**。

`这就像最经典的打电话方式:我们向10086打人工电话时，需要接通到人工状态；10086客服人员会回应我们‘有什么需要服务的吗？’然后等待我们回复；我们听到10086客服的声音后，回复‘有’。总共3次握手，接下来就是沟通解决问题了。`

#### ![](/assets/tcp_sanciwoshou.png)

#### 连接终止

**建立一个连接需要三次握手，而终止一个连接要经过四次握手**，这是由TCP的半关闭（half-close）造成的。具体过程如下图所示。

\(1\) 某个应用进程首先调用close，称该端执行“主动关闭”（active close）。该端的TCP于是发送一个FIN分节，表示数据发送完毕。\(2\) 接收到这个FIN的对端执行 “被动关闭”（passive close），这个FIN由TCP确认。

`注意：FIN的接收也作为一个文件结束符（end-of-file）传递给接收端应用进程，放在已排队等候该应用进程接收的任何其他数据之后，因为，FIN的接收意味着接收端应用进程在相应连接上再无额外数据可接收。`

\(3\) 一段时间后，接收到这个文件结束符的应用进程将调用close关闭它的套接字。这导致它的TCP也发送一个FIN。  
\(4\) 接收这个最终FIN的原发送端TCP（即执行主动关闭的那一端）确认这个FIN。

既然每个方向都需要一个FIN和一个ACK，因此通常需要4个分节。

`这就像我们拨打10086人工客服服务结束的时候：            
我们会对10086客服人员说，谢谢您解答了我的这个问题；            
10086客服人员会回应我们'很高兴为您解答，还有其他问题么？如果没有的话，请帮忙进行评价'——这里面两个意思，一个是对我们上一句话的应答，另一个是确认问询；            
我们会再次恢复10086客服人员，没有问题了，非常感谢，一定评10分。结束通话`

![](/assets/tcp_sicihuishou.png)

**注意：**

\(1\) “通常”是指，某些情况下，步骤1的FIN随数据一起发送，另外，步骤2和步骤3发送的分节都出自执行被动关闭那一端，有可能被合并成一个分节。  
\(2\) 在步骤2与步骤3之间，从执行被动关闭一端到执行主动关闭一端流动数据是可能的，这称为“半关闭”（half-close）。  
\(3\) 当一个Unix进程无论自愿地（调用exit或从main函数返回）还是非自愿地（收到一个终止本进程的信号）终止时，所有打开的描述符都被关闭，这也导致仍然打开的任何TCP连接上也发出一个FIN。  
无论是客户还是服务器，任何一端都可以执行主动关闭。**通常情况是，客户执行主动关闭，但是某些协议，例如，HTTP/1.0却由服务器执行主动关闭。**

## 3.2 TCP套接字流程

### 3.2.1 TCP与UDP的不同点

* 面向连接（确认有创建三方交握，连接已创建才作传输。）
* 有序数据传输
* 重发丢失的数据包
* 舍弃重复的数据包
* 无差错的数据传输
* 阻塞/流量控制

### 3.2.2 TCP套接字流程

udp通信模型中，在通信开始之前，一定要先建立相关的链接，才能发送数据，类似于生活中，"打电话""。如下图所示，为python中的TCP套接字流程，读者可以对比下图中10086的故事进行理解。

![](/assets/10086image.png)

![](/assets/tcp_socket.png)

## 3.3 TCP客户端

### 需求实现：

实现简单的TCP客户端收发数据功能：发送给服务器数据，并获取服务器返回的数据，并打印显示出来。

### 根据流程图书写模块代码

1. 导入套接字
   ```
   import socket
   ```
2. 创建套接字
   ```
   tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ```
3. 连接服务器
   ```
   tcp_client_sock.connect(server_address)
   ```
4. 发送数据
   ```
   tcp_client_sock.send(send_data.encode('utf-8'))
   ```
5. 接收数据
   ```
   recv_data = tcp_client_sock.recv(1024)
   ```
6. 关闭套接字
   ```
   tcp_client_sock.close()
   ```

### 完整代码

```py
'''net02_tcp_client.py'''
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
```

### 实现结果

我们先在虚拟机中的linux系统中运行网络调试助手，启动并配置好TCP服务器；它的ip为`192.168.234.129`，端口为`8080`.接下来在本地运行编写的TCP客户端，依次输入TCP服务器的ip和端口。根据系统提示输入发送给服务器的数据`hello tcp server`。可以看到网络调试助手收到了该信息。**此时客户端程序会运行到recv那一行，由于该函数为阻塞函数，因此客户端程序会一直在此等待直到收到服务器的数据**。然后我们从网络调试助手服务器发送数据`hello python tcp client`。发送后，客户端接收到数据并打印出来，关闭套接字结束程序。

![](/assets/socket_tcp_client.png)

从运行过程中可以看出，**由于TCP通信是面向连接的，在建立连接后发送数据时不需要再设置地址了，**这里可以和UDP进行对比，加深理解。

## 3.4 TCP服务端

### 需求实现：

实现简单的TCP服务端收发数据功能：接收到客户端连接后，接收客户端数据并打印显示，然后回复客户端`thank you, tcp client`。

### 根据流程图书写模块代码

1. 导入套接字
   ```
   import socket
   ```
2. 创建服务器套接字
   ```
   tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   ```
3. 绑定端口
   ```
   tcp_server_socket.bind(address)
   ```
4. 开启监听
   ```
   tcp_server_socket.listen()
   ```
5. 接收连接获取客户端的地址，并自动创建客户服务子套接字
   ```
   client_socket, client_address = tcp_server_socket.accept()
   ```
6. 接收数据
   ```
   recv_data = client_socket.recv(1024)
   ```
7. 发送数据
   ```
   client_socket.send('thank you, tcp client'.encode('utf-8'))
   ```
8. 关闭客户服务子套接字
   ```
   client_socket.close()
   ```

**注：实际场景中服务器要面对众多客户端，一般不轻易关闭服务器套接字。**

### 完整代码

```py
'''net02_tcp_server.py'''
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
```

### 实现结果

我们先运行编写好的程序启动TCP服务器，它的ip为`192.168.234.1`，端口为`8888` 。然后启动linux中的网络调试助手配置好TCP客户端，并发送数据`hello python tcp server`给服务器。服务器接收到数据后会以指定格式打印出接收到的数据并向客户端发送数据`thank you,tcp client`。 程序继续运行关闭服务子套接字，结束进程。

![](/assets/socket_tcp_server.png)

我们也可以先运行本节的程序启动TCP服务器，然后运行上一节的程序启动客户端，两者之间进行通信，实现数据收发。效果如下。

![](/assets/socket_tcp_server2.png)

## 3.5 TCP通信完成文件下载

### 需求实现：

**TCP客户端实现功能：**向服务器发送一个用户输入的文件名，若文件存在，则下载文件；若不存在（收到数字1）则提示不存在。

**TCP服务端实现功能：**接收TCP客户端的数据，识别并打印显示客户端请求下载的文件名，若文件存在则发送文件给客户端；若不存在则发送数字1给客户端并打印显示文件不存在。

### 根据流程图书写模块代码

* TCP客户端：

  发送数据：用户输入的文件名

  接收数据：若为1，则打印提示文件不存在

  ```
        若存在，则将文件存入./file\_path/文件夹
  ```

* TCP服务端：

  接收数据：打印显示客户端需要的文件的文件名

  发送数据：若文件存在，则调用读取文件函数，并发送文件

  ```
        若文件不存在，则发送数字1，并打印显示文件不存在
  ```

  读取文件

![](/assets/socket_tcp_file_download.png)

### 完整代码

**TCP客户端：**

```py
'''net02_tcp_client_file_download.py'''
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
```

**TCP服务端：**

```py
'''net02_tcp_server_file_download.py'''
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
```

### 实现结果

我们演示时，在与源代码同一目录下创建了一个图片文件file\_example.jpg（即TCP小结的思维导图）以供下载演示。然后创建了一个目录file\_path来保存客户端下载到的文件。可以看到，成功下载了file\_example.jpg；让文件不存在时也打印了相应的文件不存在提示。

![](/assets/socket_tcp_down2.png)

![](/assets/socket_tcp_down3.png)

## 3.6 小结

**python中的TCP注意点**

* tcp服务器一般情况下都需要绑定，否则客户端找不到这个服务器
* tcp客户端一般不绑定，因为是主动链接服务器，所以只要确定好服务器的ip、port等信息就好，本地客户端可以随机
* tcp服务器中通过listen可以将socket创建出来的主动套接字变为被动的，这是做tcp服务器时必须要做的
* 当客户端需要链接服务器时，就需要使用connect进行链接，udp是不需要链接的而是直接发送，但是tcp必须先链接，只有链接成功才能通信
* 当一个tcp客户端连接服务器时，服务器端会有1个新的套接字，这个套接字用来标记这个客户端，单独为这个客户端服务
* listen后的套接字是被动套接字，用来接收新的客户端的连接请求的，而accept返回的新套接字是标识这个新客户端的。
* 关闭listen后的套接字意味着被动套接字关闭了，会导致新的客户端不能够链接服务器，但是之前已经链接成功的客户端正常通信。
* 关闭accept返回的套接字意味着这个客户端已经服务完毕
* 当客户端的套接字调用close后，服务器端会recv解阻塞，并且返回的长度为0，因此服务器可以通过返回数据的长度来区别客户端是否已经下线；同理 当服务器断开tcp连接的时候 客户端同样也会收到0字节数据。

![](/assets/socket_tcp_summary.png)

