"""线程间全局资源竞争"""
'''
@Time    : 2018/1/22 下午2:22
@Author  : scrappy_zhang
@File    : net03_global_variable_competition.py
'''
import threading

global_num = 0 # 全局变量

class Sing(threading.Thread):
    def run(self):
        global global_num
        print('开始：全局变量sing global_num= ', global_num)
        for i in range(10000000):
            global_num = global_num + 1 # 修改全局变量
        print('结束：全局变量sing global_num= ', global_num)


class Dance(threading.Thread):
    def run(self):
        global global_num
        print('开始：全局变量dance global_num= ', global_num)
        for i in range(10000000):
            global_num = global_num + 1  # 修改全局变量
        print('结束：全局变量dance global_num= ', global_num)


if __name__ == '__main__':
    print('开始：全局变量main global_num= ', global_num)
    my_sing = Sing()
    my_dance = Dance()
    my_sing.start()
    my_dance.start()
    my_sing.join()  # 待子进程结束后再向下执行
    my_dance.join()  # 待子进程结束后再向下执行
    print('结束：全局变量main global_num= ', global_num)