# 5 多进程

## 5.1 进程

**程序：例如xxx.py这是程序，是一个静态的**

**进程：一个程序运行起来后，代码+用到的资源 称之为进程，它是操作系统分配资源的基本单元。**

进程的状态

工作中，任务数往往大于cpu的核数，即一定有一些任务正在执行，而另外一些任务在等待cpu进行执行，因此导致了有了不同的状态

* 就绪态：运行的条件都已经慢去，正在等在cpu执行
* 执行态：cpu正在执行其功能
* 等待态：等待某些条件满足，例如一个程序sleep了，此时就处于等待态

## 5.2 python实现多进程

我们来试想一下，在一个演唱会上，歌手歌唱、舞者翩翩起舞，各司其职才能达到较好的效果。我们可以这么理解：演唱会这个程序中有几个进程，一个是歌手歌唱，一个是舞者翩翩起舞，还有一个总协调的剧本。接下来我们就用python来实现这个想法：一个python程序有两个子进程：歌手歌唱、舞者翩翩起舞。

python中的multiprocessing模块就是跨平台版本的多进程模块，提供了一个Process类来代表一个进程对象，这个对象可以理解为是一个独立的进程，可以执行另外的事情。**Process的语法结构如下：**

`Process([group [, target [, name [, args [, kwargs]]]]])`

* target：如果传递了函数的引用，可以任务这个子进程就执行这里的代码
* args：给target指定的函数传递的参数，以元组的方式传递
* kwargs：给target指定的函数传递命名参数
* name：给进程设定一个名字，可以不设定
* group：指定进程组，大多数情况下用不到

**Process创建的实例对象的常用方法：**

* start\(\)：启动子进程实例（创建子进程）
* is\_alive\(\)：判断进程子进程是否还在活着
* join\(\[timeout\]\)：是否等待子进程执行结束，或等待多少秒
* terminate\(\)：不管任务是否完成，立即终止子进程

**Process创建的实例对象的常用属性：**

* name：当前进程的别名，默认为Process-N，N为从1开始递增的整数
* pid：当前进程的pid（进程号）

我们来实现多进程完成唱歌跳舞吧：

```py
'''net04_sing_dance_multiprocess.py'''
import multiprocessing
import time


def sing():
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1)  # 休息1秒


def dance():
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sing)  # 创建唱歌进程
    p2 = multiprocessing.Process(target=dance)  # 创建跳舞进程
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance
```

我们通过Process分别创建了唱歌子进程p1和跳舞子进程p2，然后启动使用start\(\)了子进程 。从结果中可以看到唱歌和跳舞完全互不影响，各自进行直到结束。

![](/assets/process1.png)

当然有经验的读者会说，这和多线程、协程（后续两章）效果不一样么，答曰：不一样。python的os模块中有关getpid方法可以获取程序的进程号，我们通过在程序中添加os.getpid\(\)来查看我们的程序有哪些进程。在刚开始运行程序时，我们可以在终端\(MAC\)输入`ps aux|grep net04`查看我们的程序在运行时的进程号，然后进行对比确认。完整的代码如下：

```py
'''net04_getpid.py'''
import multiprocessing
import os
import time


def sing():
    print('唱歌进程pid: %d' % os.getpid())
    for i in range(5):
        print('正在唱歌呢 %d' % i)
        time.sleep(1)  # 休息1秒


def dance():
    print('跳舞进程pid: %d' % os.getpid())
    for i in range(5):
        print('正在跳舞呢 %d' % i)
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    print('父进程pid: %d' % os.getpid())
    p1 = multiprocessing.Process(target=sing)  # 创建唱歌进程
    p2 = multiprocessing.Process(target=dance)  # 创建跳舞进程
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance
```

从结果中可以看到，我们的程序运行时共占用了三个进程：19277、19278、19279，和我们预想的一样。由于进程时系统分配资源的基本单元，所以我们的三个进程程序相比单进程程序会占用系统更多的资源去同步完成唱歌和跳舞的任务。

![](/assets/process2.png)



