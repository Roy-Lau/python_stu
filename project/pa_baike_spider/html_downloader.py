# coding:utf8
from urllib import request

class HtmlDownloader(object):
	""" html 下载器 """
	def download(self, url):
		if url is None:
			return None

		response = request.urlopen(url)
		if response.getcode() != 200:
			return None

		return response.read()
