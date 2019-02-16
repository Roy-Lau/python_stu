#             爬取豆瓣电影前250条数据

> 要爬取的网站：https://movie.douban.com/top250

```
pip install scrapy # 安装scrapy
scrapy startproject project_namne #  创建项目
cd project_name/spiders # 进入spiders文件
scrapy genspider douban_spiders movie.douban.com # 生成douban_spiders.py文件
scrapy crawl douban_spiders # 抓取数据（运行项目）
scrapy crawl douban_spiders -o output.json # 将抓取到的数据保存到 json 文件中
scrapy crawl douban_spiders -o output.csv # 将抓取到的数据保存到 csv（表格） 文件中
pip install pymongo # 安装MongoDB包
```

#### project_name目录介绍

- scrapy.cfg 配置文件
- items.py 定义item数据结构的地方
- settings 设置文件
- middlewares.py 中间件

> 注意事项：中间件定义完一定要在settings文件中启用