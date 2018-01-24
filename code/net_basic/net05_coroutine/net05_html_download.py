"""gevent 协程实现多个html网页抓取下载"""
'''
@Time    : 2018/1/23 下午5:40
@Author  : scrappy_zhang
@File    : net05_html_download.py
'''

from gevent import monkey
import gevent
import urllib.request

monkey.patch_all()


def my_download(url):
    print('GET: %s' % url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    input_file = url.lstrip('http://www.').rstrip('.com/') + '.html'
    with open(input_file, 'wb') as html_in_file:
        html_in_file.write(data)
    print('%d bytes received from %s.' % (len(data), url))

# joinall 为阻塞主程序使得列表内所有协程完成
gevent.joinall([
    gevent.spawn(my_download, 'http://www.baidu.com/'),
    gevent.spawn(my_download, 'http://www.163.com/'),
    gevent.spawn(my_download, 'http://www.hao123.com/')
])
