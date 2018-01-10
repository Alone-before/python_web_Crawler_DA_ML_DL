# Deferred（延迟）的目的:保持对非同步活动的跟踪，并且获得活动结束时的结果
# 默认状态下，reactor不会因为所调用的业务代码出现异常而退出，
# 但是实际场景中有些异常需要合适的退出，这就需要使用Deferred来进行对非同步活动的跟踪

# 代码实现了根据deferred返回结果调用合适的事件处理。即reactor调用的业务代码在出现异常时也可以结束reactor

from twisted.internet import reactor, defer, protocol


class CallbackAndDisconnectProtocol(protocol.Protocol):

    def connectionMade(self):
        '''连接完成时调用此方法'''
        self.factory.deferred.callback('Connected!')  # 调用此告知连接成功给deferred
        self.transport.loseConnection() # 关闭连接


class ConnectionTestFactory(protocol.ClientFactory):

    protocol=CallbackAndDisconnectProtocol

    def __init__(self):
        self.deferred = defer.Deferred()  # 初始化建立一个Deferred对象

    def clientConnectionFailed(self, connector, reason):
        # 返回给deferred错误时的信息
        self.deferred.errback(reason)  # reason是twisted.python.failure.Failure对象，里面封装了异常的原因


def testConnect(host, port):
    '''创建自定义管理连接类对象
        创建TCP连接'''
    testFactory = ConnectionTestFactory()
    reactor.connectTCP(host, port, testFactory)

    return testFactory.deferred   # 连接成功时，返回stFactory.deferred属性，用于跟踪Defferred对象


def handleSuccess(result, port):   # 事件处理器函数：连接成功时执行的信息
    '''输出连接端口信息，并终止reactor'''
    print('连接到端口port： %d' % port)
    reactor.stop()


def handleFailure(failure, port): # 事件处理器函数：连接错误时执行的信息
    print('连接错误,port： %d：%s' % (port, failure.getErrorMessage()))
    reactor.stop()


if __name__ == '__main__':

    import sys
    if not len(sys.argv) == 3:
        print('输入格式错误,请按照格式：python 4Deferred_addErrback.py host port')
        sys.exit(1)

    host=sys.argv[1]
    port=int(sys.argv[2])

    connecting = testConnect(host, port)

    connecting.addCallback(handleSuccess, port) #对应第10行， 成功时调用Derred的callback

    connecting.addErrback(handleFailure, port) #对应第22行，出错时，调用Derred的errback

    reactor.run()