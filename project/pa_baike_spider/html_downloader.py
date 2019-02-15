# coding:utf8
from urllib import request
from urllib.parse import quote
import string

class HtmlDownloader(object):
	""" html 下载器 """
	def download(self, url):
		if url is None:
			return None
		# 中文url转化成urlopen可以打开的格式
		s = quote(url,safe=string.printable)
		response = request.urlopen(s)
		if response.getcode() != 200:
			return None

		return response.read()
