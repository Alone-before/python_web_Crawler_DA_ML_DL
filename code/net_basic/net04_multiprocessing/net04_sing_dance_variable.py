"""进程传递参数"""
'''
@Time    : 2018/1/22 下午4:22
@Author  : scrappy_zhang
@File    : net04_sing_dance_variable.py
'''

import multiprocessing
import time


def sing(name, sing_name):
    for i in range(5):
        print(name, '正在唱歌%s呢 %d' % (sing_name, i))
        time.sleep(1)  # 休息1秒


def dance(**kwargs):
    dancer = kwargs['dancer']
    for i in range(5):
        print('%s正在伴舞呢 %d' % (dancer,i))
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    singer = 'Jam'
    sing_name = '不露声色'
    p1 = multiprocessing.Process(target=sing, args=(singer, sing_name))  # 创建唱歌进程,告诉子进程是Jam唱不露声色
    p2 = multiprocessing.Process(target=dance,kwargs={'dancer':'杰克逊'})  # 创建跳舞进程，告诉子进程是杰克逊来唱歌啦
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance