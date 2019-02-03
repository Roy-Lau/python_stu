# -*- coding: utf-8 -*-

import requests

def dowload_img():
	""" 下载图片 （下载图片后未关闭连接）"""
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}
	img_url = "http://img5.imgtn.bdimg.com/it/u=2581445340,2068113219&fm=26&gp=0.jpg"
	r = requests.get(img_url,headers=headers,stream=True)
	print(r.status_code,r.reason)
	# print(r.headers)
	# 存放图片
	with open('demo.jpg','wb') as f:
		for chunk in r.iter_content(128):
			f.write(chunk)


def dowload_img_improved():
	""" 下载图片 下载后关闭连接"""
	# 伪造 headers信息
	headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36"}
	img_url = "http://img5.imgtn.bdimg.com/it/u=2581445340,2068113219&fm=26&gp=0.jpg"
	# 发送请求
	r = requests.get(img_url,headers=headers,stream=True)
	print(r.status_code,r.reason)
	from contextlib import closing
	with closing(requests.get(img_url,headers=headers,stream=True)) as r:
		# 打开文件
		with open('demo_closing.jpg','wb') as f:
			# 每 128 写入一次
			for chunk in r.iter_content(128):
				f.write(chunk)

if __name__ == '__main__':
	print("≥≥≥≥≥下载图片：")
	dowload_img()
	print("≥≥≥≥≥下载图片并关闭连接：")
	dowload_img_improved()