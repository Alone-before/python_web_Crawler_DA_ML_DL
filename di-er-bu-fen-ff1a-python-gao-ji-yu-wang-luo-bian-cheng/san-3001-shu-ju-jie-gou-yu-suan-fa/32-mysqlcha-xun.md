# 3.2 MySQL 语句

**MySQL语句的关键词不区分大小写，语句以逗号为结束符，--为MySQL语句注释行。本节的所有命令操作均可以在终端命令实操后显示查看，建议初学者可以在图形化界面同步查看以便加深理解。**

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
create database jing_dong charset=utf8;
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

主要包括表的创建、删除、属性查看、显示当前数据库的表、表头的增删改查。

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
例： 突然项目通知，我们的客户所需要的商品的名称一般都很容易记着，根本不需要简称，那我们需要删除它。
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









### 3. 数据增删改查

### 4. 数据备份与恢复命令

## 3.2.2 MySQL查询

### 1. 条件查询

### 2. 排序查询

### 3. 集合\(统计\)函数

### 4. 分组与分页查询

### 5. 连接查询

### 6. 自关联查询

### 7. 子查询

### 8. 小结



