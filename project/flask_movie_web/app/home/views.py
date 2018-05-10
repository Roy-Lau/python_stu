#!/usr/bin/python
# -*- coding: UTF-8 -*-

from . import home

@home.route("/")
def index():
	return "<center><h1 style='color:blue;'>this is home page</h1><a href='/admin'>go admin</a></center>"