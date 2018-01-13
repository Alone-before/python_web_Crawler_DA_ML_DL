# 3.4 MySQL高级了解

## 3.4.1 视图

#### 什么是视图

通俗的讲，视图就是一条SELECT语句执行后返回的结果集。所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上。

#### 视图的特性

视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；可以跟基本表一样，进行增删改查操作\(ps:增删改操作有条件限制\)。

#### 视图的作用

方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性；更加安全，数据库授权命令不能限定到特定行和特定列，但是通过合理创建视图，可以把权限限定到行列级别。

#### 使用场合

权限控制的时候，不希望用户访问表中某些含敏感信息的列，比如price 、salary...；关键信息来源于多个复杂关联表，可以创建视图提取我们需要的信息，简化操作。

#### 视图实例1-创建视图及查询数据操作

`注：本章数据库操作演示数据，使用3.3章创建的jing_dong数据库。`

想象一下，当我们需要查询商品 x240 超极本 的商品id、商品名称、商品种类名称、品牌名称的相关数据时，怎么办？一般我们会以下面的SQL语句查询。

```
select goods.id, goods.name, goods_cates.name, goods_brands.name
from goods
    left join goods_cates on (goods.cate_id = goods_cates.id)
    left join goods_brands on (goods.brand_id = goods_brands.id)
where
    goods.name = "x240 超极本";
```

![](/assets/mysql_view1.png)

从结果中可以看到，我们通过三张表的连接查到了x240 超极本的所有信息。但是假如有10张表来记录所有信息并且我们一段工作时间中需要频繁查询呢？那这种语句太繁琐太容易出错了。**此时，视图便可以帮我们解一时之忧。**

首先我们创建一张视图：

```
-- 创建视图语句
-- create view 视图名称 as select语句;
-- 一般建议之家以v_开头赋值视图名，这样方便查阅。
create view v_good_info as select
    goods.id, goods.name, goods_cates.name as catename, goods_brands.name as brandname
    from goods
    left join goods_cates on (goods.cate_id = goods_cates.id)
    left join goods_brands on (goods.brand_id = goods_brands.id);
```

![](/assets/mysql_view.png)

通过show tables;语句查看数据库中的表，可以看到数据库里多了一张v\_good\_info表，这便是我们刚才创建的视图，**它仅仅是之前三张表goods、goods\_cates、goods\_brands的引用，不占用存储空间。**

接下来我们来看看其表内内容，可以看到，所有在库商品的相关信息都放置在这张表中，可以方便我们查询。

```
select * from v_good_info;
```

![](/assets/mysql_view3.png)

我们通过普通的查询语句来查询“x420 超极本”,可以看到结果和之前完全一样。**这就是视图的用武之地。**

```
select * from v_good_info where name = "x240 超极本";
```

![](/assets/mysql_view4.png)

#### 视图实例2-增删改数据操作

大家可以看到我们之前在创建并数据库增加数据时，把“x240 超极本”中的“级”字错写为了“极”，那么我们来尝试通过update来更新修改视图实例1中的此数据。

```
update v_good_info set name="x240 超级本" where id = 5;
```

![](/assets/mysql_view5.png)

好尴尬，系统报错了。这是为什么呢？因为不能在一张由多张关联表连接而成的视图上做同时修改两张表的操作。

我们来分析一下，实际上视图是代替了一块语句，如果我们把之前创建v\_good\_info视图的语句嵌套进去分析的话，会发现，其实这里面有很多name和id，id=5的行不唯一且视图中的行不与我们要修改的goods.name所在表goods的行一一对应，所以不能更新。

![](/assets/mysql_view6.png)那么哪些修改操作可以在视图中进行呢？  
官方文档中这样解释：  
for a view to be updatable, there must be a one to one relationship between the rows in the view and the rows in the underlying table.为了使视图可以更新，视图中的行与基础表中的行之间必须有一对一的关系。

所以在视图进行修改操作时遇到此问题，请注意通过此方向来分析\(如果需要深入了解，建议查看官方文档中的第23.5.3节 Updatable and Insertable Views\)。接下来我们创建一个简单的视图，将goods表中的id，name，price提取作为一个视图v\_good我们修改”x240 超极本“为 ”x240 超级本“了。

```
-- 创建视图v_good
create view v_good as select
    goods.id, goods.name, goods.price
    from goods;
-- 更新数据
update v_good set name="x240 超级本" where id = 5;
-- 查看数据
select * from v_good_info where id = 5;
```

![](/assets/mysql_view8.png)

为了演示操作这一一定时期内的工作，我们创建了两个视图来进行方便的操作。现在工作完成了，我们可以删除它了。

```
drop view v_good_info;
drop view v_good;
```

## 3.4.2 事务

#### 为什么要有事务？

我们先举个例子：

