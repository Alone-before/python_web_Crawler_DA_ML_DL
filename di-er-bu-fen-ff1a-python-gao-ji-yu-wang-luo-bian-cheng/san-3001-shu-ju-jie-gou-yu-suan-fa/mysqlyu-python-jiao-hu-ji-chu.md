# 3.3 MySQL 与python交互

## 3.3.1 实例数据库创建——京东商品数据库

此处我们创建三个表：goods代表商品，goods\_cates代表商品种类\_，\_goods\_brands代表品牌 。

![](/assets/mysqljingdong.png)

具体操作代码，见源码中的create\_ jing \_ dong.sql，如下：

```
-- 创建'京东'数据库
create database jing_dong charset=utf8;
-- 使用'京东'数据库
use jing_dong;
-- 表设计并创建开始
-- 创建'商品分类'表
create table goods_cates(
    id int unsigned primary key auto_increment not null,
    name varchar(40) not null
);
-- 创建'商品品牌'表
create table goods_brands (
    id int unsigned primary key auto_increment not null,
    name varchar(40) not null
);
-- 创建 '商品' 表
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(40) default '',
    price decimal(5,2),
    cate_id int unsigned,
    brand_id int unsigned,
    is_show bit default 1,
    is_saleoff bit default 0,
    foreign key(cate_id) references goods_cates(id),
    foreign key(brand_id) references goods_brands(id)
);
-- 由于外键关系，需要先创建goods_cates 和 goods_brands
-- foreign key 外键， 如下六行注释为操作示例
-- 
-- 给brand_id 添加外键约束
--alter table goods add foreign key (brand_id) references goods_brands(id);
-- 获取外键名称
-- show create table goods;
-- 删除外键
-- alter table goods drop foreign key 外键名称;
--
-- 表设计创建完成
-- 向goods_brands添加数据  path为路径
load data local infile '/path/goods_brands.txt' into table goods_brands;
-- 向goods_cates添加数据
load data local infile '/path/goods_cates.txt' into table goods_cates;
-- 向goods表添加数据
load data local infile '/path/goods.txt' into table goods;
-- 也可以用load导入txt文本方法：LOAD DATA LOCAL INFILE '/路径/jingdong.txt' INTO TABLE goods
-- 导出数据SELECT * FROM goods INTO OUTFILE '路径文件';  需要权限设置
```

```
注：此处是采用三个文本文件导入数据，源数据见源代码文件夹相应名称的文件。由于外键的关系，一些情况也可以在拥有goods表数据后，
也同步更新goods_cates和 goods_brands。可采用如下命令。
```

获得三个数据表如下：

![](/assets/mysqltables.png)

## 3.3.2 交互操作逻辑

本章我们使用第三方库pymysql来说明mysql和python的交互。在使用python操作mysql前，一般需要终端命令安装该库：

`pip install pymysql`。

使用python操作mysql的逻辑如下图所示。基本过程为：1、开始；2、创建连接connection；3、创建并获取操作游标cursor；4、执行操作；5、关闭游标cursor；6、关闭连接； 7、结束。下面我们举一个简单例子**s1python\_mysql\_sample.py 来实现向goods\_cates表里插入两行数据：\(0,'硬盘'\)，\(0，'光盘'\)。**

![](/assets/mysqlpython1.png)

```
import pymysql  # 1、导入pymsql模块

# connect对象用于建立连接
# host：mysql主机
# port： mysql端口默认3306
# database：数据库名称
# user： 用户名
# password： 密码
# charset： 通信编码
# 2、创建连接，设置连接ip，port，用户，密码，以及所要连接的数据库
conn = pymysql.connect(host='localhost', port=3306,database='jing_dong', user='root', password='hitzzy',
                       charset='utf8')
# cursor对象用于执行SQL语句
# 3、创建游标, 操作数据库, 指定游标返回内容为字典类型
cs1 = conn.cursor()
# 4、执行语句 execute（），返回受影响的行数结果。
count = cs1.execute('insert into goods_cates(name) values("硬盘")')
print(count)

count = cs1.execute('insert into goods_cates(name) values("光盘")')
print(count)
# 5、提交操作
conn.commit()
# 6、关闭游标和连接
cs1.close()
conn.close()
```

运行程序后，通过mysql终端查询语句查询goods\_cates表，我们会发现，末尾已经添加了两行我们刚才添加的数据。

![](/assets/mysql_python_sample.png)

## 3.3.3 pymysql语句

1. 命令介绍

2. 实例操作



