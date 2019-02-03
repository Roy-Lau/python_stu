# -*- coding: utf-8 -*-

import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_point):
	return '/'.join([BASE_URL,end_point])

def basic_auth():
	""" auth 认证 """
	r = requests.get(construct_url('user'),auth=('imoocdemo','imoocdemo123'))
	print(r.request.headers)

def basic_oauth():
	""" oauth 认证 """
	headers = {'Authorization':'Basic aW1vb2NkZW1vOmltb29jZGVtbzEyMw=='}
	r = requests.get(construct_url('user/emails'),headers=headers)
	print(r.status_code)
	print(r.request.headers)
	print(r.text)


from requests.auth import AuthBase

class GithubAuth(AuthBase):
	"""docstring for GithubAuth"""
	def __init__(self, token):
		self.token = token
	def __call__(self,r):
		# 给 requests加入headers信息
		r.headers['Authorization'] = ' '.join(['Basic',self.token])
		return r

def oauth_advanced():
	""" oauth 通过面向对象的方式认证 """
	auth = GithubAuth('aW1vb2NkZW1vOmltb29jZGVtbzEyMw==')
	r = requests.get(construct_url('user/emails'),auth=auth)
	print(r.status_code)
	print(r.request.headers)
	print(r.text)



if __name__ == '__main__':
	print("≥≥≥≥≥ http auth 认证：")
	basic_auth()
	print("≥≥≥≥≥ http oauth 认证：")
	basic_oauth()
	print("≥≥≥≥≥ http oauth 认证(面向对象)：")
	oauth_advanced()



