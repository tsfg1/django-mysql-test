[TOC]



# 1配置

安装环境: PyMySQL

PyMySQL是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中是使用mysqldb。

# 2 创建一个项目

startproject

# 3 配置mysql数据库（参考之前的windows下安装mysql）

windoows下安装mysql

mysqlworkerbranch

![1635131116948](C:\Users\WGJ\Desktop\python_md\1635131116948.png)

![1635131186007](C:\Users\WGJ\Desktop\python_md\1635131186007.png)

name： 用workerbranch新建一个database 比如叫mydata

将原有模块，例如admin中的数据库迁移到 mydata数据库中

python manage.py migrate

![1635146053306](C:\Users\WGJ\Desktop\python_md\1635146053306.png)

那么用户名和密码是多少那？

# 4 django-admin账户

在django中创建超级管理员

python manage.py createsuperuser

输入账号名和密码

# 5 写一个简单的登录界面

创建一个自己的应用

​	

配置主路由

![1635150370605](C:\Users\WGJ\Desktop\python_md\1635150370605.png)

配置应用子路由

![1635150915578](C:\Users\WGJ\Desktop\python_md\1635150915578.png)

views.py

![1635150799958](C:\Users\WGJ\Desktop\python_md\1635150799958.png)

配置模板

![1635151499766](C:\Users\WGJ\Desktop\python_md\1635151499766.png)

创建.html文件

![1635151625267](C:\Users\WGJ\Desktop\python_md\1635151625267.png)

子app加入到 主应用 中

![1635151759497](C:\Users\WGJ\Desktop\python_md\1635151759497.png)

改变html样式

![1635151879514](C:\Users\WGJ\Desktop\python_md\1635151879514.png)

![1635151915342](C:\Users\WGJ\Desktop\python_md\1635151915342.png)

# 6 登录界面---使用get和post做一个登录功能

修改.html

![1635154720298](C:\Users\WGJ\Desktop\python_md\1635154720298.png)

![](C:\Users\WGJ\Desktop\python_md\1635154748074.png)

配路由（注意：polls路由已经在主路由中配置，此处只需要加/index即可）

Login_view处理逻辑：判断账号和密码是否匹配

（注意：此处/index写错了，应该为index/）

![1635155031885](C:\Users\WGJ\Desktop\python_md\1635155031885.png)

修改.html

点提交时会跳转到polls/index界面（前端知识）

【然后会找到上一处配的路由polls/index

![1635155106967](C:\Users\WGJ\Desktop\python_md\1635155106967.png)

修改views.py

![1635151625267](C:\Users\WGJ\Desktop\python_md\163521605731922.png)

注意：此处的GET和.html中的methon="get"相对应



修改views.py中的逻辑：

（写死判断）

![1635216334794](C:\Users\WGJ\Desktop\python_md\1635216334794.png)



登录一般不会用get请求

![1635216470013](C:\Users\WGJ\Desktop\python_md\16352164700131.png)

修改login.html

改为post请求

![1635216642600](C:\Users\WGJ\Desktop\python_md\1635216642600.png)

（如果报错：改为/polls/index/）



修改views.py

将GET改为POST

![1635218305182](C:\Users\WGJ\Desktop\python_md\1635218305182.png)



crf错误()

![1635217135743](C:\Users\WGJ\Desktop\python_md\16352171135743.png)

修改login.html

![1635217263696](C:\Users\WGJ\Desktop\python_md\16315217263696.png)

# 7 链接数据库判断登录

修改models.py

![1635220122427](C:\Users\WGJ\Desktop\python_md\1635220122427.png)

class studentinfo 

在django中是一个数据模型

在数据库中是一张表



添加字段

![1635234601761](C:\Users\WGJ\Desktop\python_md\1635234601761.png)





![1635234717808](C:\Users\WGJ\Desktop\python_md\1635234717808.png)



制造迁移的文件，

应用名为polls：

python.exe .\manage.py makemigrations polls

![1635234799399](C:\Users\WGJ\Desktop\python_md\1635234799399.png)

运行完以后会多一个文件 

![1635234977085](C:\Users\WGJ\Desktop\python_md\1635234977085.png)





把迁移文件的内容迁移到数据库



![1635235389161](C:\Users\WGJ\Desktop\python_md\1635235389161.png)



看一下迁移文件的内容：（就是把模型生成了数据库文件）

![1635235516667](C:\Users\WGJ\Desktop\python_md\1635235516667.png)



数据库表中增加一条记录：

![1635235730632](C:\Users\WGJ\Desktop\python_md\1635235730632.png)



修改views.py

查找stu_name为u, stu_psw为p的记录 的个数

![1635236019201](C:\Users\WGJ\Desktop\python_md\1635236019201.png)



## models.py中修改比如把filed从20改为60，不能直接反映到mysql数据库中，后续：经过试验

在models.py中修改后，不会主动生成下面的文件

![1635237664844](C:\Users\WGJ\Desktop\python_md\1635237664844.png)

需要执行

python manage.py makemigrations polls

然后执行

python manage.py mirgate 

才能同步到数据库



# 8 数据库 反映射 数据模型 到models

和之前的 反过来

在数据库中创建一张表------生成models.py中的代码

![1635239400723](C:\Users\WGJ\Desktop\python_md\1635239400723.png)

命令：

python.exe .\manage.py inspectdb > polls/models.py

![1635239488162](C:\Users\WGJ\Desktop\python_md\1635239488162.png)

查看models.py中的代码：

db_table为表名

![1635239628580](C:\Users\WGJ\Desktop\python_md\1635239628580.png)



# 9 注册功能 连接数据库

注册以后，输入到数据库中

新增register.html

![1635303390248](C:\Users\WGJ\Desktop\python_md\1635303390248.png)

修改urls.py

![1635303449644](C:\Users\WGJ\Desktop\python_md\1635303449644.png)

修改views.py

![1635303902521](C:\Users\WGJ\Desktop\python_md\1635303902521.png)



首先要到了register.html的这个界面

修改urls.py

![1635304081284](C:\Users\WGJ\Desktop\python_md\1635304081284.png)

修改views.py

![1635304196602](C:\Users\WGJ\Desktop\python_md\1635304196602.png)

增加点提示：

![1635304237184](C:\Users\WGJ\Desktop\python_md\1635304237184.png)

注册完后看一下数据库中有没有？

![1635304394800](C:\Users\WGJ\Desktop\python_md\1635304394800.png)

但是可以看到没有stu_id

生成一个随机数（测试代码）

![1635304692652](C:\Users\WGJ\Desktop\python_md\1635304692652.png)

数据库中查看

![1635304614377](C:\Users\WGJ\Desktop\python_md\1635304614377.png)



## 记录一个问题：

启动runserver时报错：

 File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed ValueError: source code string cannot contain null bytes

注意：执行 python.exe .\manage.py inspectdb > .\polls\models.py 命令完后，生成的models.py的编码格式为utf-16，需要用notepad++改为utf-8



## 记录迁移数据库时：新建表后，迁移失败的问题

https://blog.csdn.net/u011630575/article/details/51065052

