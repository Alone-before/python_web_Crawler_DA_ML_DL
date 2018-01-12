# 3.2 MySQL 语句

**MySQL语句的关键词不区分大小写，语句以逗号为结束符。本节的所有命令操作均可以在终端命令实操后显示查看，建议初学者可以在图形化界面同步查看以便加深理解。**

## 3.2.1 MySQL基本操作

### 1. 数据库操作

**查看当前有哪些数据库**

```MySQL
show databases;
```

```
可以看到，目前数据库里有默认的四个数据库，其中：mysql为本地服务器的配置、sys为系统配置信息。
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

**创建数据库 **create database 数据库名 \[其他选项\];

```MySQL
create database jing_dong charset=utf8;
```



**使用数据库:**use 数据库名

```
use jing_dong;
```

```
可以看到提示，数据库发生了改变。
mysql> use jing_dong;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
```















### 2. 数据表操作

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



