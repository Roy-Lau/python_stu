# coding:utf8


class UrlManager(object):
	""" url 管理器 """
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()

	# 添加 url
	def add_new_url(self, url):
		# url 如果为空的话不添加
		if url is None:
			return
		# url 是没有添加过的才 add
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)
	# 添加 url列表
	def add_new_urls(self, urls):
		# urls不为None，且长度等于0，返回
		if urls is None or len(urls) == 0:
			return
		# 遍历urls 添加url
		for url in urls:
			self.add_new_url(url)
	# 匹配 url
	def has_new_url(self):
		return len(self.new_urls) != 0
	# 获取 url
	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url
