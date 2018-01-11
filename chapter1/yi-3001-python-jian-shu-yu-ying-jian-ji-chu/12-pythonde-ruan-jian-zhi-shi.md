# 1.2 python的软件知识

本节分三部分进行说明：python语言自身的软件版本、开发中经常用到的IDE和程序员需要用到的一些小工具基础。对于软件的安装等，本书不介绍，一个程序员应当有获得操作方法的能力。

## 1.2.1 python版本

目前主流的python分为两大版本：python2和python3。python2.0是在2000年发布，当时导入了内存回收机制，构成了目前python语言的框架。python2.4在2004年与比较流行的WEB框架Django一起诞生。python2.7是2010年发布，一直维护到2020年。而python3.0是2008年发布，目前已经更新到3.6.4，明年会出3.7 。python3是少有的打破兼容的语言版本。但是目前python2.7的最新版本已经和python3.4+的版本兼容了很多了，许多代码可以轻松共用。

由于python2发布时，还没有包括unicode等诞生，所以在python3诞生时，鬼叔等本着不庞杂，不重复的原则，重构了python，并将其发布。目前社区基本都已迁移到python3，**建议大家直接使用python3进行学习，**好模块多多哦。所以初学者不建议用很老的资料（python2编写的）取学习。在学习完python基础后，了解了几个大概的两个版本区别，可以尝试分析python2编写的程序。官方为此也出了2to3的转换工具，可以转换部分代码。下文列出两个版本几个常见区别，供大家以后查阅。

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

