#!/usr/bin/python
# -*- coding: UTF-8 -*-

from . import admin

@admin.route("/")
def index():
	return "<center><h1>this is admin page</h1><a href='/'>to home</a></center>"