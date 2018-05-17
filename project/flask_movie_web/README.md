# Flask 框架知识

1. 学会使用整型、浮点型、路径型、字符串行正则表达式路由转换器

2. 学会使用 `post` 与 `get` 请求、上传文件、 `cookie` 获取与响应。`404`处理。

3. 学会使用模板自动转义、定义过滤器、定义全局上下文处理器、`jinja2`语法、包含、继承、定义宏

4. 学会使用 `flask-wtf` 定义表单模型、字段定义、字段验证、视图处理表单、模板使用表单

5. 学会使用 `flask-sqlachemy` 定义数据库模型、添加数据、修改数据、查询数据、删除数据、数据库事件、数据迁移

6. 学会使用蓝图优化项目结构，实现微电影网站前台与后台业务逻辑。

7. 学会`flask`的部署方法、安装编译`nginx`服务、安装编译 `python3.6` 服务、安装 `mysql`服务以及通过`nginx`反向代理对视频流媒体限制下载速率、限制单个 `ip` 能发起的播放连接数

### 扩展插件

* `werkzug` 工具箱
* `pymysql` 数据库驱动
* `sqlalchemy` 数据库orm
* `wtforms` 表单验证工具
* `jinjia2` 模板引擎
* `flask-script` 命令行脚本
* `functools` 定义高阶函数

### 视频技术

- `jqplayer` 播放器插件
- 视频限速限`ip`访问
- `flv、mp4` 视频格式支持
- `nginx` 点播实现

## 开发流程

1. 介绍

	- 介绍微电影网站整体开发流程
	- `flask`简介
	- 需要掌握的知识点

2. 环境搭建与工具

	- 搭建开发环境安装依赖包、 `virtualenv` 虚拟化环境的使用
	- 编辑器的使用、介绍 `pip` 下载工具的使用

3. 项目优化与模型设计

	- 使用 `flask` 的蓝图 `Blueprint` 规划项目结构
	- 使用 `flask sqlalchemy` 定义和业务需求相关的数据库模型
	- 结合 `mysql`数据库生成数据表

4. 前端搭建

	- 前端后台HTML布局页面搭建
	- 学习 `jinjia2` 引擎语法
	- 引入静态资源文件、 `404` 错误页面的处理

5. 后台开发

	- `flask sqlalchemy`结合`mysql`数据表进行增删改查操作
	- `flask` 数据分页查询、 路由装饰器定义、模板中变量调用登陆会话机制、上传文件
	- `flask wtforms` 表单验证、 `flask` 自定义应用上下文、自定义权限装饰器对管理系统进行基于角色的访问控制
	- `flask` 的多表关联查询、关键字模糊查询等

6. 网站部署

	- 实现在`centos`服务器上搭建`nginx+mysql+python`环境
	- 使用`nginx`反向代理多端口多进程部署微电影网站
	- 配置`nginx`流媒体访问限制参数

### virtualenv 的使用及 falsk 的安装

1. virtualenv 的使用

```bash
pip instasll virtualenv 		# 1. 安装
virtualenv venv 				# 2. 创建虚拟化环境(执行成功后会出现一个venv的目录)
source venv/bin/activate 		# 3. 激活虚拟化环境(mac os/liunx/ubuntu)
venv\Scripts\activate 			# 3. 激活虚拟化环境(win cmd)
…………
deactivate 						# 4. 退出虚拟化环境
```

2. flask 的安装
```bash
(env) pip freeze 		# 安装前检测(查看当前安装了什么包)
(env) pip install flask # 安装flask  (pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com flask)
(env) pip freeze 		# 安装后检测(查看当前安装了什么包)
```

### 项目目录结构

	manage.py 			入口启动脚本
	app					项目app
	 │  __init__.py 	初始化文件
	 │  models.py 		数据模型文件
	 │
	 ├─static 			静态目录
	 ├─home 			前端目录
	 │  │  forms.py 	表单处理文件
	 │  │  views.py 	视图处理文件
	 │  │  __init__.py 	初始化脚本
	 │  │
	 ├─admin 			后端目录
	 │  │  forms.py 	表单处理文件
	 │  │  views.py 	视图处理文件
	 │  │  __init__.py 	初始化脚本
	 │  │
	 └─templates 		模板目录
	     └─home 		前端目录
	         └─admin  	后台模板

### 蓝图构建项目目录

* 什么是蓝图？

> 蓝图是一个应用中或跨应用制作应用组件和支持日通用的模式

* 蓝图的作用？

	- 将不同的功能模块化
	- 构建大型应用
	- 优化项目结构
	- 增强可读性，易于维护

