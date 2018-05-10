# Flask 框架知识

1. 学会使用整型、浮点型、路径型、字符串行正则表达式路由转换器

2. 学会使用 `post` 与 `get` 请求、上传文件、 `cookie` 获取与响应。`404`处理。

3. 学会使用模板自动转义、定义过滤器、定义全局上下文处理器、`jinja2`语法、包含、继承、定义宏

4. 学会使用 `flask-wtf` 定义表单模型、字段定义、字段验证、视图处理表单、模板使用表单

5. 学会使用 `flask-sqlachemy` 定义数据库模型、添加数据、修改数据、查询数据、删除数据、数据库事件、数据迁移

6. 学会使用蓝图优化项目结构，实现微电影网站前台与后台业务逻辑。

7. 学会`flask`的部署方法、安装编译`nginx`服务、安装编译 `python3.6` 服务、安装 `mysql`服务以及通过`nginx`反向代理对视频流媒体限制下载速率、限制单个 `ip` 能发起的播放连接数

### 扩展插件

* werkzug 工具箱
* pymysql 数据库驱动
* sqlalchemy 数据库orm
* wtforms 表单验证工具
* jinjia2 模板引擎
* flask-script 命令行脚本
* functools 定义高阶函数

### 视频技术

- jqplayer 播放器插件
- 视频限速限`ip`访问
- flv、mp4视频格式支持
- nginx 点播实现

## 开发流程

1. 介绍

	- 介绍微电影网站整体开发流程
	- flask简介
	- 需要掌握的知识点

2. 环境搭建与工具

	- 搭建开发环境安装依赖包、 `virtualenv` 虚拟化环境的使用
	- 编辑器的使用、介绍 pip 下载工具的使用

3. 项目优化与模型设计

	- 使用 flask 的蓝图 `Blueprint` 规划项目结构
	- 使用 `flask sqlalchemy` 定义和业务需求相关的数据库模型
	- 结合 `mysql`数据库生成数据表

4. 前端搭建

	- 前端后台HTML布局页面搭建
	- 学习 `jinjia2` 引擎语法
	- 引入静态资源文件、 404 错误页面的处理

5. 后台开发

	- `flask sqlalchemy`结合`mysql`数据表进行增删改查操作
	- flask 数据分页查询、 路由装饰器定义、模板中变量调用登陆会话机制、上传文件
	- `flask wtforms` 表单验证、 flask 自定义应用上下文、自定义权限装饰器对管理系统进行基于角色的访问控制
	- flask 的多表关联查询、关键字模糊查询等

6. 网站部署

	- 实现在`centos`服务器上搭建`nginx+mysql+python`环境
	- 使用`nginx`反向代理多端口多进程部署微电影网站
	- 配置 nginx 流媒体访问限制参数

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
(env) pip freeze # 安装前检测(查看当前安装了什么包)
(env) pip install flask  # 安装flask  (pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com flask)
(env) pip freeze # 安装后检测(查看当前安装了什么包)
```