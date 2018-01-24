"""线程间共享全局变量"""
'''
@Time    : 2018/1/22 下午2:03
@Author  : scrappy_zhang
@File    : net03_global_variables.py
'''

import threading
import time

global_num = 0 # 全局变量

class Sing(threading.Thread):
    def run(self):
        for i in range(3):
            print('正在唱歌呢 %d' % i)
            global global_num
            global_num = global_num + i # 修改全局变量
            time.sleep(1)  # 休息1秒
        print('全局变量sing global_num= ', global_num)


class Dance(threading.Thread):
    def run(self):
        for i in range(3):
            print('正在跳舞呢 %d' % i)
            time.sleep(1)  # 休息1秒
        global global_num
        print('全局变量dance global_num= ', global_num)


if __name__ == '__main__':
    my_sing = Sing()
    my_dance = Dance()
    my_sing.start()
    my_dance.start()
    my_sing.join()  # 待子进程结束后再向下执行
    my_dance.join()  # 待子进程结束后再向下执行
    print('全局变量main global_num= ', global_num)
