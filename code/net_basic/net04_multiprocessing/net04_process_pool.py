"""进程池"""
'''
@Time    : 2018/1/22 下午5:09
@Author  : scrappy_zhang
@File    : net04_process_pool.py
'''

import multiprocessing
import time


def sing(singer_num, sleep_time):
    for i in range(4):
        print('歌手', singer_num, '正在唱歌呢 %d' % i)
        time.sleep(sleep_time)  # 休息


if __name__ == '__main__':
    processes = multiprocessing.Pool(3) # 创建进程池，最大进程数为3
    for i in range(5):
        processes.apply_async(sing, (i + 1, 1 + 0.3 * i)) # 进程池创建进程 ，传入参数为歌手编号和歌唱间隔休息时间

    print('歌唱开始')
    processes.close()
    processes.join()
    print('歌唱结束')
