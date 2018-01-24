"""同时唱歌跳舞"""
'''
@Time    : 2018/1/22 上午10:18
@Author  : scrappy_zhang
@File    : net03_sing_dance_threading.py
'''

import time
import threading

def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1) # 休息1秒


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1) # 休息1秒

if __name__ == '__main__':
    td1 = threading.Thread(target=sing)  # 创建唱歌子线程
    td2 = threading.Thread(target=dance) # 创建跳舞子线程
    td1.start() # 开始运行子线程
    td2.start() # 开始运行子线程