* 蓝图使用流程


1、定义蓝图(`app/admin/__init__.py`)

```py
from flask import Blueprint
admin = Blueprint("admin",__name__)
import views
```

2、注册蓝图(`app/__init__.py`)

```py
from admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint,url_prefix="admin")
```

3、调用蓝图(`app/admin/views.py`)

```py
from . import admin
@admin.route("/")
```

### 会员及会员登录日志数据模型设计

1、 安装数据库连接依赖包

```bash
pip install flask-sqlalchemy
```

2、 定义`mysql`数据库连接

[Flask-SQLAlchemy详细配置](http://www.pythondoc.com/flask-sqlalchemy/config.html)
```py
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/movie" # 配置链接数据库的地址
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app) # 实例化
```

3、定义会员数据模型

```py
class User(db.Model):
	__tablename__ = "user" 		# 数据表的名称
	id = db.Column(db.Integer, primary_key = True) # id 是 整型，主键，自动递增
	name = db.Column(db.String)
	pwd  = db.Column(db.String)
	email  = db.Column(db.String)
	phone  = db.Column(db.String)
	info  = db.Column(db.Text) 		# 个人简介
	face  = db.Column(db.String)	# 用户头像
	addtime  = db.Column(db.DateTime, index = True, default = datetime.utcnow) 	# 注册时间
	uuid = db.Column(db.String) 	# 唯一标志符
```

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`name`			| 账号
|`pwd`			| 密码
|`email`		| 邮箱
|`phone`		| 手机号
|`info`			| 简介
|`face`			| 头像
|`addtime`		| 注册时间
|`uuid`			| 唯一标志符
|`comment`		| 评论外键关联
|`userlogs`		| 会员登录日志外键关联
|`moviecols`	| 电影收藏外键关联

定义会员登录日志数据模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`user_id`		| 所属会员编号
|`ip`			| 最近登录`ip`
|`addtime`		| 最近登录时间

### 标签、电影、 上映预告数据模型设计

定义标签数据模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`name`			| 标题
|`movies`		| 电影外键关联
|`addtime`		| 创建时间

定义电影数据模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`title`		| 电影标题
|`url`			| 电影地址
|`info`			| 电影简介
|`logo`			| 电影封面
|`star`			| 星级
|`playnum`		| 电影播放量
|`commentnum`	| 电影评论量
|`tag_id`		| 所属标签
|`area`			| 地区
|`release_time`	| 发布时间
|`length`		| 电影长度
|`addtimne`		| 添加时间
|`comments`		| 电影评论（外键关联）
|`moviecols`	| 电影收藏（外键关联）

定义上映预告数据模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`title`		| 上映预告标题
|`logo`			| 上映预告封面
|`addtime`		| 创建时间


### 评论及收藏电影数据模型设计

定义评论数据模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`content`		| 评论内容
|`movie_id`		| 所属电影(外键关联)
|`user_id`		| 所属用户(外键关联)
|`addtime`		| 最近登录时间

定义收藏电影模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`movie_id`		| 所属电影(外键关联)
|`user_id`		| 所属用户(外键关联)
|`addtime`		| 最近登录时间

### 权限及角色数据模型设计

定义权限数据模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`name`			| 名称
|`url`			| 地址
|`addtime`		| 最近登录时间

定义角色数据模型

|Column			| 注释
|---------------|----------------
|`id`			| 编号(整型，主键，自动递增)
|`name`			| 名称
|`auths`		| 权限列表
|`addtime`		| 创建时间
|`admins`		| 管理员外键关联


### 前端布局搭建

1、静态文件引入： `{{url_for('static', filename='文件路径')}}`
2、定义路由： `{{url_for('模块名.视图名', 变量=参数)}}`
2、定义数据块： `{% block 数据块名称 %}……{% endblock %}`

#### 会员登录页面搭建

登录

```py
@home.route("/login")
def login():
	return render_template("home/login.html")
```

退出

```py
@home.route("/logout/")
def logout():
	return redirect(url_for('home.login'))
```

#### 会员中心页面搭建


> 会员中心

`@home.route("/user/")`

> 修改密码

`@home.route("/pwd/")`

> 评论记录

`@home.route("/comments/")`

> 登录日志

`@home.route("/loginlog/")`

> 收藏电影

`@home.route("/moviecol/")`

#### 电影列表页面搭建


> 列表

```py
@home.route("/")
def index():
	return render_template("home/index.html")
```

> 动画

```py
@home.route("/animation/")
def animation():
	return redirect(url_for('home/animation.html'))
```

#### 电影詳情页面搭建

> 電影播放

```py
@home.route("/play")
def play():
	return render_template("home/play.html")
```


### 管理员登录页面搭建

> 登录

```py
@admin.route("/login")
def login():
	return render_template("admin/login.html")
```

> 退出

```py
@admin.route("/logout")
def logout():
	return render_template("admin.logout")
```

#### 后台布局搭建

> admin.html

```jinjia2
{% block css %} …… {% end %}
{% include "grid.html" %}
{% block content %} …… {% end %}
{% block js %} …… {% end %}
```

> admin.html

```jinjia2
{% extends "admin/admin.html" %}
{% block css %} …… {% end %}
{% include "grid.html" %}
{% block content %} …… {% end %}
{% block js %} …… {% end %}
```

#### 控制面板

> 系统管理

```py
@admin.route("/")
def index():
	return render_template("admin/index.html")
```

#### 标签管理页面的搭建

> 编辑标签

```py
@admin.route("/tag/add/")
def tag_add():
	return render_template("admin/tag_add.html")
```

> 编辑列表

```py
@admin.route("/tag/list/")
def tag_list():
	return render_template("admin/tag_list.html")
```


#### 电影管理页面搭建

> 编辑电影

```py
@admin.route("/movie/add/")
def movie_add():
	return render_template("admin/movie_add.html")
```

> 电影列表

```py
@admin.route("/movie/list/")
def movie_list():
	return render_template("admin/movie_list.html")
```

#### 电影預告页面搭建

> 编辑电影預告

```py
@admin.route("/movie/add/")
def movie_add():
	return render_template("admin/movie_add.html")
```

> 电影預告列表

```py
@admin.route("/movie/list/")
def movie_list():
	return render_template("admin/movie_list.html")
```

#### 会员页面搭建

> 会员列表

```py
@admin.route("/user/list/")
def user_add():
	return render_template("admin/user_add.html")
```

> 查看会员

```py
@admin.route("/user/view/")
def user_list():
	return render_template("admin/user_list.html")
```

#### 评论管理页面搭建

> 评论列表

```py
@admin.route("/comment/list/")
def comment_list():
	return render_template("admin/comment_list.html")
```

#### 电影收藏页面搭建

> 电影收藏

```py
@admin.route("/moviecol/list/")
def moviecol_list():
	return render_template("admin/moviecol_list.html")
```

#### 操作日志页面搭建

> 操作日志

```py
@admin.route("/oplog/list/")
def oplog_list():
	return render_template("admin/oplog_list.html")
```

> 管理员登录日志

```py
@admin.route("/adminloginlog/list/")
def adminloginlog_list():
	return render_template("admin/adminloginlog_list.html")
```

> 会员登录日志

```py
@admin.route("/userloginlog/list/")
def userloginlog_list():
	return render_template("admin/userloginlog_list.html")
```

#### 角色管理页面搭建

> 添加角色

```py
@admin.route("/role/add/")
def role_add():
	return render_template("admin/role_add.html")
```

> 角色列表

```py
@admin.route("/role/list/")
def role_list():
	return render_template("admin/role_list.html")
```

#### 权限管理页面搭建

> 添加权限

```py
@admin.route("/auth/add/")
def auth_add():
	return render_template("admin/auth_add.html")
```

> 权限列表

```py
@admin.route("/auth/list/")
def auth_list():
	return render_template("admin/auth_list.html")
```


#### 管理员管理页面搭建

> 添加管理员

```py
@admin.route("/admin/add/")
def admin_add():
	return render_template("admin/admin_add.html")
```

> 管理员列表

```py
@admin.route("/admin/list/")
def admin_list():
	return render_template("admin/admin_list.html")
```

### 管理员登陆


1. `app/__init__.py` 中创建db对象

2. `app/models.py` 中导入db对象

3. `app/admin/forms.py` 中定义表单验证

4. `app/templates/admin/login.html` 中使用表单字段，信息验证，消息闪现

5. `app/admin/views.py` 中处理登陆请求，保存会话

6. `app/admin/views.py` 定义登陆装饰器，访问控制

- 模型：`Admin`
- 表单：`LoginForm`
- 请求方法：`GET，POST`
- 访问控制：无

__标签管理__

- 模型： Tag
- 表单： TagForm
- 请求方法： GET、 POST
- 访问控制： @admin_login_req

__电影管理__

- 模型： Movie
- 表单： MovieForm
- 请求方法： GET、 POST
- 访问控制： @admin_login_req

__预告管理__

- 模型： Preview
- 表单： PreviewForm
- 请求方法： GET、 POST
- 访问控制： @admin_login_req

