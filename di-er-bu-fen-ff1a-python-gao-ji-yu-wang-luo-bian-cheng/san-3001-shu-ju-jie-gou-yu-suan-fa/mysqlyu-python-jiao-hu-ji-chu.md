# 3.3 MySQL 与python交互

## 3.3.1 实例数据库创建——京东商品数据库

此处我们创建三个表：goods代表商品，goods\_cates代表商品种类_，_goods\_brands代表品牌 。

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

## 3.3.3 pymysql语句



