'''功能：从twisted.internet模块导入reactor
        示例对比观看callLater的顺序
        示例终止reactor：reactor.stop()   终止反应器
        此时程序会一直运行到reactor.stop()被调用
        其中，reactor.callLater(等待的秒数，调用的函数) 是用来未来定时调用某函数的。
        可以看到，callLater可以进行参数回传调用
'''

from twisted.internet import reactor
import time


def printTime(x=0):
    print(x, 'Current time is ', time.strftime('%H:%M:%S'))

def stopReactor():
    print('Stopping reactor...')
    reactor.stop()  # 终止reactor

for i in range(5):
    if i == 0 :
        reactor.callLater(3, stopReactor) # 启动到第3秒时调用终止reactor，但是已经调用的函数则会执行完毕
    else:
        reactor.callLater(5-i, printTime, x=(5-i))

print('开始运行Running the reactor。。。')
reactor.run()

print('结束运行reactor。。。')
