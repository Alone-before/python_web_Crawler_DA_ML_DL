# 3.2 MySQL 语句

**MySQL语句的关键词不区分大小写，语句以逗号为结束符，--为MySQL语句注释行。本节的所有命令操作均可以在终端命令实操后显示查看，建议初学者可以在图形化界面同步查看以便加深理解。笔者曾从事于传统IT行业，所以本章全程贯穿一个京东电子产品的数据库实例来进行演示各个语句以便我们更好的理解。**

## 3.2.1 MySQL基本操作

### 1. 数据库操作

主要包括数据库的查看、创建、使用、删除操作。

* **查看当前有哪些数据库       **

show databases;

```
mysql> show databases;

+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
可以看到，目前数据库里有默认的四个数据库，其中：mysql为本地服务器的配置、sys为系统配置信息。
```

* **创建数据库 **create database 数据库名 \[其他选项\];

```MySQL
create database jing_dong;


-- create database jing_dong charset=utf8;
-- charset是指数据库所用的编码集
```

* **使用数据库:**use 数据库名

```
use jing_dong;
```

```
mysql> use jing_dong;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

可以看到提示，数据库发生了改变。
```

* **查看当前使用的数据库**

```
select database();
```

```
mysql> select database();
+------------+
| database() |
+------------+
| jing_dong  |
+------------+

可以看到我们正在使用的数据库是jing_dong
```

* **删除数据库     **drop database 数据库名；

```
drop database jing_dong;
```

```
mysql> drop database jing_dong;
Query OK, 0 rows affected (0.04 sec)
通过显示所有数据库的命令会发现jing_dong数据库已被删除。
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```

### 2. 数据表操作

主要包括表的创建、删除、属性查看、显示当前数据库的表及属性、表头的增删改查。

* **创建表**

```
create table 表名称(列声明);
详解：
CREATE TABLE table_name(
    column1 datatype contrai,
    column2 datatype,
    column3 datatype,
    .....
    columnN datatype,
    PRIMARY KEY(one or more columns)
);
```

示例：创建商品种类表goods\_cates

```
create table goods_cates(
    id int unsigned primary key auto_increment not null,
    name varchar(40) not null
);
```

列id，代表商品种类id，取值类型为int unsigned，primary key指id列为主键， 值为自增auto\_increment ,且不能为空\(not null\)；  
列name，代表商品种类名称，取值为最长40的字符，不能为空  
**注意：最后一列的后面不能有逗号**

```
系统会提示：
Query OK, 0 rows affected (0.04 sec)
说明添加成功
```

* **显示表**

```
show tables;
```

可以看到goods\_cates表已在数据库中。

```
mysql> show tables;
+----------------+
| Tables_in_jing |
+----------------+
| goods_cates    |
+----------------+
1 row in set (0.00 sec)
```

* **查看表结构**

```
desc 表名;

例：
desc goods_cates;
```

可以看到goods\_cates表的表头信息：共有两个字段id和name，以及它们的详细信息。

```
mysql> desc goods_cates;
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(40)      | NO   |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+
2 rows in set (0.01 sec)
```

* **添加字段\(列\)**

```
alter table 表名 add 列名 类型;

例：假设刚才我们所统计的商品种类名字太长，需要简称，那么向商品种类表中增加列abbreviation（种类简称）
alter table goods_cates add abbreviation varchar(5);
```

```
终端返回以下信息，说明添加成功。
mysql> alter table goods_cates add abbreviation varchar(5);
Query OK, 0 rows affected (0.05 sec)
Records: 0  Duplicates: 0  Warnings: 0
```

通过查看表结构来看是否添加成功abbreviation。里面已经有了该列。

```
mysql> desc goods_cates;
+--------------+------------------+------+-----+---------+----------------+
| Field        | Type             | Null | Key | Default | Extra          |
+--------------+------------------+------+-----+---------+----------------+
| id           | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name         | varchar(40)      | NO   |     | NULL    |                |
| abbreviation | varchar(5)       | YES  |     | NULL    |                |
+--------------+------------------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```

* **修改字段\(列\)**

```
不重命名版：alter table 表名 modify 列名 类型及约束;   

例：假设我们现在认为简写还是太长了，仅仅需要3个长度的字符就可以。
alter table goods_cates modify abbreviation varchar(3);
```

