# 简单的HTTP服务器
# 收到浏览器的请求，将其打印出来，并将浏览器的请求信息发送给浏览器显示
# 简单的显示固定内容而已

from twisted.protocols import basic
from twisted.internet import protocol, reactor


class HttpEchoProtocol(basic.LineReceiver):

    def __init__(self):
        self.lines = [] # 自定义一个变量lines来存储浏览器的请求头信息
        self.gotRequest = False # 自定义一个变量来确定是否已得到请求头信息

    def lineReceived(self, line):
        self.lines.append(line.decode()) # 从浏览器发送过来的数据均存储在self.lines中。当遇到空行，头字段结束
        print('请求信息： ', line.decode())

        if not line.decode() and not self.gotRequest: # 遇到空行代表请求头字段已结束，可以发送响应信息了
            self.sendResponse()
            self.gotRequest=True

    def sendResponse(self): # 发送响应信息
        responseBody = 'You said:\r\n\r\n' + '\r\n'.join(self.lines)
        # print(responseBody)
        self.sendLine('HTTP/1.0 200 OK'.encode()) # 响应HTTP版本和状态码   sendLine()发送的数据是bytes型
        self.sendLine('Content-Type: text/plain'.encode()) # 内容格式
        self.sendLine(('Content-Length: %d' % len(responseBody.encode())).encode()) # 内容长度
        self.sendLine(''.encode()) # 空行
        self.transport.write(responseBody.encode()) # 响应体
        self.transport.loseConnection() # 关闭连接

if __name__ == '__main__':
    f = protocol.ServerFactory()  # 直接采用ServerFactory()对象
    f.protocol= HttpEchoProtocol

    reactor.listenTCP(8000, f)

    reactor.run()

