# -*- coding: utf-8 -*-

import requests,json
from requests import exceptions

URL = 'https://api.github.com'

# 构建 uri
def build_uri(endpoint):
	return '/'.join([URL,endpoint])

# 格式化输出（传入一个json字符串，返回格式化的json数据，缩进为4）
def better_print(json_str):
	return json.dumps(json.loads(json_str),indent=4)


# 请求方法
# 接口文档 https://developer.github.com/v3/users/
def request_method(last_uri):
	response = requests.get(build_uri(last_uri),auth=('imoocdemo','imoocdemo123'))
	print(better_print(response.text))
	# for data in response.json():
		# print(data['email'])
		# res = requests.delete(build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),json={"emails":[data['email']]}) # 删除邮箱
		# print(better_print(res.text))

# 参数请求
def params_request():
	response = requests.get(build_uri('users'),params={'since':11})
	print('响应 headers：')
	print(response.request.headers)
	print('响应 url：')
	print(response.url)
	print(better_print(response.text))

# json 请求
def json_request():
	# jsons = {'name':'babymooc12','email': 'hello-world@imooc.org'}
	# response = requests.patch(build_uri('user'),auth=('imoocdemo','imoocdemo123'),json=jsons)
	response = requests.post(build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),json=['admin@imooc.org']) # 给用户新增邮箱
	print(better_print(response.text))
	print(response.request.headers)
	print(response.request.body)
	print(response.status_code)

# 封装 requests
def hard_request():
	from requests import Request, Session
	s = Session()
	headers = {'User-Agent':'fake1.3.4'}
	# 请求
	req = Request('GET',build_uri('user/emails'),auth=('imoocdemo','imoocdemo123'),headers=headers)
	prepped = req.prepare()
	print(prepped.body)
	print(prepped.headers)

	# 响应
	res = s.send(prepped,timeout=5)
	print(res.status_code)
	print(res.request.headers)
	print(res.text)

# 超时请求
def timeout_request():
	try:
		response = requests.get(build_uri('user/emails'), timeout=0.1)
	except exceptions.Timeout as e:
		print('响应超时：')
		print(e.message)
	except exceptions.HTTPError as e:
		print('网络错误：')
		print(e.message)
	else:
		print(response.text)
		print(response.status_code)




if __name__ == '__main__':
	# print('>>>>> get: github imoocdemo 用户信息：')
	# request_method('users/imoocdemo')
	# print('>>>>> get: github imoocdemo 用户邮箱：')
	# request_method('user/emails')
	# print('>>>>> get: github 用户列表：')
	# params_request()
	# print('>>>>> patch or post: 修改 github 用户信息：')
	# json_request()
	print('>>>>> 封装 requests：')
	hard_request()
	# print('>>>>> 超时请求(处理异常)：')
	# timeout_request()