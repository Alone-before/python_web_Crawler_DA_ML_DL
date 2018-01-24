"""死锁"""
'''
@Time    : 2018/1/22 下午3:02
@Author  : scrappy_zhang
@File    : net03_dead_lock.py
'''

import threading

global_num = 0 # 全局变量

class Sing(threading.Thread):
    def run(self):
        global global_num
        print('开始：全局变量sing global_num= ', global_num)
        for i in range(10000000):
            mutex.acquire() # 锁定全局变量
            global_num = global_num + 1
            # mutex.release() # 释放全局变量
        print('结束：全局变量sing global_num= ', global_num)


class Dance(threading.Thread):
    def run(self):
        global global_num
        print('开始：全局变量dance global_num= ', global_num)
        for i in range(10000000):
            mutex.acquire()  # 锁定全局变量
            global_num = global_num + 1
            mutex.release()  # 释放全局变量
        print('结束：全局变量dance global_num= ', global_num)


if __name__ == '__main__':
    mutex = threading.Lock()
    print('开始：全局变量main global_num= ', global_num)
    my_sing = Sing()
    my_dance = Dance()
    my_sing.start()
    my_dance.start()
    my_sing.join()
    my_dance.join()
    print('结束：全局变量main global_num= ', global_num)