"""进程间不共享全局变量"""
'''
@Time    : 2018/1/22 下午4:32
@Author  : scrappy_zhang
@File    : net04_global_variables.py
'''
import multiprocessing
import time

global_num = 0


def sing():
    global global_num
    print('开始：全局变量sing global_num= ', global_num)
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        global_num = global_num + 1  # 修改全局变量
        time.sleep(1)  # 休息1秒
    print('结束：全局变量sing global_num= ', global_num)


def dance():
    global global_num
    print('开始：全局变量dance global_num= ', global_num)
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        global_num = global_num + 1  # 修改全局变量
        time.sleep(1)  # 休息1秒
    print('结束：全局变量dance global_num= ', global_num)


if __name__ == '__main__':
    print('开始：全局变量main global_num= ', global_num)
    p1 = multiprocessing.Process(target=sing)  # 创建唱歌进程
    p2 = multiprocessing.Process(target=dance)  # 创建跳舞进程
    p1.start()
    p2.start()
    p1.join()  # 待子进程p1执行完毕后再执行下面的语句
    p2.join()  # 待子进程p2执行完毕后再执行下面的语句
    print('结束：全局变量main global_num= ', global_num)
