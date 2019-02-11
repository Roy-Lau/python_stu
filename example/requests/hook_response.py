# -*- coding: utf-8 -*-

import requests

def get_key_info(response,*args,**kwargs):
	""" 回调函数 """
	print(response.headers['Content-Type'])


if __name__ == '__main__':
	print("≥≥≥≥≥ 通过钩子函数打印出响应 headers ：")
	requests.get('https://api.github.com',hooks=dict(response=get_key_info))