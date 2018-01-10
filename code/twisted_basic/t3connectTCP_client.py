"""本代码将实现建立一个TCP连接到baidu"""
"""ClientFactory类用来管理连接
   Protocol类对象用来处理每一个成功的连接
   transport代表当前活动连接对象
"""


from twisted.internet import reactor, protocol


class QuickDisconnectedProtocol(protocol.Protocol):
    '''继承Protocol类的子类，用来处理每一个成功的连接
    此子类实现一旦建立连接获取地址后输出，然后关闭连接
    '''
    def connectionMade(self):
        '''重载连接后成功的父类方法
           获取对方端的地址 transport.getPeer()
           获取本地端的地址 trandport.getHost()
        '''
        print('Connected to %s.' % self.transport.getPeer().host)
        self.transport.loseConnection()  # 关闭连接

class BasicClientFactory(protocol.ClientFactory):
    '''继承ClientFatory类的子类，用来管理连接
    该子类实现连接关闭或连接错误时输出具体信息，并终止reactor
    '''
    protocol=QuickDisconnectedProtocol # 调用一个Protocol子类对象

    def clientConnectionLost(self, connector, reason):
        '''重载父类方法'''
        '''输出关闭连接或断开连接的缘由信息，并随后终止reactor'''
        print('关闭 connection: %s' % reason.getErrorMessage())
        reactor.stop()

    def clientConnectionFailed(self, connector, reason):
        '''重载父类方法'''
        '''在反应器无法建立时的缘由信息，并随后终止reactor'''
        print('Connection failed: %s' % reason.getErrorMessage)
        reactor.stop()

# 创建TCP连接
# http默认端口为80，并调用自定义的管理连接类对象BasicClientFactory()
# 即连接到百度，并通过BasicClientFactory()对象来管理
reactor.connectTCP('www.baidu.com', 80, BasicClientFactory())
reactor.run()