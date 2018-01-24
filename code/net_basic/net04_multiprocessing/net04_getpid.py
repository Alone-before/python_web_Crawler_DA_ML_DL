"""获取进程号"""
'''
@Time    : 2018/1/22 下午4:14
@Author  : scrappy_zhang
@File    : net04_getpid.py
'''

import multiprocessing
import os
import time


def sing():
    print('唱歌进程pid: %d' % os.getpid())
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1)  # 休息1秒


def dance():
    print('跳舞进程pid: %d' % os.getpid())
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())
    p1 = multiprocessing.Process(target=sing)  # 创建唱歌进程
    p2 = multiprocessing.Process(target=dance)  # 创建跳舞进程
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance