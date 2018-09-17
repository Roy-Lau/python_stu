#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 18:28:44
# ==============================

from . import home
from flask import render_template, redirect, url_for, flash, session, request, Response
from app.home.forms import RegistForm,LoginForm,UserdetailForm,PwdForm,CommentForm
from app.models import User,Userlog,Preview,Tag,Movie,Comment,Moviecol
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from app import db, app, rd
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
			flash("权限认证失败，请登录！","err")
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
	flash("已退出！","ok")
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
@home.route("/comments/<int:page>")
@user_login_req
def comments(page=None):
	if page is None:
		page = 1
	page_data = Comment.query.join(
		Movie,
		User
	).filter(
		Movie.id == Comment.movie_id,
		User.id == session["user_id"]
	).order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template('home/comments.html',page_data=page_data,)

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

# 添加收藏电影
@home.route("/moviecol/add/",methods=["GET"])
@user_login_req
def moviecol_add():
	uid = request.args.get("uid","")
	mid = request.args.get("mid","")
	moviecol = Moviecol.query.filter_by(
		user_id=int(uid),
		movie_id=int(mid)
	).count()
	if moviecol == 1:
		data = dict(ok=0)

	if moviecol ==0:
		moviecol = Moviecol(
			user_id=int(uid),
			movie_id=int(mid)
		)
		db.session.add(moviecol)
		db.session.commit()
		data = dict(ok=1)
	import json
	return json.dumps(data)

# 收藏电影
@home.route("/moviecol/<int:page>")
@user_login_req
def moviecol(page=None):
	if page is None:
		page = 1
	page_data = Moviecol.query.join(
		Movie,
		User
	).filter(
		Movie.id == Moviecol.movie_id,
		User.id == session["user_id"]
	).order_by(
		Moviecol.addtime.desc()
	).paginate(page=page,per_page=10)
	return render_template("home/Moviecol.html",page_data=page_data)


# 首页
@home.route("/<int:page>/",methods=["GET"])
def index(page=1):
	tags = Tag.query.all()
	page_data = Movie.query
	#标题id
	tid = request.args.get("tid",0)
	if int(tid) != 0:
		page_data = page_data.filter_by(tag_id=int(tid))
	#星级
	star = request.args.get("star",0)
	if int(star) != 0:
		page_data = page_data.filter_by(star=int(star))
	# 上映时间
	time = request.args.get("time",0)
	if int(time) != 0:
		if int(time) == 1:
			page_data = page_data.order_by(Movie.addtime.desc())
		else:
			page_data = page_data.order_by(Movie.addtime.asc())
	# 播放数量
	pm = request.args.get("pm",0)
	if int(pm) != 0:
		if int(pm) == 1:
			page_data = page_data.order_by(Movie.playnum.desc())
		else:
			page_data = page_data.order_by(Movie.playnum.asc())
	# 评论数量
	cm = request.args.get("cm",0)
	if int(cm) != 0:
		if int(cm) == 1:
			page_data = page_data.order_by(Movie.commentnum.desc())
		else:
			page_data = page_data.order_by(Movie.commentnum.asc())
	# 页码
	if page is None:
		page = 1
	# 分页
	page_data = page_data.paginate(page=int(page),per_page=10)
	# 将参数做成字典 返回，方便前端处理
	p = dict(
		tid=tid,
		star=star,
		time=time,
		pm=pm,
		cm=cm
	)
	return render_template("home/index.html",tags=tags,p=p,page_data=page_data)
	# return "<center><h1 style='color:blue;'>this is home page</h1><a href='/admin'>go admin</a></center>"


# 动画(上映预告)
@home.route("/animation/")
def animation():
	data = Preview.query.all()
	return render_template('home/animation.html', data=data)

# 搜索
@home.route("/search/<int:page>/")
def search(page=None):
	if page is None:
		page = 1
	key = request.args.get("key","")
	movie_count = Movie.query.filter(
		Movie.title.ilike('%' + key + '%')
	).count()
	page_data = Movie.query.filter(
		Movie.title.ilike('%' + key +'%')
	).order_by(
		Movie.addtime.desc()
	).paginate(page=page, per_page=10)
	page_data.key = key
	return render_template("home/search.html",movie_count=movie_count,key=key,page_data=page_data)


# 電影詳情
@home.route("/play/<int:id>/<int:page>",methods=["GET","POST"])
# @user_login_req
def play(id=None,page=None):
	movie = Movie.query.join(Tag).filter(
			Tag.id == Movie.tag_id,
			Movie.id == int(id)
		).first_or_404()
	# 评论列表
	if page is None:
		page = 1
	page_data = Comment.query.join(
		Movie,
		User
	).filter(
		Movie.id == movie.id
	).order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	movie.playnum = movie.playnum +1
	form = CommentForm()
	# 评论
	if "user" in session and form.validate_on_submit():
		data = form.data
		comment = Comment(
			content = data["content"],
			movie_id = movie.id,
			user_id = session["user_id"]
		)
		db.session.add(comment)
		db.session.commit()
		movie.commentnum = movie.commentnum +1
		db.session.add(movie)
		db.session.commit()
		flash("评论添加成功","ok")
		return redirect(url_for("home.play",id=movie.id,page=1))
	db.session.add(movie)
	db.session.commit()
	return render_template("home/play.html",movie=movie,form=form,page_data=page_data)


# 電影视频
@home.route("/video/<int:id>/<int:page>",methods=["GET","POST"])
def video(id=None,page=None):
	movie = Movie.query.join(Tag).filter(
			Tag.id == Movie.tag_id,
			Movie.id == int(id)
		).first_or_404()
	# 评论列表
	if page is None:
		page = 1
	page_data = Comment.query.join(
		Movie,
		User
	).filter(
		Movie.id == movie.id
	).order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	movie.playnum = movie.playnum +1
	form = CommentForm()
	# 评论
	if "user" in session and form.validate_on_submit():
		data = form.data
		comment = Comment(
			content = data["content"],
			movie_id = movie.id,
			user_id = session["user_id"]
		)
		db.session.add(comment)
		db.session.commit()
		movie.commentnum = movie.commentnum +1
		db.session.add(movie)
		db.session.commit()
		flash("评论添加成功","ok")
		return redirect(url_for("home.video",id=movie.id,page=1))
	db.session.add(movie)
	db.session.commit()
	return render_template("home/video.html",movie=movie,form=form,page_data=page_data)


# 電影弹幕
@home.route("/tm/",methods=["GET","POST"])
def tm():
	import json
	if request.method == "GET":
		# 获取弹幕消息队列
		id = request.args.get("id")
		key = "movie" + str(id)
		if rd.llen(key):
			msgs = rd.lrange(key, 0, 2999)
			res = {
				"code": 1,
				"danmaku": [json.loads(v) for v in msgs]
			}
		else:
			res = {
				"code": 1,
				"danmaku": []
			}
		resp = json.dumps(res)
	if request.method == "POST":
		data = json.loads(request.get_data())
		msg = {
			"__v" : 0,
			"author": data["author"],
			"time": data["time"],
			"text": data["text"],
			"color": data["color"],
			"type": data["type"],
			"ip": request.remote_addr,
			"_id": datetime.now().strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex,
			"player": [
				data["player"]
				]
		}
		res = {
			"code": 1,
			"data": msg
		}
		resp = json.dumps(res)
		# 放到Redis中
		rd.lpush("movie" + str(data["player"]), json.dumps(msg))
	return Response(resp, mimetype='application/json')