运行后，通过查看表结构，可以看到这一列的数据类型修改为varchar\(3\)了。

```
+--------------+------------------+------+-----+---------+----------------+
| Field        | Type             | Null | Key | Default | Extra          |
+--------------+------------------+------+-----+---------+----------------+
| id           | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name         | varchar(40)      | NO   |     | NULL    |                |
| abbreviation | varchar(3)       | YES  |     | NULL    |                |
+--------------+------------------+------+-----+---------+----------------+
```

```
重命名版：alter table 表名 change 列原名 列新名 类型及约束;   

例：假设我们觉得表头里“abbreviation”这个单词太长了，想修改为“简称”。
alter table goods_cates change abbreviation 简称 varchar(3);
```

运行后，通过查看表结构，可以看到这一列的表头更改为“简称”了。

```
+--------+------------------+------+-----+---------+----------------+
| Field  | Type             | Null | Key | Default | Extra          |
+--------+------------------+------+-----+---------+----------------+
| id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name   | varchar(40)      | NO   |     | NULL    |                |
| 简称    | varchar(3)       | YES  |     | NULL    |                |
+--------+------------------+------+-----+---------+----------------+
```

* **删除字段\(列\)**

```
alter table 表名 drop 列名;

例： 突然项目通知，我们的客户所需要的商品的名称一般都很容易记着，根本不需要简称，我们需要删除它。
alter table goods_cates drop 简称;
```

可以看到，已经删除：

```
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(40)      | NO   |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+
```

* **查看创建表的语句**

```
show create table 表名;

例：假如我们刚进入一个新环境拿到一个新账号需要操作，一般我们可以先看一下表的一些信息。
show create table goods_cates;
```

可以看到goods\_cates表的数据引擎为InnoDB，字符集为latin1 ；主键时字头id等等。

