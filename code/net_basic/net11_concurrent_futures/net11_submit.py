"""submit"""
'''
@Author  : scrappy_zhang
@File    : net11_submit.py
'''

from concurrent.futures import ThreadPoolExecutor
import time


def return_future(msg):
    time.sleep(1)
    return msg


# 创建一个线程池
pool = ThreadPoolExecutor(max_workers=2)

# 往线程池加入2个task
f1 = pool.submit(return_future, 'hello')
f2 = pool.submit(return_future, 'world')
time.sleep(0.9)
print(f1.done()) # 判断线程f1是否已执行
time.sleep(1)
print(f2.done())

print(f1.result()) # 输出结果
print(f2.result())