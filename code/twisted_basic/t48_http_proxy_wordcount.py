# 两个功能：
# 1、实现localhost：8001网络代理功能，可以统计访问页面的text格式的单词数量（仅简单演示用，复杂网站可能不能实现（无解压等技术），
# 可利用t44http_resourcetree做的http服务器进行访问测试效果）
#  实现网络代理：同时作为服务端和客户端
# 2、访问localhost：8000 可以获得页面统计结果，简单的访问响应功能
from html.parser import HTMLParser
from twisted.web import proxy, http
import sys
from twisted.python import log
import re

log.startLogging(sys.stdout)

WEB_PORT = 8000

PROXY_PORT = 8001

'''
三大类：
1、字符解析类、字符统计类
2、作为8000端口的网络代理
2.1 HTTP代理：HTTP连接管理类、HTTP连接处理类、HTTP连接响应类（调用字符解析）
2.2 客户端：连接管理类、连接处理类
3、作为8001端口的服务器：
    HTTP连接管理类、HTTP连接处理类、HTTP连接响应类（发送字符统计结果）
    
也就是说，真正干活的就只有四个类。其他都是连接
'''


class WordParser(HTMLParser):
    '''用来解析单词'''
    def __init__(self):
        HTMLParser.__init__(self)
        self.chardata = []
        self.inBody = False

    def start_body(self, attrs):
        self.inBody = True

    def end_body(self):
        self.inBody = False

    def handle_data(self, data):
        # if self.inBody:
        self.chardata.append(data)
    def getWords(self):
        '''从字符串中解出单词'''
        wordFinder = re.compile(r'\w*')
        words = wordFinder.findall(''.join(self.chardata))
        words = list(filter(lambda word: word.strip(), words))
        # filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，
        # filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
        # python2 和 python3不同
        # print('单词有：', words)
        return words


class WorldCount():
    '''计算单词数量'''
    ignoredWords = 'the a of in from to this that and or but is was be can could i you they' \
                   'we at'.split()

    def __init__(self):
        self.words = {}

    def addWords(self, words):
        for word in words:
            word = word.lower()
            if not (word in self.ignoredWords):
                currentCount = self.words.get(word, 0) # 若self.words中存在word，则返回其数值；若不存在则返回0
                self.words[word] = currentCount + 1


class WordCountProxyClient(proxy.ProxyClient):
    '''作为客户端成功连接处理：调用解析单词的类'''
    def handleHeader(self, key, value):
        proxy.ProxyClient.handleHeader(self, key, value)
        if key.lower() == b'content-type':
            if value.decode().split(';')[0] == 'text/html':
                self.parser = WordParser()

    def handleResponsePart(self, buffer):
        proxy.ProxyClient.handleResponsePart(self, buffer)
        if hasattr(self, 'parser'):
            self.parser.feed(buffer.decode())
            self.father.wordCounter.addWords(self.parser.getWords())
            del self.parser


class WordCountProxyClientFactory(proxy.ProxyClientFactory):
    '''作为客户端连接管理'''
    def buildProtocol(self, addr):
        client = proxy.ProxyClientFactory.buildProtocol(self, addr)
        # 升级proxy.proxyClient对象到WordCountProxyClient
        client.__class__ = WordCountProxyClient

        return client


class WordCountProxyRequest(proxy.ProxyRequest):
    '''作为服务器，响应客户端连接'''
    protocols = {b'http': WordCountProxyClientFactory}

    def __init__(self, wordCounter, *args):
        self.wordCounter = wordCounter
        proxy.ProxyRequest.__init__(self, *args)


class WordCountProxy(proxy.Proxy):
    '''Proxy是HTTPChannel的子类，处理每一个proxy的成功连接'''
    def __init__(self, wordCounter):
        self.wordCounter = wordCounter
        proxy.Proxy.__init__(self)

    def requestFactory(self, *args):
        return WordCountProxyRequest(self.wordCounter, *args)


class WordCountProxyFactory(http.HTTPFactory):
    '''管理代理8000通信连接'''
    def __init__(self, wordCount):
        self.wordCounter = wordCount
        http.HTTPFactory.__init__(self)

    def buildProtocol(self, addr):
        protocol = WordCountProxy(self.wordCounter)
        return protocol

# 使用WEB接口展示记录的接口.即 下面的类与统计代理无关，仅是浏览器响应服务器8000
# 统计完页面单词后，用浏览器打开localhost：8000  得到统计结果

class WebReportRequest(http.Request):
    '''重载process方法'''
    def __init__(self, wordCounter, *args):
        self.wordCounter = wordCounter
        http.Request.__init__(self, *args)

    def process(self):
        '''响应处理，将统计信息发给客户端'''
        self.setHeader(b'Content-Type', b'text/html')
        words = self.wordCounter.words
        words_temp = sorted(words.items(), key=lambda item: item[1], reverse=True) # 数量越多的单词先显示。

        for word, count in words_temp:
            self.write(('<li>%s %s</li>' % (word, count)).encode()) # 发送信息

        self.finish()


class WebReportChannel(http.HTTPChannel):
    '''成功连接处理类'''
    def __init__(self, wordCounter):
        self.wordCounter = wordCounter
        http.HTTPChannel.__init__(self)

    def requestFactory(self, *args):
        return WebReportRequest(self.wordCounter, *args)


class WebReportFactory(http.HTTPFactory):
    '''管理8888端口的连接事务'''
    def __init__(self, wordCounter):
        self.wordCounter = wordCounter
        http.HTTPFactory.__init__(self)

    def buildProtocol(self, addr):
        return WebReportChannel(self.wordCounter)


if __name__ == '__main__':
    from twisted.internet import reactor

    counter = WorldCount()

    prox = WordCountProxyFactory(counter)
    reactor.listenTCP(PROXY_PORT, prox)


    reactor.listenTCP(WEB_PORT, WebReportFactory(counter))

    reactor.run()
