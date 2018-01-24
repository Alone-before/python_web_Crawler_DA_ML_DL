"""自定义 Thread子类"""
'''
@Time    : 2018/1/22 上午11:51
@Author  : scrappy_zhang
@File    : net03_Thread_subclass.py
'''
import threading
import time


class Sing(threading.Thread):
    def run(self):
        for i in range(5):
            print('正在唱歌呢 %d' % i)
            time.sleep(1)  # 休息1秒


class Dance(threading.Thread):
    def run(self):
        for i in range(5):
            print('正在跳舞呢 %d' % i)
            time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    my_sing = Sing()
    my_dance = Dance()
    my_sing.start()
    my_dance.start()
