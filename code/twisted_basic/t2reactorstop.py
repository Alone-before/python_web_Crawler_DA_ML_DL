'''功能：从twisted.internet模块导入reactor
        示例终止reactor：reactor.stop()   终止反应器
        此时程序会一直运行到reactor.stop()被调用
        其中，reactor.callLater(等待的秒数，调用的函数) 是用来未来定时调用某函数的。
'''

from twisted.internet import reactor
import time


def printTime():
    print('Current time is ', time.strftime('%H:%M:%S'))

def stopReactor():
    print('Stopping reactor...')
    reactor.stop()  # 终止reactor

for i in range(5):
    if i == 4 :
        reactor.callLater(i+1, stopReactor) # 启动到第五秒时调用终止reactor
    else:
        reactor.callLater(i+1, printTime)

print('开始运行Running the reactor。。。')
reactor.run()

print('结束运行reactor。。。')
