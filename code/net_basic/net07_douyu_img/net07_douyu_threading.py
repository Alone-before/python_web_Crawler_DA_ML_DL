"""多线程抓取斗鱼美女主播首页美女主播图片"""
'''
@Time    : 2018/1/23 下午5:59
@Author  : scrappy_zhang
@File    : net07_douyu_threading.py
'''

import urllib.request
import re
import time
import threading

max_retry_count = 3


def down_img(url):
    """
    下载图片
    https://rpic.douyucdn.cn/live-cover/appCovers/2017/10/24/12017.jpg
    """
    for i in range(max_retry_count):
        try:
            response = urllib.request.urlopen(url)
            # bytes
            data = response.read()

            # 从url中得到文件名
            file_name = url[url.rfind('/') + 1:]

            # 打开文件用以写入
            with open("img/" + file_name, "wb") as file:
                file.write(data)

        except Exception as e:
            print("出错 %s 正在重试" % e)
        else:
            break


if __name__ == '__main__':

    start = time.time()  # 程序大约的开始时间

    home = """https://www.douyu.com/directory/game/yz?page=1&isAjax=1"""  # 首页地址
    # 请求的时候需要带上头部 可以防止初步的反爬措施
    headers = {
        "Host": "www.douyu.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/62.0.3202.94 Safari/537.36"
    }

    # 构造好请求对象 将请求提交到服务器 获取的响应就是到首页的html代码
    request = urllib.request.Request(url=home, headers=headers)

    # urlopen函数可以直接传入url网址 也可以指定好一个请求对象
    response = urllib.request.urlopen(request)

    # 将收到的响应对象中数据的bytes数据读出出来 并且解码
    html_data = response.read().decode()

    # 使用正则 从所要抓取的网页中 提取出所有美女主播的图片链接，并存入一个列表
    img_list = re.findall(r"https://.*?\.(?:jpg)", html_data)

    # 下载美女主播图片
    for img_url in img_list:
        td = threading.Thread(target=down_img, args=(img_url,))
        td.start()
    # 阻塞程序直到所有线程运行完毕
    while True:
        length = len(threading.enumerate())
        if length == 1:
            break
    end = time.time()  # 程序大约的结束时间
    print('耗时：', end - start)
