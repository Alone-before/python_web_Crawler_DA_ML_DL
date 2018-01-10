# 发送与接收
# 通过标准I/O来进行数据发送和接收，将接收到的数据传递到标准输出，并打印数据到标准输出
# 验证：可以通过网络调试助手服务器两边互发数据
#       也可以通过GET / HTTP/1.1\r\nHost: example.webscraping.com\r\nUser-Agent: wswb\r\n\r\n
#       来实现HTTP操作得到网站webscraping返回值

from twisted.internet import stdio, reactor, protocol
# from twisted.protocols import basic
import re


class DataForwardingProtocol(protocol.Protocol):

    def __init__(self):
        self.output = None
        self.normalizeNewLines = False

    def dataReceived(self, data):

        data = data.decode()
        # print(data)
        if self.normalizeNewLines:
            data = re.sub(r'\r\n|\n', '\r\n', data) # 转换成常见的网络格式\r\n
            # print(data)
        if self.output:
            self.output.write(data.encode())   # 将接受到的数据写入self.output
            # print(self.output)


class StdioProxyProtocol(DataForwardingProtocol):

    def connectionMade(self):
        inputForwarder = DataForwardingProtocol()
        inputForwarder.output = self.transport # 将transport传递给inputForwarder.output
        inputForwarder.normalizeNewLines = True
        # 将实例对象的输出转换传递到为标准I/O输出
        stdioWarpper = stdio.StandardIO(inputForwarder)
        self.output = stdioWarpper
        print('连接到服务器，可以按CTRL+C关闭连接')
        # print(self.output)

class StdioProxyFactory(protocol.ClientFactory):

    protocol=StdioProxyProtocol

    def clientConnectionLost(self, connector, reason):
        # print('1')
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        print(reason.getErrorMessage())
        # print('2')
        reactor.stop()

if __name__ == '__main__':
    import sys

    if not len(sys.argv)==3:
        print('格式不对：%s host port' % __file__)
        sys.exit(1)

    reactor.connectTCP(sys.argv[1], int(sys.argv[2]), StdioProxyFactory())
    reactor.run()