"""单线程唱歌跳舞"""
'''
@Time    : 2018/1/22 上午10:00
@Author  : scrappy_zhang
@File    : net03_sing_dance.py
'''

import time


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1) # 休息1秒


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1) # 休息1秒

if __name__ == '__main__':
    sing() # 唱歌
    dance() # 跳舞

