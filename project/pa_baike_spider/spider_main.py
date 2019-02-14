# 入口文件
#
# 要爬取的页面 https://baike.baidu.com/item/Python/407313
#
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
	"""docstring for SpiderMain"""
	def __init__(self):
		# 调用 url管理器
		self.urls = url_manager.UrlManager()
		# 调用 html下载器
		self.downloader = html_downloader.HtmlDownloader()
		# 调用 html解析器
		self.parser = html_parser.HtmlParser()
		# 调用 html输出器
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			# try:
			new_url = self.urls.get_new_url()
			html_count = self.downloader.download(new_url)
			new_urls, new_data = self.parser.parse(new_url,html_count)
			self.urls.add_new_urls(new_urls)
			self.outputer.collect_data(new_data)

			# 大于 1000 条数据就不抓取了
			if count == 1000:
				break
			count = count + 1
			# except:
			# 	print("抓取失败！")
		# 将抓取的数据输出到HTML文件中
		self.outputer.output_html()


if __name__ == '__main__':
	root_url = "https://baike.baidu.com/item/Python/407313"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)

