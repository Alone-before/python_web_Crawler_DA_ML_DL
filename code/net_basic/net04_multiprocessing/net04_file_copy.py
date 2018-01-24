"""多进程实现文件拷贝"""
'''
@Time    : 2018/1/23 下午4:03
@Author  : scrappy_zhang
@File    : net04_file_copy.py
'''

import multiprocessing
import os
import time
import random


def copy_file(file_name, src, dest, queue):
    '''拷贝文件的函数'''
    src_file = open(src + '/' + file_name, 'rb')
    dest_file = open(dest + '/' + file_name, 'wb')

    while True:
        time.sleep(random.random())
        data = src_file.read(4096)
        if data:
            dest_file.write(data)
        else:
            break
    src_file.close()
    dest_file.close()
    queue.put(file_name)


if __name__ == '__main__':
    src_path = input('请输入你要拷贝的目录名：')
    try:
        dest_path = src_path + '-备份'
        os.mkdir(dest_path)
        file_list = os.listdir(src_path)
    except Exception as e:
        print(e)
    else:
        queue = multiprocessing.Queue()

        for file in file_list:
            pro = multiprocessing.Process(
                target=copy_file, args=(file, src_path, dest_path, queue)
            )
            pro.start()

        count = 0
        while True:
            queue.get()
            count += 1
            print('\r当前进度为%d%%' % (100.0 * count / len(file_list)),end='')
            if count == len(file_list):
                break
