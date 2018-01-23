# 6 协程

## 6.1 协程

协程，又称微线程，纤程。英文名Coroutine。

协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。

子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。

所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。

子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。

协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：

```
def A():
    print('1')
    print('2')
    print('3')

def B():
    print('4')
    print('5')
    print('6')
```

正常情况下，会输出123456 。假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：

```
1
2
4
5
3
6
```

但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。

看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？

最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。

**注：在实现多任务时, 线程切换从系统层面远不止保存和恢复 CPU上下文这么简单。 操作系统为了程序运行的高效性每个线程都有自己缓存Cache等等数据，操作系统还会帮你做这些数据的恢复操作。 所以线程的切换非常耗性能。但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。**

## 6.2 python通过生成器实现协程

Python对协程的支持是通过generator生成器实现的。在generator生成器中，我们不但可以通过`for`循环来迭代，还可以不断调用`next()`函数获取由`yield`语句返回的下一个值。Python的`yield`不但可以返回一个值，它还可以接收调用者发出的参数。

**yield的作用**

**挂起当前函数，将yield后面的值当做返回给调用生成器的地方；能够在唤醒生成器函数的时候，回复代码继续紧接着从上次执行的地方执行（可以接受额外的参数）**

```py
'''net05_yield.py'''
import time


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        yield
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        yield
        time.sleep(1)

if __name__ == '__main__':
    s1 = sing() # 唱歌
    d1 = dance() # 跳舞
    i = 5
    while i > 0:
        next(s1) # next获取由yield语句的协程切换
        next(d1)
        i -= 1
```

结果如下：

```
正在唱歌呢 0
正在跳舞呢 0
正在唱歌呢 1
正在跳舞呢 1
正在唱歌呢 2
正在跳舞呢 2
正在唱歌呢 3
正在跳舞呢 3
正在唱歌呢 4
正在跳舞呢 4
```

首先，我们应当注意到代码中的sing和dance函数中的**for循环是一个生成器**，这是python协程的前提。通过yield实现协程切换，next来调用完成各生成器的下一步动作。整个过程在一个线程内完成，非常高效；不需要多线程的锁，不存在线程安全问题。

需要注意的是：在用yield来完成send参数传递时需要先执行一次next，然后才可以send传递参数。可以看例子：

在第一次唤醒生成器代码时，我们使用next\(f\)。在后续的协程切换中，我们使用f.send\(100\)来讲参数100传递给gen中的temp；通过value = f.send\(\)将yield返回的值i赋给value。

```py
'''net05_yield_variable.py'''
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
```

结果：

```
第一次传递过来的值为 0
send过来的值为 100
传递过来元素的值是1
send过来的值为 100
传递过来元素的值是2
send过来的值为 100
传递过来元素的值是3
send过来的值为 100
传递过来元素的值是4
send过来的值为 100
结束
```

## 6.3 协程——greenlet

为了更好使用协程来完成多任务，python中的greenlet模块对其协程进行了封装，从而省去next等使得切换任务变的更加简单。我们可以通过`pip install greenlet`安装并使用它。

它一般通过创建greenlet对象，并在相应的代码块里假如switch语句来实现不同函数间的切换。来继续修改唱歌跳舞例子：

```py
'''net05_greenlet.py'''
import time
from greenlet import greenlet  # 导入greenlet.greenlet


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        d1.switch()  # 切换到跳舞函数
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        s1.switch()  # 切换到唱歌函数
        time.sleep(1)


if __name__ == '__main__':
    s1 = greenlet(sing)  # 唱歌
    d1 = greenlet(dance)  # 跳舞
    s1.switch()  # 切换到唱歌函数
```

结果如下：

```
正在唱歌呢 0
正在跳舞呢 0
正在唱歌呢 1
正在跳舞呢 1
正在唱歌呢 2
正在跳舞呢 2
正在唱歌呢 3
正在跳舞呢 3
正在唱歌呢 4
正在跳舞呢 4
```

我们首先创建了两个greenlet实例对象，然后从主程序通过s1.switch\(\)切换到sing函数进行唱歌模块。在sing函数中我们又通过d1.switch\(\)切换到跳舞函数模块；在dance函数中通过s1.switch\(\)切换到sing函数。这样便实现了交替切换执行。就像我们分析的那样，它确实简化了next等操作，但是**需要开发者手动设置switch来实现不同函数之间的切换**。

## 6.4 协程——gevent

正如上一节所说，greenlet需要手动设置切换，并不友好，所以本节介绍一个更友好的协程模块gevent。我们可能需要通过`pip install gevent`来安装它。

gevent原理是当一个greenlet遇到IO\(指的是input output 输入输出，比如网络、文件操作等\)操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

gevent一般通过以下语句创建协程并执行：

```
gevent.spawn(函数名，参数)
```

但是它创建的协程默认不自动切换，需要使用gevent包的monkey来进行破解切换，语句如下：

```
from gevent import monkey
monkey.patch_all()
```

我们继续修改我们的唱歌跳舞实例，以gevent协程的方式来实现同时唱歌跳舞：

```py
'''net05_gevent.py'''
import time
import gevent
# 默认协程不切换，需要使用monkey此语句来破解
from gevent import monkey

monkey.patch_all()


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1)


if __name__ == '__main__':
    g1 = gevent.spawn(sing)
    g2 = gevent.spawn(dance)
    g1.join()
    g2.join()
```

结果是一样的，至此，我们分别通过多线程、多进程和协程三种方式实现了同时唱歌跳舞。

```
正在唱歌呢 0
正在跳舞呢 0
正在唱歌呢 1
正在跳舞呢 1
正在唱歌呢 2
正在跳舞呢 2
正在唱歌呢 3
正在跳舞呢 3
正在唱歌呢 4
正在跳舞呢 4
```

## 6.5 进程、线程、协程区别

* 进程是资源分配的单位
* 线程是操作系统调度的单位
* 进程切换需要的资源很最大，效率很低
* 线程切换需要的资源一般，效率一般
* 协程切换任务资源很小，效率高
* 多进程、多线程根据cpu核数不一样可能是并行的 也可能是并发的。协程的本质就是使用当前进程在不同的函数代码中切换执行，可以理解为并行。 协程是一个用户层面的概念，不同协程的模型实现可能是单线程 也可能是多线程。

## 6.7 协程实现网页并发下载

### 需求实现：

通过gevent协程来同时下载百度、163、hao123的主页html并保存到本地。

### 完整源代码：

```py
'''net05_html_download.py'''
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

```







