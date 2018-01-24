"""查看状态数"""
'''
@Time    : 2018/1/22 上午11:16
@Author  : scrappy_zhang
@File    : net03_threading_enumerate.py
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

    while True:
        length = len(threading.enumerate()) # 当前线程数量
        print('通过active_count查询到的线程数：', threading.active_count()) # 当前线程的数量
        print(threading.enumerate()) # 打印显示目前还存在的线程
        print('当前运行的线程数为：%d' % length)
        if length <= 1: # 除了两个子进程，还有默认的父进程，所以当唱歌跳舞执行完毕后，还剩一个线程
            break

        time.sleep(0.5)