# 0、介绍

matplotlib是python最著名的绘图库，它提供了一整套和matlab相似的命令API，十分适合交互式进行制图，而且方便作为绘图控件嵌入GUI应用程序中。在Gallery页面\([http://matplotlib.sourceforge.net/gallery.html](http://matplotlib.sourceforge.net/gallery.html%29\) ）中有上百幅缩略图，打开之后都要源程序。若你想绘制某种类型的图，只需要在这个页面中浏览复制粘贴一下，基本都能搞定。

在Linux下比较著名的数据图工具还有gnuplot，但画图质量不好。

而matplotlib的语法、python语言、latex画图质量非常好（可以使用内嵌的latex引擎绘制数学公式）。

# 1、快速入门

若您是新手，请从本节开始，若是老手，则直接跳到下一节进行学习分析。为了快速的获取程序显示出的效果，本节使用ipython notebook\(Jupty\)进行代码演示.

在jupty中执行matplotlib时，为了显示，需要将以下命令写入：

```py
%matplotlib inline
```

使用inline模式可以使jupty中绘制的图表自动关闭。

为了在多个jupty单元格内操作同一幅图表，需要运行以下命令：

```py
%config InlineBackend.close_figures = False
```

## 1-1、使用pyplot模块绘图

matplotlib的pyplot模块提供了类似matlab一样的绘图函数API，方便我们快速绘制二维图表。先看个简单例子。

这个例子总共五个步骤，源代码注释里均有序号，后续例子只在源代码中表示之前未提到的一些步骤，其他不作标注。这里简单说明一下，此程序主要实现了pyplot绘制二维图表的功能，演示了基本步骤：1、导入模块matplotlib.pyplot；2、调用figure\(\)创建一个图表；3、设置关键字参数；4、设置子图属性；5、显示show\(\)（在很多实际应用中不需要显示，可直接将图片存储，后面会有说明。）

```py
import matplotlib.pyplot as plt  # 1、导入模块pylot
import numpy as np  # 需要numpy扩展包里的方法创建x、y数据等，因此导入

x = np.linspace(0, 10, 1000) # x取0到10之间均匀1000个数
y = np.sin(x)
z = np.cos(x**2)
# 2、调用figure()创建一个图表
# figsize参数指定宽和高， 单位为英寸
plt.figure(figsize=(8,4))
# 3、设置关键字参数
# label:给曲线指定标签并显示，其中$表示会调用LaTex来显示数学公式
# color:指定曲线颜色
# linewidth: 指定线宽
# b-- 是直接指定曲线颜色和线型，b为蓝色，--为虚线
plt.plot(x, y, label="$sin(x)$", color="red", linewidth=2)
plt.plot(x, z, "b--", label="$cos(x^2)$")
# 4、设置子图属性
# xlabel、ylabel:设置X、Y轴的标题文字
# title: 设置子图的标题
# xlim、ylim:设置X、Y显示范围
# legend: 显示标签区域
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("First Pyplot")
plt.ylim(-1.2, 1.2)
plt.legend()
# 5、显示窗口
plt.show() # 阻塞程序并显示绘图窗口，直到绘图窗口关闭
```

结果：

![](/assets/first_pyplot.jpg)

刚才提到，在实际应用中，有时候需要直接将图片存储并不显示，一般将第5步修改为plt.savefig\(\)即可，即将当前的Figure对象保存成图像文件，图像格式由图像文件的扩展名决定。

```py
plt.savefig("first_pyplot.png", dpi=120) #存储为png格式，分辨率为120
```

实际应用中除了直接存储外，有时候需要被其他文件对象调用，使用savefig\(\)也可实现，即第一个参数修改为相应的对象。

```py
import io
buf = io.BytesIO() # 创建一个用来保存图像内容的BytesIO对象
plt.savefig(buf, fmt="png") # 将图像以png格式保存到buf中
buf.getvalue()[:20] # 显示图像内容的前20个字节
```

```
b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02@'
```

matplotlib.pyplot模块虽然用法简单，但不适合在交大的应用程序中使用。

```py
import matplotlib.pyplot as plt
```

当前的图表可以使用plt.gcf\(\)获得--------get current figure

当前的子图可以使用plt.gca\(\)获得--------get current Axes

plt.plot\(\)实际上会通过plt.gca\(\)获取当前的Axes对象ax,然后再调用ax.plot\(\)方法实现

真正的绘图。

在ipython中可以输入plt.plot??的命令查看

由于matplotlib实际上是一套面向对象的绘图库，所以可以配置其属性。

## 1-2、 面向对象方式绘图



