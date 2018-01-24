"""多进程实现唱歌跳舞"""
'''
@Time    : 2018/1/22 下午4:10
@Author  : scrappy_zhang
@File    : net04_sing_dance_multiprocess.py
'''

import multiprocessing
import time


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1)  # 休息1秒


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sing)  # 创建唱歌进程
    p2 = multiprocessing.Process(target=dance)  # 创建跳舞进程
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance
