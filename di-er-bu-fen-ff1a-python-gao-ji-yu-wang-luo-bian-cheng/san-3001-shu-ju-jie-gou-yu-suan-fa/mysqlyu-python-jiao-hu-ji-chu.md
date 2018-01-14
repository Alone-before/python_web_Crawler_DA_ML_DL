# 3.3 MySQL 与python交互

## 3.3.1 实例数据库创建——京东商品数据库

此处我们创建三个表，为后面两章\(3.3和3.4\)演练服务：goods代表商品，goods\_cates代表商品种类\_，\_goods\_brands代表品牌 。

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

```py
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

上一节中我们用了一个简单实例演示了python操作mysql的基本流程，本节将详细讲述里面的一些基本命令含义及其参数，并进行几个实例演练。

### Connection 对象

* 用于建立与数据库的连接

* 创建对象：调用connect\(\)方法

```py
conn=connect(参数列表)
```

* 参数host：连接的mysql主机，如果本机是'localhost'
* 参数port：连接的mysql主机的端口，默认是3306
* 参数database：数据库的名称
* 参数user：连接的用户名
* 参数password：连接的密码
* 参数charset：通信采用的编码方式，推荐使用utf8

#### 对象的方法 {#对象的方法}

* close\(\)关闭连接
* commit\(\)提交
* cursor\(\)返回Cursor对象，用于执行sql语句并获得结果

### Cursor对象

* 用于执行sql语句，使用频度最高的语句为select、insert、update、delete
* 获取Cursor对象：调用Connection对象的cursor\(\)方法

```py
cs1=conn.cursor()
```

#### 对象的方法 {#对象的方法}

* close\(\)关闭
* execute\(operation \[, parameters \]\)执行语句，返回受影响的行数，主要用于执行insert、update、delete语句，也可以执行create、alter、drop等语句
* fetchone\(\)执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
* fetchall\(\)执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回

#### 对象的属性 {#对象的属性}

* rowcount只读属性，表示最近一次execute\(\)执行后受影响的行数
* connection获得当前连接对象

示例1： s2python\_mysql\_fetchone.py  查询goods表中id不大于4的数据，以fetchone方法来获取查询到的数据。

```py
'''fetchone()获取单行结果并打印出来'''
import pymysql


def main():
    # 创建连接
    conn = pymysql.connect(host='localhost', port=3306,database='jing_dong', user='root', password='hitzzy',
                           charset='utf8')
    # 获取游标
    cs1 = conn.cursor()
    # 执行查询操作
    count = cs1.execute('select id,name from goods where id<=4')
    print('查询到%d条数据：' % count)
    # 打印查询结果
    for i in range(count):
        # fetchone（）执行查询语句时获取被影响的行的第一行
        result = cs1.fetchone()  # result 为一个元组哦
        # print(type(result))  # 可以查看result的数据类型，加深理解
        print(result)
    # 关闭游标和连接
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
```

![](/assets/s2mysql_python_fetchone.png)

示例2： s3python\_mysql\_fetchall.py  查询goods表中id不大于4的数据，以fetchall方法来获取查询到的数据。

```py
'''fetchall()获取所有行结果并打印出来'''
import pymysql


def main():
    find_name = input('请输入物品名称:') # 输入想要查询的物品名称
    # print('select * from goods where name like %{}%' .format(find_name))
    # 创建连接
    conn = pymysql.connect(host='localhost', port=3306,database='jing_dong', user='root', password='hitzzy',
                           charset='utf8')
    # 获取游标
    cs1 = conn.cursor()

    # 执行select语句，并返回受影响的行数：查询所有数据
    # 安全模式

    count = cs1.execute('select * from goods where name=%s', [find_name])

    # 非安全模式
    # 当find_name 被输入   " or 1 "    包含双引号时，会显示表中所有数据，造成数据泄露。
    # sql = 'select * from goods WHERE name="%s"' % find_name
    # count = cs1.execute(sql)

    print('查询到%d条数据：' % count)
    # 获取并打印查询到的数据
    result = cs1.fetchall()
    print(result)
    # 关闭游标和连接
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
```

![](/assets/s3python_mysql_fetchall.png)

示例3： s4python\_mysql\_safe.py   请用户输入商品名，并显示其具体信息。 ** \(注意SQL注入\)**

```py
'''sql注入'''
import pymysql


def main():
    find_name = input('请输入物品名称:') # 输入想要查询的物品名称
    # print('select * from goods where name like %{}%' .format(find_name))
    # 创建连接
    conn = pymysql.connect(host='localhost', port=3306,database='jing_dong', user='root', password='hitzzy',
                           charset='utf8')
    # 获取游标
    cs1 = conn.cursor()

    # 执行select语句，并返回受影响的行数：查询所有数据
    # 安全模式

    count = cs1.execute('select * from goods where name=%s', [find_name])

    # 非安全模式
    # 当find_name 被输入   " or 1 or "    包含双引号时，会显示表中所有数据，造成数据泄露。
    # sql = 'select * from goods WHERE name="%s"' % find_name
    # count = cs1.execute(sql)

    print('查询到%d条数据：' % count)
    # 获取并打印查询到的数据
    for i in range(count):
        # fetchone（）执行查询语句时获取被影响的行的第一行
        result = cs1.fetchone()  # result 为一个元组哦
        # print(type(result))  # 可以查看result的数据类型，加深理解
        print(result)
    # 关闭游标和连接
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
```

可以看到，当输入 x240 超极本，查询到此商品在库，并打印出该结果。

![](/assets/s4python_mysql_safe1.png)

不要着急，我们把代码中安全模式的行注释掉，将非安全模式的行取消注释，然后再次输入 x240 超极本。我们也能查询到该商品信息。也就是说，execute里可以是一个SQL语句的字符串。那为什么还需要前面语法介绍的参数赋值呢？

![](/assets/s4python_mysql_safe1.png)

再查询一种商品（“ or 1 or ”），再看看结果。奇怪，goods表中所有的数据都显示出来了。为什么呢？我们来分析一下。当把（“ or 1 or ”）赋值给find\_name时，sql字符串变量的值为 select \* from goods where name="“ or 1 or ”";大家看一下，where后的语句结果始终为True。所以会显示出goods表中所有数据，造成数据库数据泄露。**因此在使用execute语句时，尽量使用安全模式中的参数化赋值，以避免因疏忽造成的SQL注入并引发安全问题。**

![](/assets/s4python_mysql_safe2.png)

