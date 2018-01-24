"""map"""
'''
@Author  : scrappy_zhang
@File    : net11_map.py
'''
from concurrent.futures import ThreadPoolExecutor as Pool
import requests

URLS = ['http://www.baidu.com', 'http://qq.com', 'http://sina.com']


def task(url, timeout=10):
    return requests.get(url, timeout=timeout)


pool = Pool(max_workers=3)
results = pool.map(task, URLS)

for ret in results:
    print('%s, %s' % (ret.url, len(ret.content)))