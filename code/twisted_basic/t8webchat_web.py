# twisted.web
# 请求网页并打印

from twisted.web import client
from twisted.internet import reactor
import sys

def printPage(data):
    print(data.decode())
    # reactor.stop()

def printError(failure):
    print('>>',sys.stderr, 'Error:', failure.getErrorMessage())
    reactor.stop()

# def downDone(data):
#     print('下载完成')
#     reactor.stop()


if __name__ == '__main__':

    url = 'http://www.baidu.com'

    # url = str(sys.argv[1])
    # client.getPage(url) 获取网页，但是url为bytes型
    # client.getPage(url) 返回了Deferred对象，用于非同步状态下通知下载完成时间
    client.getPage(url.encode()).addCallback(printPage).addErrback(printError)
    # client.downloadPage(url.encode(),'baidu1.html').addCallback(downDone).addErrback(printError) # 下载网页到某文件
    reactor.run()

