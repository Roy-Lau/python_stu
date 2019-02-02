# -*- coding: utf-8 -*-

import requests

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

# 简单的例子
def use_simple_requests():
	response = requests.get(URL_IP)
	print('响应头： ')
	print(response.headers)
	print('响应体：')
	print(response.text)

def use_params_requests():
	# 构建请求参数
	params = {'param1':'hello','param2':'world'}
	# 发送请求
	response = requests.get(URL_GET,params=params)
	# 处理响应
	print('响应头：')
	print(response.headers)
	print('状态码：')
	print(response.status_code)
	print('响应体：')
	# print(response.text)
	print(response.json())






if __name__ == '__main__':
	print('>>>>>调用 use_simple_requests 函数')
	use_simple_requests()
	print('>>>>>调用 use_params_requests 函数')
	use_params_requests()
