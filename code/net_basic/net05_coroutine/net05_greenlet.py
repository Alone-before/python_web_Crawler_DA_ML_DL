"""greenlet 实现协程"""
'''
@Time    : 2018/1/23 下午5:17
@Author  : scrappy_zhang
@File    : net05_greenlet.py
'''

import time
from greenlet import greenlet  # 导入greenlet.greenlet


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        d1.switch()  # 切换到跳舞函数
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        s1.switch()  # 切换到唱歌函数
        time.sleep(1)


if __name__ == '__main__':
    s1 = greenlet(sing)  # 唱歌
    d1 = greenlet(dance)  # 跳舞
    s1.switch()  # 切换到唱歌函数
