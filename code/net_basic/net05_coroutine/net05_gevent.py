"""gevent 实现协程"""
'''
@Time    : 2018/1/23 下午5:30
@Author  : scrappy_zhang
@File    : net05_gevent.py
'''

import time
import gevent
# 默认协程不切换，需要使用monkey此语句来破解
from gevent import monkey

monkey.patch_all()


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)
    g1.join() #阻塞等待协程运行完成再结束线程 另一种方式为joinall，可参考并发下载中的代码
    g2.join()
