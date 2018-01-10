'''功能：从twisted.internet模块导入reactor
        示例启动reactor：reactor.run()   启动反应器
        此时程序会一直运行等待直到被强制终止
        这个现象不同于while循环，这里不占有CPU资源
'''

from twisted.internet import reactor

print('开始运行Running the reactor。。。')

reactor.run()

print('结束运行reactor。。。')


