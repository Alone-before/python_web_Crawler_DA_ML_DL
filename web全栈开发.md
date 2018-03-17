# 第五部分 web全栈开发

本部分主要内容由web服务器部署介绍、web应用框架介绍、WSGI协议介绍、Django基础、基于Django的项目开发实例——Nginx配置和uWSGI部署、RESTful接口等。

本部分所讲述的全栈开发内容并不包含基础的网络编程（见第二部分）、数据库部分（见第三部分）前端HTML和Javascript（见第四部分）等。

笔者认为在开始web全栈开发之前，应当了解web全栈的主要组成部分，笔者推荐海鸣的gitbook书籍《[web全栈》](https://getfullstack.com/)，它主要讲述了web全栈需要什么，读者应当花费20分钟大体浏览下这本100页的书籍。

之后呢，进行web全栈开发之前应当了解web服务器部署的大体介绍和web应用框架介绍，这是通往架构师的必由之路。但是在一开始学习时应当对相关的部署有个全局了解。笔者参照一些文献总结并转载了一些网络资源，对着两个介绍进行了初步介绍。

然后介绍了python中的WSGI协议，并基于第二部分的静态web服务器来实现简单的符合WSGI协议服务器。

此时我们开始学习python中功能最全面的Django框架——MTV与ORM。

最后我们学习一些其他的框架和web开发知识。



**在学习之前，若读者直接从第五部分开始，建议按照以下思路进行python web全栈开发学习：**

1.python入门

推荐老齐《从零开始学python》，《python简明教程》，这两本书很适合小白入门（像我一样长期徘徊在编程门外的人）

2.python进阶

推荐《python学习手册》，python学习手册的前半部分与在入门教程中的基础部分相重复，后面部分对python的介绍更细致，比如面向对象的这部分对于小白理解相对容易。

还有一本《python cookbook》，这本是在讲述python的经典用法，目前读过函数，装饰器以及网络编程这三部分，在不断的敲玩具代码的过程中，会发现书中讲的例子不断会出现。

3.学习web开发，自然要涉及到基于python的web 框架。

1）flask

flask如同官方所描述的那样，是一个web微框架，用几行代码就可以实现一个在hello world，现在的个人感觉是flask确实适合新手入门。基于这个原则，

推荐《flask web 开发》这本书，这本书简直是良心，讲的很细，并且在github上有源码，可以很容易跟着作者的步骤去学习，不懂得的地方可以去问谷歌或者qq群。

推荐的第二本是《building web applications with flask》这本书是对flask框架的细化，深入讲解flask的模板，restful等等，虽然是英文，但是叶能顺利阅读下去

推荐的第三本是《flask Framework cookbook》，这三本书是一个不段进阶的部分。

2）django

django是大而全，开箱即用，在flask了解的差不多的时候去了解，毕竟生成环境用的django相对多一点。

django学习可以看得书：（1）tango with django只有一个应用去学习，对于新手友好，可以比对github源码

（2）django by example 注重实战，有几个实例，blog， shop etc,涉及django基础，redis,celery,solr,ajax,很全面，也是web开发常用的技术

4.在学习框架的过程中，会不断体会到前端的知识也是要补回来，可以w3c school看一下。

5.数据库，在python中内置了sqlite， sql命令有相同之处，路线是sqlite， mysql， mongodb，有个逐渐过度的过程。

6.了解http的具体工作流程，这点目前还是有点模糊

7.工具集：sublime\(需要配置，主要用于python编程，神器谁用谁知道\)， vim， firebug, firefox, linux,github（代码大宝库，各种代码）

8.学习的过程觉得几点很重要

1）做好笔记，同样的问题会遇到第二次，有个笔记容易复查

2）善用谷歌，善用qq与论坛，你现在遇到的问题，大多数前人都遇到过，stackflow是个好地方

3）迷茫的时候还是坚持看，因为毕竟是小白，不懂的太多，你总要把他弄懂

4）有时间了可以把算法与数据结构补起来。



