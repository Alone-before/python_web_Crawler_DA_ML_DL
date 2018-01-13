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





## 3.4.2 事务

## 3.4.4 函数

## 3.4.4 索引

## 3.4.5 一些账户管理知识

## 3.4.6 数据库设计基础知识