A用户和B用户是银行的储户，现在A要给B转账500元，那么需要做以下几件事：  
检查A的账户余额&gt;500元；  
A 账户中扣除500元;  
B 账户中增加500元;  
正常的流程走下来，A账户扣了500，B账户加了500，皆大欢喜。  
那如果A账户扣了钱之后，系统出故障了呢？A白白损失了500，而B也没有收到本该属于他的500。  
以上的案例中，隐藏着一个前提条件：A扣钱和B加钱，要么同时成功，要么同时失败。事务的需求就在此。

再举一个例子：

在人员管理系统中，作为管理员删除一个人员，即需要删除人员的基本资料，也要删除和该人员相关的信息，如信箱，文章等等，这样，这些数据库操作语句就构成一个事务！

**事务广泛的运用于订单系统、银行系统等多种场景。**

事务的需求就在于此.

#### 什么是事务？

**所谓事务,它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的工作单位。**

`在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。`

`事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。`

`事务用来管理 insert,update,delete 语句`

一般来说，**事务是必须满足4个条件（ACID）： Atomicity（原子性）、Consistency（稳定性）、Isolation（隔离性）、Durability（可靠性）。**

1、**事务的原子性**：一组事务，要么成功；要么撤回。  
2、**稳定性 **：有非法数据（外键约束之类），事务撤回。  
3、**隔离性**：事务独立运行。一个事务处理后的结果，影响了其他事务，那么其他事务会撤回。事务的100%隔离，需要牺牲速度。  
4、**可靠性**：软、硬件崩溃后，InnoDB数据表驱动会利用日志文件重构修改。可靠性和高速度不可兼得， innodb\_flush\_log\_at\_trx\_commit 选项 决定什么时候把事务保存到日志里。

**在 MySQL 命令行的默认设置下，事务都是自动提交的，即执行 SQL 语句后就会马上执行 COMMIT 操作。因此要显式地开启一个事务务须使用命令 BEGIN 或 START TRANSACTION，或者执行命令 SET AUTOCOMMIT=0，用来禁止使用当前会话的自动提交。**

#### 事务控制语句：

BEGIN或START TRANSACTION；显式地开启一个事务；  
COMMIT；也可以使用COMMIT WORK，不过二者是等价的。COMMIT会提交事务，并使已对数据库进行的所有修改称为永久性的；ROLLBACK；有可以使用ROLLBACK WORK，不过二者是等价的。回滚会结束用户的事务，并撤销正在进行的所有未提交的修改；SAVEPOINT identifier；SAVEPOINT允许在事务中创建一个保存点，一个事务中可以有多个SAVEPOINT；  
RELEASE SAVEPOINT identifier；删除一个事务的保存点，当没有指定的保存点时，执行该语句会抛出一个异常；  
ROLLBACK TO identifier；把事务回滚到标记点；  
SET TRANSACTION；用来设置事务的隔离级别。InnoDB存储引擎提供事务的隔离级别有READ UNCOMMITTED、READ COMMITTED、REPEATABLE READ和SERIALIZABLE。

#### MYSQL 事务处理主要有两种方法：

1、用 BEGIN, ROLLBACK, COMMIT来实现

BEGIN 开始一个事务

ROLLBACK 事务回滚

COMMIT 事务确认

2、直接用 SET 来改变 MySQL 的自动提交模式:

SET AUTOCOMMIT=0 禁止自动提交

SET AUTOCOMMIT=1 开启自动提交

## 3.4.4 函数

## 3.4.4 索引

#### 什么是索引？

**索引是一种特殊的文件\(InnoDB数据表上的索引是表空间的一个组成部分\)，它们包含着对数据表里所有记录的引用指针。**更通俗的说，数据库索引好比是一本书前面的目录，能加快数据库的查询速度。

#### 为什么要索引？

当我们查阅一本几千页的书时，常常是先看看目录，然后寻找最感兴趣的部分并直接根据页码翻到那个地方进行具体查阅。很明显，这样的查阅效率很高。这就是一种索引。数据库一样，当在一个海量的数据表中寻找数据时，如果有索引，我们的查询速度将会非常快。

**索引的目的在于提高查询效率**，可以类比字典，如果要查“mysql”这个单词，我们肯定需要定位到m字母，然后从下往下找到y字母，再找到剩下的sql。如果没有索引，那么你可能需要把所有单词看一遍才能找到你想要的，如果我想找到m开头的单词呢？或者ze开头的单词呢？是不是觉得如果没有索引，这个事情根本无法完成？

#### 索引操作

* **查看索引**

`show index from 表名;`

* **创建索引**

如果指定字段是字符串，需要指定长度，建议长度与定义字段时的长度一致；  
字段类型如果不是字符串，可以不填写长度部分

`create index 索引名称 on 表名(字段名称(长度))`

* **删除索引：**

`drop index 索引名称 on 表名;`

#### 索引效果示例





## 3.4.5 一些账户管理知识

## 3.4.6 数据库设计基础知识



