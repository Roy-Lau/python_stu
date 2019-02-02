# -*- coding: utf-8 -*-

# import urllib.request, urllib.parse
from urllib import request, parse

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

# 简单的例子
def use_simple_urllib():
	response = request.urlopen(URL_IP)
	print('响应头： ')
	print(response.info())
	print('响应体：')
	print(response.read().decode('utf-8'))

def use_params_urllib():
	# 构建请求参数
	params = parse.urlencode({'param1':'hello','param2':'world'})
	print('请求参数：')
	print(params)
	# 发送请求
	response = request.urlopen('?'.join([URL_GET,params]) )
	# 处理响应
	print('响应头：')
	print(response.info())
	print('状态码：')
	print(response.getcode())
	print('响应体：')
	print(response.read().decode('utf-8'))






if __name__ == '__main__':
	print('>>>>>调用 use_simple_urllib 函数')
	use_simple_urllib()
	print('>>>>>调用 use_params_urllib 函数')
	use_params_urllib()
