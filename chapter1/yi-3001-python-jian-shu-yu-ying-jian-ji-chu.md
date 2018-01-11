本章主要讲述python的一些常识：python的软件配置、硬件需求、以及开发应用场景等。

# 1.1 python简介

python由吉多·范罗苏姆（Guido van Rossum）在1989年创造。社区都称创始人为龟叔。1989年，龟叔在阿姆斯特丹为了打发圣诞节的无趣生活，开发了一个新的脚本解释程序，这便是python。1991年，第一个python编译器诞生，它是用C语言实现的，并能够调用C语言的库文件。因此，其很多语法和C相似。

## 1.1.1 python的定义

对于众多的计算机语言，根据其特点和语法本身侧重点的不同，一般会有不同的分类和叫法。

`拓展：python从一开始就特别在意可拓展新，可以在多个层次上拓展。从高层上，我们可以引入.py文件（python文件的后缀）；从底层上，我们可以引入C语言的库。可以快速的使用.py文件作为拓展模块。当考虑性能时，可以深入底层，写C程序，编译为.so文件引入到python中使用。python就好像使用钢构建房一样，先规定好大的框架，而程序员在此框架下自由拓展。`

`由于计算机性能的提高，硬件不再是大多数应用的瓶颈，所以很多人使用语法规范简单的python。初期龟叔便维护了一个maillist，大家通过邮件进行交流。一般python使用者将修改或拓展后的内容发给龟叔，并由龟叔决定是否将新的特征加入到python或者其标准库中。因此，大家一般称其为“终身的仁慈独裁者”。`

