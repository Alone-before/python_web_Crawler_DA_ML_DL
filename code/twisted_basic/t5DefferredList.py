# 有时候需要同时保持多个非同步任务，且并非同时完成
# 例如： 有时需要建立一个端口扫描器运行testConnect函数来对应一个端口范围
# 可以使用DeferredList对象来实现

from twisted.internet import reactor, defer
from t4Defferred_addErrback import testConnect

# 为了简便，直接把t4Defferred_addErrback.py中的testConnect导入使用

def handleAllResules(results, ports):

    for port, resultinfo in zip(ports, results):
        '''
        在Deferred完成时，第一个回传值是True，第二个参数是Deferred回传结果
        在Deferred失败时，第一个回传值是False，第二个参数是Failure对象包装的异常。
        '''
        success, result = resultinfo

        if success:
            print('连接到端口%d' % port)

    reactor.stop()


import sys


host = sys.argv[1]
ports = range(8079, 8082)

testers = [testConnect(host, port) for port in ports]  # 将每一个testConnect()返回的Deferred对象存贮为一个列表
# DeferredList会跟踪所有的Deferred对象结果并传递作为首参数，即handleAllResults里的results参数
# consumeErrors=True 代表Defferredlist完成了吸收Deferred的所有错误。
defer.DeferredList(testers, consumeErrors=True).addCallback(handleAllResules, ports)

reactor.run()