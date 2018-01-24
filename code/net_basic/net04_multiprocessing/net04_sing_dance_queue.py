"""Queue"""
'''
@Time    : 2018/1/22 下午4:58
@Author  : scrappy_zhang
@File    : net04_sing_dance_queue.py
'''

import multiprocessing
import time


def sing(name, sing_name):
    for i in range(5):
        print(name, '正在唱歌%s呢 %d' % (sing_name, i))
        time.sleep(1)  # 休息1秒
    while True:
        if not q.empty():
            value = q.get() # 从队列中读取数据
            print('Jam收到了', value)
        else:
            break


def dance(**kwargs):
    dancer = kwargs['dancer']
    q.put('花') # 向队列中写入花数据
    print('杰克逊向Jam递了一朵花')
    for i in range(5):
        print('%s正在伴舞呢 %d' % (dancer, i))
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    singer = 'Jam'
    sing_name = '不露声色'
    q = multiprocessing.Queue() # 创建队列
    p1 = multiprocessing.Process(target=sing, args=(singer, sing_name))  # 创建唱歌进程
    p2 = multiprocessing.Process(target=dance, kwargs={'dancer': '杰克逊'})  # 创建跳舞进程
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance
