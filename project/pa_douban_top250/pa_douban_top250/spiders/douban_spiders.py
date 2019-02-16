# -*- coding: utf-8 -*-
import scrapy
from pa_douban_top250.items import PaDoubanTop250Item


class DoubanSpidersSpider(scrapy.Spider):
	# 爬虫名字
    name = 'douban_spiders'
    # 爬取的域名
    allowed_domains = ['movie.douban.com']
    # 入口 url ，放入调度器中
    start_urls = ['https://movie.douban.com/top250']

    # scrapy 默认的解析方法
    def parse(self, response):
    	# 循环电影条目
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for li in movie_list:
        	# 将 item 文件导入进来
        	douban_item = PaDoubanTop250Item()
        	# 写详细的 xpath ，进行数据解析
        	douban_item['serial_number'] = li.xpath(".//div[@class='item']//em/text()").extract_first()
        	douban_item['movie_namne'] = li.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]//text()").extract_first()
        	contents = li.xpath(".//div[@class='info']/div[@class='bd']/p[1]//text()").extract()
        	# 多行的情况下进行数据的处理
        	for conts in contents:
        		cont = "".join(conts.split())
        		douban_item['introduce'] = cont
        	douban_item['star'] = li.xpath(".//span[@class='rating_num']/text()").extract_first()
        	douban_item['evaluate'] = li.xpath(".//div[@class='star']//span[4]/text()").extract_first()
        	douban_item['describe'] = li.xpath(".//p[@class='quote']/span/text()").extract_first()
        	# print(douban_item)
        	# 将数据 yield 到 pipelines，对数据进行清洗等操作
        	yield douban_item
        # 解析下一页规则
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
        	next_link = next_link[0]
        	yield scrapy.Request('https://movie.douban.com/top250'+next_link,callback=self.parse)
