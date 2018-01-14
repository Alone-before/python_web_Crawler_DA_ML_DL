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

MySQL数据库提供了很多函数包括：

* 数学函数；
* 字符串函数；
* 日期和时间函数；
* 条件判断函数；
* 系统信息函数；
* 加密函数；
* 格式化函数；

详见链接[https://www.cnblogs.com/kissdodog/p/4168721.html,笔者已将其转化为pdf放置与源代码同目录内，为mysql\_function.pdf](https://www.cnblogs.com/kissdodog/p/4168721.html,笔者已将其转化为pdf放置与源代码同目录内，为mysql_function.pdf)

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

我们在mysql终端窗口先创建一个表test\_index，并通过python向其插入10000行形如”py-%d“的数据。

```
create table test_index(title varchar(10));
```

```py
‘’‘s8python_mysql_index.py  插入10000行数据’‘’
import pymysql

def main():
    # 创建Connection连接
    conn = pymysql.connect(host='localhost', port=3306, database='jing_dong',
                           user='root', password='hitzzy', charset='utf8')
    # 获得Cursor对象
    cursor = conn.cursor()
    # 插入10万次数据
    for i in range(100000):
        cursor.execute("insert into test_index values('py-%d')" % i)
    # 提交数据
    conn.commit()

if __name__ == "__main__":
    main()
```

![](/assets/mysql_index2.png)

可以看到已经插入了10000行数据。接下来我们进行以下有索引时和无索引时查询操作:

```
-- 开启运行时间监测：
set profiling=1;
-- 查找第1万条数据py-99999  无索引
select * from test_index where title='py-99999';

-- 为表title_index的title列创建索引：
create index title_index on test_index(title(10));
-- 查找第1万条数据py-99999  有索引
select * from test_index where title='py-99999';
-- 查看执行的时间：
show profiles;
```

![](/assets/mysql_index3.png)

从结果中可以看到，使用索引前，花费了0.036秒；使用索引后，花费了0.0004秒。整整73倍的差距，在海量数据时更加明显。

_注：索引是占用存储空间的，且建立太多的索引将会影响更新和插入的速度，因为它需要同样更新每个索引文件。对于一个经常需要更新和插入的表格，就没有必要为一个很少使用的where字句单独建立索引了，对于比较小的表，排序的开销不会很大，也没有必要建立另外的索引。_

## 3.4.5 一些账户管理知识

#### 账户管理

* 在生产环境下操作数据库时，绝对不可以使用root账户连接，而是创建特定的账户，授予这个账户特定的操作权限，然后连接进行操作，主要的操作就是数据的crud
* MySQL账户体系：根据账户所具有的权限的不同，MySQL的账户可以分为以下几种
  * 服务实例级账号：，启动了一个mysqld，即为一个数据库实例；如果某用户如root,拥有服务实例级分配的权限，那么该账号就可以删除所有的数据库、连同这些库中的表
  * 数据库级别账号：对特定数据库执行增删改查的所有操作
  * 数据表级别账号：对特定表执行增删改查等所有操作
  * 字段级别的权限：对某些表的特定字段进行操作
  * 存储程序级别的账号：对存储程序进行增删改查的操作
* 账户的操作主要包括创建账户、删除账户、修改密码、授权权限等

注意：

1. 进行账户操作时，需要使用root账户登录，这个账户拥有最高的实例级权限
2. 通常都使用数据库级操作权限

#### 授予权限

需要使用实例级账户登录后操作，以root为例

主要操作包括：

* 查看所有用户
* 修改密码
* 删除用户

##### 1. 查看所有用户

* 所有用户及权限信息存储在mysql数据库的user表中
* 查看user表的结构

```
desc user;
```

* 主要字段说明：
  * Host表示允许访问的主机
  * User表示用户名
  * authentication\_string表示密码，为加密后的值

查看所有用户

```
select host,user,authentication_string from user ;
```

结果

```
mysql
>
 select host,user,authentication_string from user;
+-----------+------------------+-------------------------------------------+
| host      | user             | authentication_string                     |
+-----------+------------------+-------------------------------------------+
| localhost | root             | *E74858DB86EBA20BC33D0AECAE8A8108C56B17FA |
| localhost | mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
| localhost | debian-sys-maint | *EFED9C764966EDB33BB7318E1CBD122C0DFE4827 |
+-----------+------------------+-------------------------------------------+
3 rows in set (0.00 sec)
```

##### 2. 创建账户、授权

* 需要使用实例级账户登录后操作，以root为例
* 常用权限主要包括：create、alter、drop、insert、update、delete、select
* 如果分配所有权限，可以使用all privileges

###### 2.1 创建账户&授权

```
grant 权限列表 on 数据库 to '用户名'@'访问主机'identified by '密码';
```

**2.2 示例1**

创建一个`laowang`的账号，密码为`123456`，只能通过本地访问, 并且只能对`jing_dong`数据库中的所有表进行`读`操作

**step1：使用root登录**

```
mysql -uroot -p
回车后写密码，然后回车
```

**step2：创建账户并授予所有权限**

```
grant 权限列表 on 数据库 to '用户名'@'访问主机' identified by '密码';
```

说明

* 可以操作python数据库的所有表，方式为:
  `jing_dong.*`
* 访问主机通常使用 百分号% 表示此账户可以使用任何ip的主机登录访问此数据库
* 访问主机可以设置成 localhost或具体的ip，表示只允许本机或特定主机访问

* 查看用户有哪些权限

```
show grants for laowang@localhost;
```

**step3：退出root的登录**

```
quit
```

**step4：使用laowang账户登录**

```
mysql -ulaowang -p
回车后写密码，然后回车
```

**2.3 示例2**

创建一个`laoli`的账号，密码为`12345678`，可以任意电脑进行链接访问, 并且对`jing_dong`数据库中的所有表拥有所有权限

```
grant all privileges on jing_dong.* to "laoli"@"%" identified by "12345678"
```

#### 账户操作

##### 1. 修改权限

```
 删除账户
语法1：使用root登录grant 权限名称 on 数据库 to 账户@主机 with grant option;
```

##### 2. 修改密码

使用root登录，修改mysql数据库的user表

* 使用password\(\)函数进行密码加密

```
update user set authentication_string=password('新密码') where user='用户名';
例：
update user set authentication_string=password('123') where user='laowang';
```

* 注意修改完成后需要刷新权限

```
刷新权限：flush privileges
```

##### 3.删除账户

* 语法1：使用root登录

```
drop user '用户名'@'主机';
例：
drop user 'laowang'@'%';
```

* 语法2：使用root登录，删除mysql数据库的user表中数据

```
delete from user where user='用户名';
例：
delete from user where user='laowang';

-- 操作结束之后需要刷新权限
flush privileges
```

_注：推荐使用语法1删除用户, 如果使用语法1删除失败，采用语法2方式。_

