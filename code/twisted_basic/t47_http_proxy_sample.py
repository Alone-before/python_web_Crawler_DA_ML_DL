# 简单的服务器代理示例
# 通过在电脑网络设置代理localhost ：8001 实现可以监测日志并打印输出信息
from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import sys

log.startLogging(sys.stdout) # 将HTTP日志信息记录在stdout中并直接查看


class ProxyFactory(http.HTTPFactory):
    protocol = proxy.Proxy

reactor.listenTCP(8001, ProxyFactory())

reactor.run()