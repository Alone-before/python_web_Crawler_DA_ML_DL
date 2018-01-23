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

既然我们实现了多进程完成唱歌跳舞，那我们更进一步的实现告诉子进程让谁唱歌让谁跳舞吧，没错，我们就是导演，我们说了算。通过在Process对象创建时通过对args或者kwargs进行赋值来传递参数就可以实现。

```py
singer = 'Jam'
sing_name = '不露声色'
p1 = multiprocessing.Process(target=sing, args=(singer, sing_name))  # 创建唱歌进程,告诉子进程是Jam唱不露声色
p2 = multiprocessing.Process(target=dance,kwargs={'dancer':'杰克逊'})  # 创建跳舞进程，告诉子进程是杰克逊来唱歌啦
```

实例完整代码如下:

```py
'''net04_sing_dance_variable.py'''
import multiprocessing
import time


def sing(name, sing_name):
    for i in range(5):
        print(name, '正在唱歌%s呢 %d' % (sing_name, i))
        time.sleep(1)  # 休息1秒


def dance(**kwargs):
    dancer = kwargs['dancer']
    for i in range(5):
        print('%s正在伴舞呢 %d' % (dancer,i))
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    singer = 'Jam'
    sing_name = '不露声色'
    p1 = multiprocessing.Process(target=sing, args=(singer, sing_name))  # 创建唱歌进程,告诉子进程是Jam唱不露声色
    p2 = multiprocessing.Process(target=dance,kwargs={'dancer':'杰克逊'})  # 创建跳舞进程，告诉子进程是杰克逊来唱歌啦
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance
```

从运行结果中我们可以很清晰的看到Jam唱不露声色的时候杰克逊在为她伴舞——so crazy。

![](/assets/process3.png)

## 5.3 进程间不共享全局变量

上一章我们知道线程间会共享全局变量，本节我们来想一下，进程间呢？当然不会啦，假如我们的电脑上装有QQ音乐和网易云音乐，在网易云音乐收藏的歌单不会自动到QQ音乐的。我们一起看个实例吧。定义一个全局变量global\_num=0，然后在唱歌和跳舞两个代码块中添加global\_num+1操作。我们会发现，父进程、sing子进程和dance子进程之间global\_num并无半点关系，即进程间不共享全局变量。

```py
'''net04_global_variables.py'''
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
```

![](/assets/process4.png)

## 5.4 进程间通信

上一节我们了解到进程间不共享全局变量，但是试想一下，我们电脑上登录了两个QQ并需要互传消息或者杰克逊作为伴舞者打算给Jam递花，怎么办呢？这就要涉及进程间通信。在多进程程序中，有众多的进程间通信方式，我们今天通过python中multiprocessing模块中的Queue来实现进程间的通信。它的基本语法如下：

初始化Queue\(\)对象时（例如：q=Queue\(\)），若括号中没有指定最大可接收的消息数量，或数量为负值，那么就代表可接受的消息数量没有上限（直到内存的尽头）；

* Queue.qsize\(\)：返回当前队列包含的消息数量；
* Queue.empty\(\)：如果队列为空，返回True，反之False ；
* Queue.full\(\)：如果队列满了，返回True,反之False；
* Queue.get\(\[block\[, timeout\]\]\)：获取队列中的一条消息，然后将其从列队中移除，block默认值为True；

1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果为空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为止，如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛出"Queue.Empty"异常；  
2）如果block值为False，消息列队如果为空，则会立刻抛出"Queue.Empty"异常；

* Queue.get\_nowait\(\)：相当Queue.get\(False\)；
* Queue.put\(item,\[block\[, timeout\]\]\)：将item消息写入队列，block默认值为True；

1）如果block使用默认值，且没有设置timeout（单位秒），消息列队如果已经没有空间可写入，此时程序将被阻塞（停在写入状态），直到从消息列队腾出空间为止，如果设置了timeout，则会等待timeout秒，若还没空间，则抛出"Queue.Full"异常；  
2）如果block值为False，消息列队如果没有空间可写入，则会立刻抛出"Queue.Full"异常；

* Queue.put\_nowait\(item\)：相当Queue.put\(item, False\)。

我们来看一下下面这个例子：

```py
'''net04_queue_sample.py'''
from multiprocessing import Queue

q = Queue(3)  # 初始化一个Queue对象，最多可接收三条put消息
q.put("消息1")
q.put("消息2")
print(q.full())  # False
q.put("消息3")
print(q.full())  # True

# 因为消息列队已满,所以下面的try都会抛出异常，第一个try会等待2秒后再抛出异常，第二个Try会立刻抛出异常
try:
    q.put("消息4", True, 2)
except:
    print("消息列队已满，现有消息数量:%s" % q.qsize()) # mac os不支持qsize
# Note that this may raise NotImplementedError on Unix platforms like Mac OS X where sem_getvalue() is not implemented.

try:
    q.put_nowait("消息4")
except:
    print("消息列队已满，现有消息数量:%s" % q.qsize())

# 推荐的方式，先判断消息列队是否已满，再写入
if not q.full():
    q.put_nowait("消息4")

# 读取消息时，先判断消息列队是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
```

