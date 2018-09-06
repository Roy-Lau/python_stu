#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 18:28:44
# ==============================

from . import home
from flask import render_template, redirect, url_for, flash, session, request
from app.home.forms import RegistForm,LoginForm
from app.models import User,Userlog
from werkzeug.security import generate_password_hash
from app import db
from functools import wraps
import uuid

# 登录权限装饰器
def user_login_req(f):
	@wraps(f)
	def decorated_function(*args,**kwargs):
		# 如果`session`中没有`user`，或者`session`的`user`为`None`
		if "user" not in session:
			flash("权限认证失败！","err")
			# 跳转到登录页，并获取到 要跳转的地址
			return redirect(url_for("home.login", next=request.url))
		return f(*args, **kwargs)

	return decorated_function

# 登录
@home.route("/login/",methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		data = form.data
		user = User.query.filter_by(name=data["name"]).first()
		if not user.check_pwd(data["pwd"]):
			flash("密码错误","err")
			return redirect(url_for("home.login"))
		session["user"] = user.name
		session["user_id"] = user.id
		userlog = Userlog(
			user_id = user.id,
			ip = request.remote_addr
		)
		db.session.add(userlog)
		db.session.commit()
		return redirect(url_for("home.user"))
	return render_template("home/login.html",form=form)

# 退出
@home.route("/logout/")
def logout():
	session.pop("user",None)
	session.pop("user_id",None)
	return redirect(url_for('home.login'))

# 会员注册
@home.route("/regist/",methods=["GET","POST"])
def regist():
	form = RegistForm()
	if form.validate_on_submit():
		data = form.data
		user = User(
			name=data["name"],
			email=data["email"],
			phone=data["phone"],
			pwd=generate_password_hash(data["pwd"]),
			uuid=uuid.uuid4().hex
		)
		db.session.add(user)
		db.session.commit()
		flash("注册成功！","ok")
	return render_template("home/regist.html",form=form)

# 会员中心
@home.route("/user/")
@user_login_req
def user():
	return redirect(url_for('home/user.html'))

# 修改密码
@home.route("/pwd/")
@user_login_req
def pwd():
	return redirect(url_for('home/pwd.html'))

# 评论记录
@home.route("/comments/")
@user_login_req
def comments():
	return redirect(url_for('home/comments.html'))

# 登陆日志
@home.route("/loginlog/")
@user_login_req
def loginlog():
	return redirect(url_for('home/loginlog.html'))

# 收藏电影
@home.route("/moviecol/")
@user_login_req
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


