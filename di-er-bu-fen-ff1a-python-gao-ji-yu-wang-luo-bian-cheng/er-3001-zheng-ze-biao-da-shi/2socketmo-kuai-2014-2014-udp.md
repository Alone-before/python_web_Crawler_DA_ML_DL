TCP/IP协议中的TCP和UDP协议都是通过一种名为套接字\(socket\)来实现网络功能。套接字是一种类文件对象，它使得程序能够接受客户端的连接或者建立对客户端的连接，用以发送和接收数据。不论是客户端程序还是服务器端程序，为了进行网络通信，都要创建套接字对象。本章讲解UDP协议用python套接字模块的实现。

## 2.1 UDP

### 2.1.1 udp定义

UDP 是User Datagram Protocol的简称， 中文名是**用户数据报协议**，是OSI（Open System Interconnection，开放式系统互联） 参考模型中一种无连接的传输层协议，提供面向事务的简单不可靠信息传送服务，IETF RFC 768是UDP的正式规范。UDP在IP报文的协议号是17。UDP有不提供数据包分组、组装和不能对数据包进行排序的缺点，也就是说，当报文发送之后，是无法得知其是否安全完整到达的。UDP用来支持那些需要在计算机之间传输数据的网络应用。包括网络视频会议系统在内的众多的客户/服务器模式的网络应用都需要使用UDP协议。

### 2.1.2 udp特性

（1） UDP是一个**无连接协议**，传输数据之前源端和终端不建立连接，当它想传送时就简单地去抓取来自应用程序的数据，并尽可能快地把它扔到网络上。在发送端，UDP传送数据的速度仅仅是受应用程序生成数据的速度、计算机的能力和传输带宽的限制；在接收端，UDP把每个消息段放在队列中，应用程序每次从队列中读一个消息段。  
（2） 由于传输数据不建立连接，因此也就不需要维护连接状态，包括收发状态等，因此一台服务机可同时向多个客户机传输相同的消息。  
（3） UDP信息包的标题很短，只有8个字节，相对于TCP的20个字节信息包的额外开销很小。  
（4） 吞吐量不受拥挤控制算法的调节，只受应用软件生成数据的速率、传输带宽、源端和终端主机性能的限制。  
（5）UDP使用尽最大努力交付，即不保证可靠交付，因此主机不需要维持复杂的链接状态表（这里面有许多参数）。  
（6）UDP是**面向报文的**。发送方的UDP对应用程序交下来的报文，在添加首部后就向下交付给IP层。既不拆分，也不合并，而是保留这些报文的边界，因此，应用程序需要选择合适的报文大小。

虽然UDP是一个不可靠的协议，但它是**分发信息的一个理想协议**。例如，在屏幕上报告股票市场、在屏幕上显示航空信息等等。UDP也用在路由信息协议RIP（Routing Information Protocol）中修改路由表。在这些应用场合下，如果有一个消息丢失，在几秒之后另一个新的消息就会替换它。UDP广泛用在多媒体应用中，例如，Progressive Networks公司开发的RealAudio软件，它是在因特网上把预先录制的或者现场音乐实时传送给客户机的一种软件，该软件使用的RealAudio audio-on-demand protocol协议就是运行在UDP之上的协议，大多数因特网电话软件产品也都运行在UDP之上。

## 2.2 socket模块函数

python中实现套接字的基本模块为socket。一般公共socket\(\)函数来创建套接字，并进行网络通信。要使用socket需要导入socket模块：`import socket`。一般使用socket.socket\(\)函数来创建套接字。其语法如下：

```py
socket.socket(family=AF_INET, type=SOCK_STREAM, proto)
```

其中：  
family为套接字家族名:AN\_INET、AF\_INET6、AF\_UNIX、AF\_CAN、AF\_RDS;AN\_INET默认值代表ipv4。  
type为套接字类型：SOCK\_STREAM、SOCK\_DGRAM、SOCK\_RAW;SOCK\_STREAM为TCP协议使用的类型，SOCK\_DGRAM为UDP使用的类型。  
proto为协议类型，默认为0 。

##### 常见的socket对象常用的方法有：

**bind\(address\)**

其参数address是由ip和端口组成的元组，如\('127.0.0.1', 8888\) 。如果ip地址为空，则表示本机，它的作用为绑定端口，使该程序在运行时使用操作系统的固定端口。

**listen\(backlog\)**

其参数backlog是指在拒绝连接之前，操作系统允许此程序的最大挂起连接数量。最小值为0.

**accept\(\)**

等待进入连接，并返回一个由新建的与客户端的socket连接和客户端地址组成的元组，其中客户的地址是由客户端ip地址和端口组成的元组。

**close\(\)**

关闭套接字，停止连接。

**recv\(buffersize\[, flag\]\)**

TCP用于接收远程连接发来的信息，并获取该信息，python3中为bytes类型。buffersize为接收缓冲区的大小。

**send\(data\[, flags\]\)**

TCP用于发送数据，data为bytes类型，返回值为已经发送的字节数。

**recvfrom\(buffersize\[, flag\]\)**

UDP用于接收远程连接发来的信息，并获取该信息，python3中为bytes类型。buffersize为接收缓冲区的大小。

**sendto\(data\[, flags\]\)**

UDP用于发送数据，data为bytes类型，返回值为已经发送的字节数。

## 2.3 UDP套接字流程

这几章为了更好的无负担学习套接字的客户端和服务端程序学习，我们借助非常有名的网络调试助手来充当服务器或者客户端进行配合演示。网络调试助手的具体使用可以查看UDP操作[https://jingyan.baidu.com/article/20b68a88a9c056796dec625e.html和TCP操作：https://jingyan.baidu.com/article/148a1921dc93e74d71c3b1d7.html。 ](https://jingyan.baidu.com/article/20b68a88a9c056796dec625e.html和TCP操作：https://jingyan.baidu.com/article/148a1921dc93e74d71c3b1d7.html。本书采用mac的网络调试助手演示，其他系统的可以查看百度链接。)  
[本书采用mac的网络调试助手演示，其他系统的可以查看百度链接。](https://jingyan.baidu.com/article/20b68a88a9c056796dec625e.html和TCP操作：https://jingyan.baidu.com/article/148a1921dc93e74d71c3b1d7.html。本书采用mac的网络调试助手演示，其他系统的可以查看百度链接。)

![](/assets/udp01.png)

![](/assets/udp02.png)

**根据UDP协议的无连接特点，一般客户端仅仅需要创建套接字、数据收发、关闭套接字三个部分就可以完成了。服务器由于需要给众多客户端一个明确的连接地址和端口，所以需要额外的绑定端口操作**。下图为UDP客户端和UDP服务器之间的通信流程。

![](/assets/udp03.png)

