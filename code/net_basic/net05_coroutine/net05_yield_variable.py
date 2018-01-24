"""yield 传递参数"""
'''
@Time    : 2018/1/23 下午5:02
@Author  : scrappy_zhang
@File    : net05_yield_variable.py
'''


def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('send过来的值为', temp)
        i += 1


f = gen()
# 在第一次唤醒生成器代码的时候　必须使用next(f) -- 在生成器代码第一次执行的时候　没有可以接收参数的功能
print('第一次传递过来的值为', next(f))

while True:
    try:
        # value = next(f)
        value = f.send(100)

    except Exception as e:
        print('结束')
        break
    else:
        print("传递过来元素的值是%d" % value)
    finally:
        pass