注：**一般建议在创建数据库时指定字符集类型，比如utf8 。 create database jing\_dong charset=utf8;**

    +-------------+-------------------------------------------
    | Table       | Create Table                                                                                                                                                          
    +-------------+------------------------------------------
    | goods_cates | CREATE TABLE `goods_cates` (
      `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
      `name` varchar(40) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
    +-------------+------------------------------------------

* **删除表**

```
drop table 表名;

例：非常抱歉，项目通知设计中取消掉这一表。
drop table goods_cates;
```

通过查看表语句`show tables;`发现jing\_dong数据库没有这个表了，由于我们只创建了这一个表，所以提示为空。

```
mysql> show tables;
Empty set (0.00 sec)
```

**好了，我们可以重新删除掉jing\_dong数据库，从一开始就定义数据库字符集为utf8来不断演练以上两节的操作了。**

### 3. 数据增删改查

以上两节相信我们已经可以在数据库里拥有表了。本小节主要来说明在表内增加数据、删除数据、修改数据和简单查询数据。

本小节讲解时会用到以下数据，先列出。大家也可以去之前提到的源码网址获取。

```
id,name
1,台式机
2,平板电脑
3,服务器/工作站
4,游戏本
5,笔记本
6,笔记本配件
7,超级本
8,路由器
9,交换机
10,网卡
```

* **添加数据行**

```
insert [into] 表名 [(列名1, 列名2, 列名3, ...)] values (值1, 值2, 值3, ...);

例：
insert into goods_cates values (0, '台式机');
```

注：也可以一次insert命令添加多条数据行：`insert into goods_cates values (0, '台式机'),(0, '平板电脑');`

* **查询数据行**

```
select 列名称 from 表名称 [查询条件];

例：查询我们添加的所有数据
select * from goods_cates;
```

注： \* 号代表全部.

可以查询看到我们添加的“台式机”。其中，id在台式机那一行为1，是因为我们之前在建立表格时设置其为自增的int数据，因此系统会默认为其赋值，我们一般用0进行占位。

```
+----+-----------+
| id | name      |
+----+-----------+
|  1 | 台式机    |
+----+-----------+
```

**拓展：**我们可以重复利用insert语句将以上提到的1条语句全部添加到数据库，但是很麻烦；所以我们把所有数据存入文件并**通过文件导入。**

```
load data local infile '/path/goods_cates.txt' into table goods_cates;

其中：path为文件存在路径。
```

通过查询所有来查看数据，已经成功导入。

```
mysql> select * from goods_cates;
+----+---------------------+
| id | name                |
+----+---------------------+
|  1 | 台式机               |
|  2 | 平板电脑             |
|  3 | 服务器/工作站         |
|  4 | 游戏本               |
|  5 | 笔记本               |
|  6 | 笔记本配件            |
|  7 | 超级本               |
|  8 | 路由器               |
|  9 | 交换机               |
| 10 | 网卡                 |
+----+---------------------+
```

* **修改数据行**

```
update 表名称 set 列名称=新值 where 更新条件;

例：
update goods_cates set name='柔性手机' where id=10;
```

系统返回信息一行已更新，如下：

```
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

通过查询操作，会发现id=10的数据行中name列的值已修改。

```
mysql> select * from goods_cates;
+----+---------------------+
| id | name                |
+----+---------------------+
|  1 | 台式机              |
|  2 | 平板电脑            |
|  3 | 服务器/工作站       |
|  4 | 游戏本              |
|  5 | 笔记本              |
|  6 | 笔记本配件          |
|  7 | 超级本              |
|  8 | 路由器              |
|  9 | 交换机              |
| 10 | 柔性手机            |
+----+---------------------+
```

* **删除数据行**

```
delete from 表名 where 条件

例：
delete from goods_cates where id=10;
```

系统会告诉我们，有一行数据有形象，如

```
Query OK, 1 row affected (0.00 sec)
```

通过查询语句来查看，我们发现柔性手机那一行已被删除。

```
mysql> select * from goods_cates;
+----+---------------------+
| id | name                |
+----+---------------------+
|  1 | 台式机              |
|  2 | 平板电脑            |
|  3 | 服务器/工作站       |
|  4 | 游戏本              |
|  5 | 笔记本              |
|  6 | 笔记本配件          |
|  7 | 超级本              |
|  8 | 路由器              |
|  9 | 交换机              |
+----+---------------------+
```

### 4. 数据备份与恢复命令

和平常生活一样，我们都喜欢备份和恢复，所以在基本操作最后一小节里列出备份和恢复命令。

* **备份**

运行mysqldump命令

```
示例：
mysqldump –uroot –p 数据库名 > python.sql;

# 按提示输入mysql的密码
```

* **恢复**

连接mysql，创建新的数据库

退出连接，执行如下命令：

```
mysql -uroot –p 新数据库名 < python.sql

# 根据提示输入mysql密码
```

## 3.2.2 MySQL查询

上一节中演示了基本的select \* from goods\_cates查询，可以获取到goods\_\_cates里的所有数据。但是当数据量大时，就需要各种合适的查询方式来获取指定的信息并呈现给我们。本节就来讲述并演示这些操作。在开始之间我们先介绍几个会用到的命令。

* **查询指定列\(指定字段\)**

```
select 列1,列2,... from 表名;
例:
select name from goods_cates;
```

```
+---------------------+
| name                |
+---------------------+
| 台式机              |
| 平板电脑            |
| 服务器/工作站       |
| 游戏本              |
| 笔记本              |
| 笔记本配件          |
| 超级本              |
| 路由器              |
| 交换机              |
| 网卡                |
+---------------------+
```

* **查询指定列，并在显示中为它指定别名**

```
select id as 序号, name as 名字 from goods_cates;
```

```
+--------+---------------------+
| 序号   | 名字                |
+--------+---------------------+
|      1 | 台式机              |
|      2 | 平板电脑            |
|      3 | 服务器/工作站       |
|      4 | 游戏本              |
|      5 | 笔记本              |
|      6 | 笔记本配件          |
|      7 | 超级本              |
|      8 | 路由器              |
|      9 | 交换机              |
|     10 | 网卡                |
+--------+---------------------+
```

注： as也可以为表等起别名以便简化语句等等。

* **查询时，显示时消除重复列**

在select后面列前使用distinct可以消除重复的行

```
select distinct 列1,... from 表名;
```

我们在goods\_cates表中先添加一列id=15，name=网卡的数据。

```
insert into goods_cates values (15, '网卡');



+----+---------------------+
| id | name                |
+----+---------------------+
|  1 | 台式机              |
|  2 | 平板电脑            |
|  3 | 服务器/工作站       |
|  4 | 游戏本              |
|  5 | 笔记本              |
|  6 | 笔记本配件          |
|  7 | 超级本              |
|  8 | 路由器              |
|  9 | 交换机              |
| 10 | 网卡                |
| 15 | 网卡                |
+----+---------------------+
```

接下来，我们获取name列，但不显示id。

```
mysql> select name from goods_cates;
+---------------------+
| name                |
+---------------------+
| 台式机              |
| 平板电脑            |
| 服务器/工作站       |
| 游戏本              |
| 笔记本              |
| 笔记本配件          |
| 超级本              |
| 路由器              |
| 交换机              |
| 网卡                |
| 网卡                |
+---------------------+
```

可以看到，显示了两行网卡。我们通过distinct来消除重复并显示，就剩一个网卡了。哇，针实用，就像EXCEL里面去重选项那样来识别本列有多少种选项。

```
mysql> select distinct name from goods_cates;
+---------------------+
| name                |
+---------------------+
| 台式机              |
| 平板电脑            |
| 服务器/工作站       |
| 游戏本              |
| 笔记本              |
| 笔记本配件          |
| 超级本              |
| 路由器              |
| 交换机              |
| 网卡                |
+---------------------+
```

### 1. 条件查询

细心的朋友会发现我们上一节删除数据行时已经实用过where关键词，没错，它就是用来条件查询的一个重要关键词。一般使用where子句来筛选获取其后语句为True的数据行。其查询的语句格式为：

```
select * from 表名 where 条件;
例：
select * from grands_goods where id=1;
```

where后面支持多种运算符，进行条件的处理

* 比较运算符
* 逻辑运算符
* 模糊查询
* 范围查询
* 空判断

接下来我们一一演示说明。

* **比较运算符**

```
等于: =
大于: >
大于等于: >=
小于: <
小于等于: <=
不等于: != 
```

示例：查询id大于7的商品种类

```
select * from goods_cates where id > 7;
```

```
+----+-----------+
| id | name      |
+----+-----------+
|  8 | 路由器    |
|  9 | 交换机    |
| 10 | 网卡      |
| 15 | 网卡      |
+----+-----------+
```

* **逻辑运算符**

```
and   与
or    或
not   非
建议为了程序逻辑易读性，可以结合括号操作
```

示例：查询name=网卡，并且id=10的商品种类

```
select * from goods_cates where name="网卡" and id = 10;
```

```
+----+--------+
| id | name   |
+----+--------+
| 10 | 网卡   |
+----+--------+
```

* **模糊查询**

```
关键字： like

% 表示任意多个任意字符
_ 表示一个任意字符
```

示例：查询商品种类name中包含“本”的数据

```
select * from goods_cates where name like '%本';
```

```
+----+-----------+
| id | name      |
+----+-----------+
|  4 | 游戏本    |
|  5 | 笔记本    |
|  7 | 超级本    |
+----+-----------+
```

* **范围查询**

```
in表示在一个非连续的范围内

between ... and ...表示在一个连续的范围内
```

示例：查询商品种类id为1、3、5的数据

```
select * from goods_cates where id in(1,3,5);
```

```
+----+---------------------+
| id | name                |
+----+---------------------+
|  1 | 台式机              |
|  3 | 服务器/工作站       |
|  5 | 笔记本              |
+----+---------------------+
```

示例：查询商品种类id为1到5的数据

```
select * from goods_cates where id between 1 and 5;
```

```
+----+---------------------+
| id | name                |
+----+---------------------+
|  1 | 台式机              |
|  2 | 平板电脑            |
|  3 | 服务器/工作站       |
|  4 | 游戏本              |
|  5 | 笔记本              |
+----+---------------------+
```

* **空判断**

```
判空is null
注意：null与''是不同的
```

### 2. 排序查询



### 3. 集合\(统计\)函数

### 4. 分组与分页查询

### 5. 连接查询

### 6. 自关联查询

### 7. 子查询

### 8. 小结



