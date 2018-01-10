# 实现从客户端单行输入数据并直接返回给客户端的服务端
# 当客户端输入quit时，关闭连接

from twisted.internet import reactor, protocol
from twisted.protocols import basic
import re


class EchoProtocol(basic.LineReceiver, protocol.Protocol):

    def lineReceived(self, line):
        line = line.decode()
        if line=='quit':
            self.sendLine('bye 再见!'.encode())
            self.transport.loseConnection()
            print('connection from %s was closed by himself!' % self.cliaddr)
        else:
            self.sendLine(('你说：' + line).encode())

    def connectionMade(self):
        self.cliaddr = self.transport.getPeer()
        print('connection from %s' % self.cliaddr.host)


class EchoServerFactory(protocol.ServerFactory):

    protocol=EchoProtocol



if __name__ == '__main__':
    port = 8888

    reactor.listenTCP(port, EchoServerFactory())
    reactor.run()