运行结果与语法中定义的一样，put为写入，get为读出；full为判断是否写满等。

```
False
True
消息列队已满，现有消息数量:3
消息列队已满，现有消息数量:3
消息1
消息2
消息3
```

接下来我们就通过multiprocessing模块中的Queue来实现唱歌跳舞时杰克逊为Jam递花这一构想。具体代码如下：

```py
'''net04_sing_dance_queue.py'''
import multiprocessing
import time


def sing(name, sing_name):
    for i in range(5):
        print(name, '正在唱歌%s呢 %d' % (sing_name, i))
        time.sleep(1)  # 休息1秒
    while True:
        if not q.empty():
            value = q.get() # 从队列中读取数据
            print('Jam收到了', value)
        else:
            break


def dance(**kwargs):
    dancer = kwargs['dancer']
    q.put('花') # 向队列中写入花数据
    print('杰克逊向Jam递了一朵花')
    for i in range(5):
        print('%s正在伴舞呢 %d' % (dancer, i))
        time.sleep(1)  # 休息1秒


if __name__ == '__main__':
    singer = 'Jam'
    sing_name = '不露声色'
    q = multiprocessing.Queue() # 创建队列
    p1 = multiprocessing.Process(target=sing, args=(singer, sing_name))  # 创建唱歌进程
    p2 = multiprocessing.Process(target=dance, kwargs={'dancer': '杰克逊'})  # 创建跳舞进程
    p1.start()  # 开始运行进程sing
    p2.start()  # 开始运行进程dance
```

在这个构想的代码中，我们首先创建了一个消息队列Queue的实例对象q，然后在sing代码块中添加从队列中读取数据的语句q.get\(\)代表收取礼物、在dance代码块中添加向队列中写入数据的语句q.put\(‘花’\)代表送出了花。这样便实现了舞者和歌手两个进程之间的通信。从代码执行的结果来看，确实如此。

## ![](/assets/process6.png)

## 5.5 进程池Pool

在之前的进程创建过程中我们通过multiprocessing中的Process来生成了唱歌和跳舞进程，但如果我们这次演唱会请的是少女时代组合呢？那可是有好多人呢，一个一个创建太累了，有没有批量创建的方法呢？答曰：有。我们可以使用进程池的概念来批量创建进程，即multiprocessing模块中的Pool。

**multiprocessing.Pool常用的函数介绍：**

* apply\_async\(func\[, args\[, kwds\]\]\) ：使用非阻塞方式调用func（并行执行，堵塞方式必须等待上一个进程退出才能执行下一个进程），args为传递给func的参数列表，kwds为传递给func的关键字参数列表；
* close\(\)：关闭Pool，使其不再接受新的任务；
* terminate\(\)：不管任务是否完成，立即终止；
* join\(\)：主进程阻塞，等待子进程的退出， 必须在close或terminate之后使用；

了解了基本语法，我们就来批量创建几个歌手进程吧:  
首先我们创建一个最大只有3个进程的进程池：

```
processes = multiprocessing.Pool(3)
```

其次我们用进程池中的apply\_async来创建五个歌手进程。

```py
'''net04_process_pool.py'''
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
```

由于我们创建的进程池最大只能容纳3个进程，所以本实例中的4号歌手和5号歌手进程需要等到之前几位歌手进程中的某一个执行完毕方可创建。具体见结果。

![](/assets/proceing1.png)

**注意：如果要使用Pool进程池创建进程，就需要使用multiprocessing.Manager\(\)中的Queue\(\)，而不是multiprocessing.Queue\(\)。**

## 5.6 进程与线程对比

### 功能 {#功能}

* 进程，能够完成多任务，比如 在一台电脑上能够同时运行多个QQ
* 线程，能够完成多任务，比如 一个QQ中的多个聊天窗口

### 定义的不同 {#定义的不同}

* **进程是系统进行资源分配和调度的一个独立单位**.

* **线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.**线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源\(如程序计数器,一组寄存器和栈\),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源.

### 区别 {#区别}

* 一个程序至少有一个进程,一个进程至少有一个线程.
* 线程的划分尺度小于进程\(资源比进程少\)，使得多线程程序的并发性高。
* 进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率
* 线线程不能够独立执行，必须依存在进程中

### 优缺点 {#优缺点}

线程和进程在使用上各有优缺点：线程执行开销小，但不利于资源的管理和保护；而进程正相反。





