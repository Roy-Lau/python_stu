# Request 学习

> 课程大纲

- 总体介绍
- HTTP 基本原理
- 发送请求（request）
- 接收响应（response）
- 进阶话题

#### 认识Requests类库

- 文档地址： http://docs.python-requests.org/zh_CN/latest/
- 作者(Kenneth Reitz):  http://www.kennethreitz.org/

### 准备工具

- python
- pip
- virtualenv （用来构建虚拟环境）
- requests库（请求数据）
- httpbin （ http://httpbin.org 服务器端）
- urllib

- 'requests[socksv5]'

### 了解http协议

- HyperText transfer Protocol 超文本传输协议

  无状态，分布式，协作式，超文本信息系统

- [简单的urlib_demo](./urllib_demo.py)
- [简单的requests_demo](./requests_demo.py)

### 调用 github API

URL： https://developer.github.com/

请求方法：

- GET：   查看资源
- POST:   增加资源
- PUT:    修改资源
- DELETE: 删除资源
- HEAD：   查看响应

#### [下载文件](./dowload_response.py)
#### [响应钩子](./hook_response.py)
#### [http认证](./http_authen.py)
#### 代理
#### session和cookie


- OPTIONS： 查看可用请求方法