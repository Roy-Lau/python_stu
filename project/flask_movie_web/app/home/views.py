#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 18:28:44
# ==============================

from . import home
from flask import render_template, redirect, url_for, flash, session, request
from app.home.forms import RegistForm,LoginForm,UserdetailForm,PwdForm
from app.models import User,Userlog
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from app import db,app
from datetime import datetime
from functools import wraps
import uuid
import os

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

# 修改文件名称
def change_filename(filename):
	fileinfo = os.path.splitext(filename)
	filename = datetime.now().strftime("%Y%m%d%H%M%S")+"-"+str(uuid.uuid4().hex)+fileinfo[-1]
	return filename

# 修改会员资料
@home.route("/user/",methods=["GET","POST"])
@user_login_req
def user():
	form = UserdetailForm()
	user = User.query.get(int(session["user_id"]))
	form.face.validators = []
	if request.method == "GET":
		form.name.data = user.name
		form.email.data = user.email
		form.phone.data = user.phone
		form.info.data = user.info
	if form.validate_on_submit():
		data = form.data
		file_face = secure_filename(form.face.data.filename)
		# 如果不存在 `FC_DIR`
		if not os.path.exists(app.config["FC_DIR"]):
			# 创建 `FC_DIR`
			os.makedirs(app.config["FC_DIR"])
			# 授权（可读，可写）
			os.chomd(app.config["FC_DIR"],"rw")
		# 修改文件名称，并赋值
		user.face = change_filename(file_face)
		form.face.data.save(app.config["FC_DIR"]+user.face)

		name_count = User.query.filter_by(name=data["name"]).count()
		email_count = User.query.filter_by(email=data["email"]).count()
		phone_count = User.query.filter_by(phone=data["phone"]).count()
		info_count = User.query.filter_by(info=data["info"]).count()
		if data["name"] != user.name and name_count == 1:
			flash("昵称已存在！","err")
			return redirect(url_for("home.user"))
		if data["email"] != user.email and email_count == 1:
			flash("邮箱已存在！","err")
			return redirect(url_for("home.user"))
		if data["phone"] != user.phone and phone_count == 1:
			flash("手机号已存在！","err")
			return redirect(url_for("home.user"))
		if data["info"] != user.info and info_count == 1:
			flash("简介已存在！","err")
			return redirect(url_for("home.user"))

		user.name = data["name"]
		user.email = data["email"]
		user.phone = data["phone"]
		user.info = data["info"]
		db.session.add(user)
		db.session.commit()
		flash("修改会员资料成功！","ok")
		return redirect(url_for("home.user"))
	return render_template("home/user.html",form=form,user=user)

# 修改密码
@home.route("/pwd/",methods=["GET","POST"])
@user_login_req
def pwd():
	form = PwdForm()
	if form.validate_on_submit():
		data = form.data
		user = User.query.filter_by(
			name=session["user"]
		).first()
		user.pwd = generate_password_hash(data["new_pwd"])
		db.session.add(user)
		db.session.commit()
		flash("修改密码成功！","ok")
		return redirect(url_for("home.logout"))
	return render_template('home/pwd.html', form=form)

# 评论记录
@home.route("/comments/")
@user_login_req
def comments():
	return redirect(url_for('home/comments.html'))

# 会员登陆日志
@home.route("/loginlog/<int:page>/",methods=["GET"])
@user_login_req
def loginlog(page=None):
	if page is None:
		page = 1
	page_data = Userlog.query.filter_by(
		user_id = int(session["user_id"])
	).order_by(
		Userlog.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template('home/loginlog.html', page_data=page_data)

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


