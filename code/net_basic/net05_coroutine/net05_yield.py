"""协程"""
'''
@Time    : 2018/1/23 下午4:45
@Author  : scrappy_zhang
@File    : net05_yield.py
'''

import time


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        yield
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        yield
        time.sleep(1)

if __name__ == '__main__':
    s1 = sing() # 唱歌
    d1 = dance() # 跳舞
    i = 5
    while i > 0:
        next(s1) # next获取由yield语句的协程切换
        next(d1)
        i -= 1

