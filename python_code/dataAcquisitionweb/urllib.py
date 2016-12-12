#!/usr/bin/python
# -*- coding: UTF-8 -*-

from urllib3.request import urlopen

resp = request.urlopen("http://www.baidu.com")
print(resp.read().decode("UTF-8"))
