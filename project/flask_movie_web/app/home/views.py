#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 18:28:44
# ==============================

from . import home
from flask import render_template, redirect, url_for


# 登录
@home.route("/login/")
def login():
	return render_template("home/login.html")


# 退出
@home.route("/logout/")
def logout():
	return redirect(url_for('home.login'))

# 注册
@home.route("/regist/")
def regist():
	return redirect(url_for('home/regist.html'))

# 会员中心
@home.route("/user/")
def user():
	return redirect(url_for('home/user.html'))

# 修改密码
@home.route("/pwd/")
def pwd():
	return redirect(url_for('home/pwd.html'))

# 评论记录
@home.route("/comments/")
def comments():
	return redirect(url_for('home/comments.html'))

# 登陆日志
@home.route("/loginlog/")
def loginlog():
	return redirect(url_for('home/loginlog.html'))

# 收藏电影
@home.route("/moviecol/")
def moviecol():
	return redirect(url_for('home/moviecol.html'))


# 首页
@home.route("/")
def index():
	# return render_template("home/index.html")
	return "<center><h1 style='color:blue;'>this is home page</h1><a href='/admin'>go admin</a></center>"


# 动画
@home.route("/animation/")
def animation():
	return redirect(url_for('home/animation.html'))

# 搜索
@home.route("/search/")
def search():
	return redirect(url_for('home/search.html'))


# 電影詳情
@home.route("/play/")
def play():
	return redirect(url_for('home/play.html'))