`随着发展便有了python社区，并拥有了自己的newsgroup,网站（`[`http://www.python.org/`](http://www.python.org/)`），及基金。通过社区，开发者们将不同领域的优点带给了python，如：python标准库的正则表达式参考的Perl，lambda、map、filter等函数参考的Lisp。从python2.0开始，开源社区开发模式，加速了python发展。直到今天，python的框架已确立。python语言以对象为核心组织代码，支持多种编程范式，采用动态类型，自动进行内存回收。`

python作为计算机语言一般会被定义为四种语言：1、脚本语言，2、解释性语言，3、高级语言，4、面向对象的语言。

### 1、脚本语言

脚本：script。脚本就像电影的剧本一样，剧本决定了电影中的人和物的发展以及具体事务过程；计算机脚本决定了计算机上电后硬件初始化驱动、操作系统初始化加载以及接下来各种软件程序要做什么事，以及何时做。例如，Windows里的命令行文件或者.bat批处理文件等、linux的shell脚本等通过一个普通文本文件，并添加脚本命令或者代码并保存，就可以在有相关环境的操作系统中运行执行相应的操作了。一般脚本语言经过编译后就可以执行了。

**编译型语言和脚本语言**

**编译型语言：**就是用此语言将程序源代码编译成可执行程序（机器语言），然后就可以运行了。一般均通过编译语言将源代码和相应的库打包链接编译为最终的可执行文件。这种语言一般执行效率高（直接运行可执行程序）、依赖编译器、跨平台性能差些，如C、C++、Delphi等。

```
源代码->编译器编译为可执行程序->运行程序
```

**脚本语言：**脚本语言不需要编译器编译源代码，可以直接在操作系统的命令行中运行，当前环境本身就是此脚本的解释器。

```
源代码->直接运行
```

### 2、解释型语言

相对于脚本语言直接在操作环境中读一行解释一行执行一行，解释型语言一般需要专门的解释器来执行。每个语句也是在执行的时候才翻译为机器语言，依赖解释器，效率较低，但跨平台性能好。如java、python等。

### 3、高级语言

高级语言相对于机器语言，是一种指令集的体系；不需要对硬件知识了解太多；是高度封装了的编程语言；并以人类日常语言为基础、并便于接收的文字\(英语\)来表示，具有较高的程序可读性。如Fortran、C、C++、JAVA、python等。

之所以称为高级语言，是因为刚开始发展的程序语言，如汇编语言，涉及太多物理层面上和硬件上的实现细节，不利于一般人去理解和学习并掌握，属于低级语言。20世纪80年代，东亚地区曾掀起一股常数开发用各自地方语言编写的高级语言，主要是改变BASIC或专用于数据库数据访问的语言，但随着编程人员的英语水平提高，现在有关开发很少。

### 4、面向对象语言

目前主要使用的高级程序语言分两种：面向过程语言和面向对象语言。

**面向过程语言：**在早期的单片机开发中，由于存储极小（几K大小），一般只能实现很少的功能。因此一般均是源码顺序执行（顶多也就是中断）。由于程序量较小，所以不需抽象实际物理参数，即可编写并实现功能调用等。这种一般只有函数调用数据形式的处理程序属于面向过程语言。当需要修改时，一般需要寻找并修改一大堆数据，易于出错，非常不利于系统复杂化。后来随着硬件的发展，在单片机及嵌入式开发中，由于存储不再是瓶颈，大量的功能集成，需要运用面向对象语言来编写以实现各自复杂的实际实例。如C51等。

**面向对象语言：**是指在语言设计时，语言本身的基本元素是以对象的方式设计的，而不同的对象之间的交互则成为整个程序运行的主要表现形式。以万物皆对象的思路将现实中的物体、概念、逻辑的整体等内容实现与语言元素意义对应。由于程序员用此方式设计程序时更直观和理解，更易建华处理逻辑，因此降低了用语言解决实际问题的负责度，提高了处理事情的效率。

Python语言也是基于对象的，属于面向对象的编程语言。

`“面向对象”的解释：现实世界中任何事物都具有自己的属性或能力，比如一种桌子有长宽高、材质、颜色等属性；但它没有生命，没有自己移动的能力。一只狗有年龄、颜色、体重等属性；也有生命，有自己走路、叫唤的能力。`

`那么，在程序中，我们可以模仿现实世界，并对其进行有目的的抽象：将实际事物在我们设计时有用的属性和能力抽象出来并建立一个关联的模型。对现实世界中事物不论属性或能力的，而程序需要的，可以直接在程序中添加；对现实世界中事物具有属性或者能力的，但程序不需要的，在程序中不进行表达。这种抽象出来的模型就叫做对象或类。例如，上文中的桌子可以是一个类对象；若是小明家的桌子则可以是一个属于桌子类的实例对象。`

## 1.1.2 python的特点

### 1、优点

**简单**————Python是⼀种代表简单主义思想的语⾔。阅读⼀个良好的Python程序就感觉像是在读英语⼀样，尽管这个英语的要求⾮常严格！Python的这种伪代码本质是它最⼤的优点之⼀。它使我们能够专注于解决问题⽽不是去搞明⽩语⾔本身。

**易学**————就如同我们即将看到的⼀样，Python极其容易上⼿。前⾯已经提到了，Python有极其简单的语法。

**免费、开源**————Python是FLOSS（⾃由/开放源码软件）之⼀。简单地说，我们可以⾃由地发布这个软件的拷⻉、阅读它的源代码、对它做改动、把它的⼀部分⽤于新的⾃由软件中。FLOSS是基于⼀个团体分享知识的概念。这是为什么Python如此优秀的原因之⼀——它是由⼀群希望看到⼀个更加优秀的Python的⼈创造并经常改进着的。

**⾼层语⾔**————当我们⽤Python语⾔编写程序的时候，你⽆需考虑诸如如何管理你的程序使⽤的内存⼀类的底层细节。

**可移植性**————由于它的开源本质，Python已经被移植在许多平台上（经过改动使它能够⼯作在不同平台上）。如果我们⼩⼼地避免使⽤依赖于系统的特性，那么我们的所有Python程序⽆需修改就可以在下述任何平台上⾯运⾏。这些平台包括Linux、Windows、FreeBSD、Macintosh、Solaris、OS/2、Amiga、AROS、AS/400、BeOS、OS/390、z/OS、PalmOS、QNX、VMS、Psion、AcomRISCOS、VxWorks、PlayStation、SharpZaurus、WindowsCE甚⾄还有PocketPC、Symbian以及Google基于linux开发的Android平台！

**解释性**————⼀个⽤编译性语⾔⽐如C或C++写的程序可以从源⽂件（即C或C++语⾔）转换到⼀个我们的计算机使⽤的语⾔（⼆进制代码，即0和1）。这个过程通过编译器和不同的标记、选项完成。当我们运⾏你的程序的时候，连接/转载器软件把我们的程序从硬盘复制到内存中并且运⾏。⽽Python语⾔写的程序不需要编译成⼆进制代码。我们可以直接从源代码运⾏程序。在计算机内部，Python解释器把源代码转换成称为字节码的中间形式，然后再把它翻译成计算机使⽤的机器语⾔并运⾏。事实上，由于我们不再需要担⼼如何编译程序，如何确保连接转载正确的库等等，所有这⼀切使得使⽤Python更加简单。只需要把我们的Python程序拷⻉到另外⼀台计算机上，它就可以⼯作了，这也使得我们的Python程序更加易于移植。

**⾯向对象**————Python既⽀持⾯向过程的编程也⽀持⾯向对象的编程。在“⾯向过程”的语⾔中，程序是由过程或仅仅是可重⽤代码的函数构建起来的。在“⾯向对象”的语⾔中，程序是由数据和功能组合⽽成的对象构建起来的。与其他主要的语⾔如C++和Java相⽐，Python以⼀种⾮常强⼤⼜简单的⽅式实现⾯向对象编程。

**可扩展性**————如果我们⼀段关键代码运⾏得更快或者希望某些算法不公开，可以把部分程序⽤C或C++编写，然后在我们的Python程序中使⽤它们。

**丰富的库**————Python标准库确实很庞⼤。它可以帮助我们处理各种⼯作，包括正则表达式、⽂档⽣成、单元测试、线程、数据库、⽹⻚浏览器、CGI、FTP、电⼦邮件、XML、XML-RPC、HTML、WAV⽂件、密码系统、GUI（图形⽤户界⾯）、Tk和其他与系统有关的操作。记住，只要安装了Python，所有这些功能都是可⽤的。这被称作Python的“功能⻬全”理念。除了标准库以外，还有许多其他⾼质量的库，如wxPython、Twisted和Python图像库等等。

**规范的代码**————**Python采⽤强制缩进（语法：代码缩进代表了代码的逻辑关系，而不仅仅是美观）的⽅式使得代码具有极佳的可读性。**

众多的优点使其被称为**胶水语言。**

### 2、缺点

① 运⾏速度——有速度要求的话，⽤C++改写关键部分吧。② 国内市场较⼩（国内以python来做主要开发的，⽬前只有⼀些web2.0公司）。但时间推移，⽬前很多国内软件公司，尤其是游戏公司，也开始规模使⽤它。③ 中⽂资料匮乏（好的python中⽂资料屈指可数）。托社区的福，有⼏本优秀的教材已经被翻译了，但⼊⻔级教材多，⾼级内容还是只能看英语版。④ 构架选择太多（没有像C\#这样的官⽅.net构架，也没有像ruby由于历史较短，构架开发的相对集中。RubyonRails构架开发中⼩型web程序天下⽆敌）。不过这也从另⼀个侧⾯说明，python⽐较优秀，吸引的⼈才多，项⽬也多。

## 1.1.3 python的应用

### 1、python不能干什么

python不能像汇编语言那样直接去操作底层的硬件，尤其是那些汇编语言可以直接操作的寄存器级别的硬件。但是C语言可以。

### 2、python适合干什么

#### python的主流应用领域：

目前主要应用于web应用开发、操作系统管理和服务器运维的自动化脚本、科学计算、桌面软件、服务器网络软件、游戏以及构思实现和产品早期原型迭代等。

##### ①、网络和以太网开发

**网络框架**：Django、TurboGears、Pylons、异步网络编程框架Twisted、flask、Webpy、Bottle  
**内容管理系统**：Plone、Mezzanine  
**应用服务器**：Zope  
**python网站**：社交分享类：Reddit；文件分享类：Dropbox；图书唱片电影等资料数据库网站：_**豆瓣**_；MediaWiki的机器人程序：Python Wikipedia Robot Framework；Wiki程序：MoinMoinWiki；图片社交分享网站：Pinterest；幻灯片存储显示分享网站：SlidShare；其他各种网站：_**知乎、果壳网、美团、快盘、扇贝网、糗事百科**_、Wopus问答等。  
**其他**：编写CGI脚本；支持HTML和XML的处理；邮件处理：Mailman；RSS处理；支持很多网络协议。

##### ②、数据库访问

**自定义和ODBC数据库接口**：MySQL、Oracle、MS SQL Server、PostgreSQL、SybODBC等。  
**标准数据库接口**：  
**对象数据库接口**：ZODB、Durus

##### ③、图形桌面

内置Tk的GUI库、wxWidgets、GTK+、通过pygt或pyside支持QT、通过win32支持MFC、Delphi、wxPython、AnyGui等。

##### ④、科学计算

Bioinformatics、Physics、NumPy、SciPy、Matplotlib、Pandas等。

##### ⑤、教育教学

Education Special Interest Group、pyBiblio、Software Carpentry Course等

##### ⑥、软件开发

**编译控制**：SCons  
**自动化连续编译和测试**： Buildbot、Apache Gump  
**缺陷追踪和项目管理**：Roundup、Trac

##### ⑦、游戏和3D图形处理

**游戏框架**：PyGame、PyKytra等  
**3D渲染库**：FreeCAD、Minilight  
**3D软件**：以C与Python开发的开源3D绘图软件：Blender、Cinema 4D  
python游戏库：PySoy、Pyglet、Python-Ogre、Panda3D、Blender3D、GGZ Gaming Zone等  
**python游戏**：EVE、SolarWolf、Mount&Blade等  
**python在线游戏服务器**：Evennia、GrailMUD等。

##### ⑧、构思实现、产品早期原型和迭代

YouTube、Google、Yahoo!、NASA都在内部⼤量地使⽤Python

### 3、我们能用python干什么

相比于其他语言，我们个人一般可以利用python进行小型的3D效果实现、网络下载器的实现；还有网络爬虫抓取数据、数据计算和数据分析等。

# 1.2 python的软件知识

本节分三部分进行说明：python语言自身的软件版本、开发中经常用到的IDE和程序员需要用到的一些小工具基础。对于软件的安装等，本书不介绍，一个程序员应当有获得操作方法的能力。

## 1.2.1 python版本

目前主流的python分为两大版本：python2和python3。python2.0是在2000年发布，当时导入了内存回收机制，构成了目前python语言的框架。python2.4在2004年与比较流行的WEB框架Django一起诞生。python2.7是2010年发布，一直维护到2020年。而python3.0是2008年发布，目前已经更新到3.6.4，明年会出3.7 。python3是少有的打破兼容的语言版本。但是目前python2.7的最新版本已经和python3.4+的版本兼容了很多了，许多代码可以轻松共用。

由于python2发布时，还没有包括unicode等诞生，所以在python3诞生时，鬼叔等本着不庞杂，不重复的原则，重构了python，并将其发布。目前社区基本都已迁移到python3，建议大家直接使用python3进行学习，好模块多多哦。所以初学者不建议用很老的资料（python2编写的）取学习。在学习完python基础后，了解了几个大概的两个版本区别，可以尝试分析python2编写的程序。官方为此也出了2to3的转换工具，可以转换部分代码。下文列出两个版本几个常见区别，供大家以后查阅。

**python2和python3的主要区别：**

_——print语法：python2不带括号，python3带括号  
——python2中的long型数据切换到python3的int型数据  
——python3不支持cmp\(\)_  
——python2分input和raw_input，python3只有input  
——python2中bytes和str可以混用，无bytes一说，python3不可以，有unicode，分bytes和bytearrays。  
——python2 整除结果为整数，python3为浮点数  
——python2有xrange和range，python3为range  
——python2触发异常的语句可以带括号也可以不带，python3统一不带括号  
——python2异常处理可以用逗号起别名，python3改为as  
——python2可以使用next\(\)和.next\(\)，python3只有next\(\)  
——python2在列表解析中赋值的全局参数不会释放，python3会释放恢复其原先的值  
——python2中无序类型可以比较，python3中不可以  
——python2中list等在python3 为可迭代对象，存储为视图类型，更节省内存  
更多详细的可以查看此链接    _[http://www.jb51.net/article/57956.htm](http://www.jb51.net/article/57956.htm)

## 1.2.2 学习常用辅助软件

本节主要列举辅助我们学习和查询资料的工具，它们对我们平时学习有非常大的帮助，**大基础才会成就大深度**。我们只需看黑色字体就可以了。python语言被称为胶水语言，连接着众多模块，因此少不了即时**查询文档的API软件**。要向学好一门语言，**英语翻译**肯定要接触。学习免不了整理思维，**思维导图**也是必须的。常用的**代码管理软件**对我们也非常有帮助。在后期web开发、数据爬取时，需要分析网页内容，好的**浏览器\(chrome和火狐\)**才会事半功倍。

### 常用API查询软件

**mac：Dash**  [https://kapeli.com/dash](https://kapeli.com/dash)

Dash是一个**API文档浏览器**（API Documentation Browser），以及代码片段管理工具（Code Snippet Manager）。你没看错，它就只有这两个功能，但确实是程序员（至少对笔者\(非程序员\)来说）最为关心的特性。左侧边栏是各种编程语言以及框架（取决于我们下载安装了多少文档集合）的导航大纲，点击某个节点，右边的内容区域就是文档的详细信息啦，非常直观。也可以在左上方的搜索框内通过输入关键字，查找相关的API文档，非常类似全文检索的实现方式，Dash的响应速度非常快！关键是可以同时查询不同的语言、框架内容，实在是太方便了。实际上它还可以做代码管理，这里不再介绍。![](/assets/Dash.png)

**Windows & linux： Zeal**       [https://zealdocs.org/](https://zealdocs.org/)

Zeal 是一个简单的**离线 API 文档浏览器**，仿照Dash写成，能在 Linux 和 Windows 上使用。在你的工作空间的任何地方中，使用`Alt + 空格`（也可以自定义）快捷键去进行快速的文档搜索。一次搜索多个文档集，不需要网络连接。Zeal 是开源的！遵循 GPL 版权协议，所有能用在 Dash 上的文档也可以用在 Zeal 中。![](/assets/Zeal.png)

### 翻译软件

**mac：词典**

![](/assets/maccidian.png)

**windows：谷歌翻译**

![](/assets/googe_transplate.png)

### 思维导图

**XMind   **[http://www.xmindchina.net/](http://www.xmindchina.net/)

XMind中的思维导图结构包含一个中心根主题，和围绕中心主题辐射的众多主要分支。除了思维导图结构，XMind还提供组织结构图、树状图、逻辑图等，这些图表在各种情况下都扮演着很重要的角色。比如，组织结构图可以清楚地显示公司/部门/团队的结构，逻辑图在分类原因的时候非常有用，更重要的是，**所有这些图表都可以在一个导图中使用**！每一个分支，甚至每一个主题，都能拥有最合适的结构。可用性非常之大。![](/assets/xmind.png)

**MindNote**     [https://mindnode.com/](https://mindnode.com/)

思考人生必须要有思维导图软件配合。**MindNode**是 Mac 上思维导图软件，免费版功能界面极简，支持全键盘操作，界面响应迅猛，满足基础要求。**非常适合用来复习知识。**![](/assets/mindnote.png)

### git

**github    ** [https://github.com/](https://github.com/)

gitHub是一个**面向开源及私有软件项目的托管平台**，因为只支持git 作为唯一的版本库格式进行托管，故名gitHub。gitHub于2008年4月10日正式上线，除了git代码仓库托管及基本的 Web管理界面以外，还提供了订阅、讨论组、文本渲染、在线文件编辑器、协作图谱（报表）、代码片段分享（Gist）等功能。目前，其注册用户已经超过350万，托管版本数量也是非常之多，其中不乏知名开源项目Ruby on Rails、jQuery、python等。GitHub for Windows 是一个 Metro 风格应用程序，集成了自包含版本的 Git，bash 命令行 shell，PowerShell 的 posh-git 扩展。GitHub 为 Windows 用户提供了一个基本的图形前端去处理大部分常用版本控制任务，可以创建版本库，向本地版本库递交补丁，在本地和远程版本库之间同步。mac桌面版GitHub Desktop如下所示。![](/assets/github.png)

**gitbook       **[https://www.gitbook.com](https://www.gitbook.com)

GitBook 是一个基于 Node.js 的命令行工具，可使用Github/Git 和Markdown来**制作精美的电子书**，GitBook 并非关于Git的教程。GitBook支持输出多种文档格式：  
·静态站点：GitBook默认输出该种格式，生成的静态站点可直接托管搭载Github Pages服务上；  
·PDF：需要安装gitbook-pdf依赖；  
·eBook：需要安装ebook-convert；  
· 单HTML网页：支持将内容输出为单页的HTML，不过一般用在将电子书格式转换为PDF或eBook的中间过程；  
·JSON：一般用于电子书的调试或元数据提取。  
使用GitBook制作电子书，必备两个文件：README.md和SUMMARY.md。  
gitbook-editor客户端可以实现离线编辑书籍、联网同步和发布了，而且也可以导出pdf、mobi格式。

![](/assets/gitbook.png)

## 1.2.3 python常用开发IDE

Python 的学习过程少不了 IDE 或者代码编辑器，或者集成的开发编辑器（IDE）。这些Python 开发工具帮助开发者加快使用 Python 开发的速度，提高效率。高效的代码编辑器或者 IDE 应该会提供插件，工具等能帮助开发者高效开发的特性.比如Vim，Eclipse with PyDev，Sublime Text，PyCharm，PyScripter等。本文只介绍我们经常用到且肯定会用到（项目开发、数据分析、脚本编辑）的软件。

**PyCharm**     [http://www.jetbrains.com/pycharm/](http://www.jetbrains.com/pycharm/)

PyCharm是一种Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。此外，该IDE提供了一些高级功能，以用于支持Django框架下的专业Web开发。同时支持Google App Engine，更酷的是，PyCharm支持IronPython。**一般大型项目开发采用此软件。**

![](/assets/pycharm.png)

**Spyder **   [https://pypi.python.org/pypi/spyder](https://pypi.python.org/pypi/spyder)

Spyder是Python\(x,y\)的作者为它开发的一个简单的集成开发环境。和其他的Python开发环境相比，它最大的优点就是**模仿MATLAB的“工作空间”的功能，可以很方便地观察和修改数组的值。**Spyder的界面由许多窗格构成，用户可以根据自己的喜好调整它们的位置和大小。当多个窗格出现在一个区域时，将使用标签页的形式显示。例如在图1中，可以看到“Editor”、“Object inspector”、“Variable explorer”、“File explorer”、“Console”、“History log”以及两个显示图像的窗格。在View菜单中可以设置是否显示这些窗格。

![](/assets/spyder.png)

**ipython **     [http://ipython.org/](http://ipython.org/)

IPython 是一个 python 的交互式 shell，**比默认的python shell好用得多，支持变量自动补全，自动缩进**，支持 bash shell 命令，内置了许多很有用的功能和函数。IPython 是基于BSD 开源的。IPython 为交互式计算提供了一个丰富的架构，包含：强大的交互式 shell Jupyter 内核交互式的数据可视化工具灵活、可嵌入的解释器易于使用，高性能的并行计算工具。**安装必选项。**

![](/assets/ipython.png)

**jupty notebook**      [http://jupyter.org/](http://jupyter.org/)

Jupyter Notebook 一个交互式笔记本，支持运行 40 多种编程语言。本质是一个 Web应用程序，便于**创建和共享文学化程序文档**，支持实时代码，数学方程，可视化和 markdown。 用途包括：**数据清理和转换，数值模拟，统计建模，机器学习等等**。与 IPython终端 共享同一个内核。

![](/assets/jupyternotebook.png)

**anaconda\(必选项\)      **[https://www.anaconda.com/download/](https://www.anaconda.com/download/)

原生的python为了实现更丰富的科学计算功能，还需要安装大量的第三方扩展库，非常繁琐。因此便出现了Anaconde。这是一个常用的科学计算发型版。它包含了**众多流行的科学、数学、工程和数据分析的python包**；完全开源和免费；全平台支持，python版本自由切换。装了它，**几乎做数据分析、机器学习，不再需要装太多的第三方扩展包了。上文中的ipython、jupyter、ipython等均会被默认安装。**

![](/assets/anaconda.png)

**Sublime Text     **[https://www.sublimetext.com/](https://www.sublimetext.com/)

Sublime Text 是一个**代码编辑器**，也是HTML和散文先进的**文本编辑器**。Sublime Text是由程序员Jon Skinner于2008年1月份所开发出来，它最初被设计为一个具有丰富扩展功能的Vim。Sublime Text具有漂亮的用户界面和强大的功能，例如代码缩略图，Python的插件，代码段等。还可自定义键绑定，菜单和工具栏。Sublime Text 的主要功能包括：拼写检查，书签，完整的 Python API ， Goto 功能，即时项目切换，多选择，多窗口等等。Sublime Text 是一个跨平台的编辑器，同时支持Windows、Linux、Mac OS X等操作系统。Sublime Text 支持多种编程语言的语法高亮、拥有优秀的代码自动完成功能，还拥有代码片段（Snippet）的功能，可以将常用的代码片段保存起来，在需要时随时调用。支持 VIM 模式，可以使用Vim模式下的多数命令。支持宏，简单地说就是把操作录制下来或者自己编写命令，然后播放刚才录制的操作或者命令。![](/assets/sublimetext.png)

# 1.3 python的硬件知识



