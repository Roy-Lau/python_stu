#             爬取豆瓣电影前250条数据

> 要爬取的网站：https://movie.douban.com/top250

```
pip install scrapy # 安装scrapy
scrapy startproject project_namne #  创建项目
cd project_name/spiders # 进入spiders文件
scrapy genspider douban_spiders movie.douban.com # 生成douban_spiders.py文件
```

#### project_name目录介绍

- scrapy.cfg 配置文件
- items.py 定义item数据结构的地方
- settings 设置文件
- middlewares.py 中间件