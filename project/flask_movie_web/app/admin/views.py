#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 18:28:11
# @discretion: 后台视图装饰器文件
# ==============================

from . import admin
from flask import render_template, redirect, url_for, flash, session, request, abort
from app.admin.forms import LoginForm, TagForm, MovieForm, PreviewForm, PwdForm, AuthForm, RoleForm, AdminForm
from app.models import Admin, Tag, Movie, Preview, User, Comment, Moviecol, Oplog, Adminlog, Userlog, Auth, Role
from functools import wraps
from app import db, app
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import uuid

# 登录权限装饰器
def admin_login_req(f):
	@wraps(f)
	def decorated_function(*args,**kwargs):
		# 如果`session`中没有`admin`，或者`session`的`admin`为`None`
		if "admin" not in session:
			flash("权限认证失败！","err")
			# 跳转到登录页，并获取到 要跳转的地址
			return redirect(url_for("admin.login", next=request.url))
		return f(*args, **kwargs)

	return decorated_function

# 定义权限控制装饰器
def admin_auth(f):
	@wraps(f)
	def decorate_function(*args, **kwargs):
		admin = Admin.query.join(
			Role
		).filter(
			Role.id == Admin.role_id,
			Admin.id == session["admin_id"]
		).first()
		print('\t Admin------------ 不能是None ',admin)
		# print(admin.auths)
		auths = admin.role.auths
		auths = list(map(lambda v: int(v), auths.split(",")))
		auth_list = Auth.query.all()
		urls = [v.url for v in auth_list for val in auths if val == v.id]
		rule = request.url_rule
		if str(rule) not in urls:
			abort(404)
		return f(*args, **kwargs)

	return decorate_function


# 修改文件名称
def change_filename(filename):
	fileinfo = os.path.splitext(filename)
	filename = datetime.now().strftime("%Y%m%d%H%M%S")+"-"+str(uuid.uuid4().hex)+fileinfo[-1]
	return filename

# 主页
@admin.route("/")
@admin_login_req
# @admin_auth
def index():
	return render_template("admin/index.html")
	# return "<center><h1>this is admin page</h1><a href='/'>to home</a></center>"

# 登录
@admin.route("/login/", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit(): # 提交时需要进行表单验证
		data = form.data
		admin = Admin.query.filter_by(name=data["account"]).first()
		if not admin.check_pwd(data["pwd"]):
			flash("密码错误！","err")
			return redirect(url_for("admin.login"))
		session["admin"] = data["account"]
		session["admin_id"] = admin.id
		adminlog = Adminlog(
		    admin_id=admin.id,
		    ip=request.remote_addr,
		)
		db.session.add(adminlog)
		db.session.commit()
		return redirect(request.args.get("next") or url_for("admin.index"))
	return render_template("admin/login.html", form=form )

# 退出
@admin.route("/logout/")
@admin_login_req
def logout():
	session.pop("admin", None)
	session.pop("admin_id", None)
	return redirect(url_for('admin.login'))

# 修改密码
@admin.route("/pwd/", methods=["GET","POST"])
@admin_login_req
def pwd():
	form = PwdForm()
	if form.validate_on_submit():
		data = form.data
		admin = Admin.query.filter_by(
			name=session["admin"]
		).first()
		from werkzeug.security import generate_password_hash
		admin.pwd = generate_password_hash(data["new_pwd"])
		db.session.add(admin)
		db.session.commit()
		flash("修改密码成功！","ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="修改密码%s" % data["name"]
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for("admin.logout"))
	return render_template('admin/pwd.html', form=form)

# 新增标签
@admin.route("/tag/add/", methods=["GET","POST"])
@admin_login_req
@admin_auth
def tag_add():
	form = TagForm()
	if form.validate_on_submit():
		data = form.data
		tag = Tag.query.filter_by(name=data["name"]).count()
		if tag == 1:
			flash("名称已经存在！","err")
			return redirect(url_for('admin.tag_add'))
		tag = Tag(name=data["name"])
		db.session.add(tag)
		db.session.commit()
		flash("添加标签成功！", "ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="添加标签%s" % data["name"]
		)
		db.session.add(oplog)
		db.session.commit()
		redirect(url_for('admin.tag_add'))
	return render_template("admin/tag_add.html", form=form)

# 标签列表
@admin.route("/tag/list/<int:page>/", methods=["GET"])
@admin_login_req
@admin_auth
def tag_list(page=None):
	if page is None:
		page = 1
	page_data = Tag.query.order_by(
			Tag.addtime.desc()
		).paginate(page=page, per_page=10)
	return render_template("admin/tag_list.html", page_data=page_data)

# 编辑标签
@admin.route("/tag/edit/<int:id>/", methods=["GET","POST"])
@admin_login_req
@admin_auth
def tag_edit(id=None):
	form = TagForm()
	tag = Tag.query.get_or_404(id)
	if form.validate_on_submit():
		data = form.data
		tag_count = Tag.query.filter_by(name=data["name"]).count()
		if tag.name != data["name"] and tag_count == 1:
			flash("名称已存在！", "err")
			return redirect(url_for("admin.tag_edit",id=id))
		tag = Tag(name=data["name"])
		tag.name = data["name"]
		db.session.add(tag)
		db.session.commit()
		flash("编辑标签成功！", "ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="编辑标签%s" % data["name"]
		)
		db.session.add(oplog)
		db.session.commit()
		redirect(url_for("admin.tag_edit",id=id))
	return render_template("admin/tag_edit.html", form=form, tag=tag)

# 删除标签
@admin.route("/tag/del/<int:id>/", methods=["GET"])
@admin_login_req
@admin_auth
def tag_del(id=None):
	tag = Tag.query.filter_by(id=id).first_or_404()
	db.session.delete(tag)
	db.session.commit()
	flash("删除标签成功！","ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="删除标签%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for('admin.tag_list', page=1))

# 新增電影
@admin.route("/movie/add/", methods=["GET","POST"])
@admin_login_req
def movie_add():
	form = MovieForm()
	if form.validate_on_submit():
		data = form.data
		title_count = Movie.query.filter_by(title=data["title"]).count()
		if title_count == 1:
			flash("片名已存在！", "err")
			return redirect(url_for('admin.movie_add'))

		# secure_filename： 保证文件的安全
		file_url = secure_filename(form.url.data.filename)
		file_logo = secure_filename(form.logo.data.filename)
		# 如果不存在 `UP_DIR`
		if not os.path.exists(app.config["UP_DIR"]):
			# 创建 `UP_DIR`
			os.makedirs(app.config["UP_DIR"])
			# 授权（可读，可写）
			os.chomd(app.config["UP_DIR"],"rw")
		# 修改文件名称，并赋值
		url = change_filename(file_url)
		logo = change_filename(file_logo)
		# 保存文件
		form.url.data.save(app.config["UP_DIR"]+url)
		form.logo.data.save(app.config["UP_DIR"]+logo)
		movie = Movie(
			title=data["title"],
			url=url,
			info=data["info"],
			logo=logo,
			star=int(data["star"]),
			playnum=0,
			commentnum=0,
			tag_id=int(data["tag_id"]),
			area=data["area"],
			release=data["release_time"],
			length=data["length"]
		)
		db.session.add(movie)
		db.session.commit()
		flash("添加电影成功！","ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="添加电影%s" % data["title"]
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for('admin.movie_add'))
	return render_template("admin/movie_add.html", form=form)

# 電影列表
@admin.route("/movie/list/<int:page>", methods=["GET"])
@admin_login_req
def movie_list(page=None):
	if page is None:
		page = 1
	# join: 将 Tag 表添加到 Movie 表中
	# filter: 多表查询，filter_by: 单表查询
	page_data = Movie.query.join(Tag).filter(
		Tag.id == Movie.tag_id
	).order_by(
		Movie.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/movie_list.html", page_data=page_data)

# 编辑电影
@admin.route("/movie/edit/<int:id>", methods=["GET","POST"])
@admin_login_req
def movie_edit(id=None):
	form = MovieForm()
	form.url.validators = []
	form.logo.validators = []
	movie = Movie.query.get_or_404(id)
	if request.method == "GET":
		# 返回
		form.info.data = movie.info
		form.tag_id.data = movie.tag_id
		form.star.data = movie.star

	if form.validate_on_submit():
		data = form.data
		movie_count = Movie.query.filter_by(title=data["title"]).count()
		if movie_count == 1 and movie.title == data["title"]:
			flash("片名已存在！","err")
			return redirect(url_for('admin.movie_edit', id=id))

		# 如果不存在 `UP_DIR`
		if not os.path.exists(app.config["UP_DIR"]):
			# 创建 `UP_DIR`
			os.makedirs(app.config["UP_DIR"])
			# 授权（可读，可写）
			os.chomd(app.config["UP_DIR"],"rw")
		# 如果修改了视频，从新命名，并保存！
		print("\t",form.url.data)
		if form.url.data != "":
			file_url = secure_filename(form.url.data.filename)
			movie.url = change_filename(file_url)
			form.url.data.save(app.config["UP_DIR"]+movie.url)
		# 如果修改了图片，从新命名，并保存！
		if form.logo.data != "":
			file_logo = secure_filename(form.logo.data.filename)
			movie.logo = change_filename(file_logo)
			form.logo.data.save(app.config["UP_DIR"]+movie.logo)

		# 修改
		movie.star = data["star"]
		movie.tag_id = data["tag_id"]
		movie.info = data["info"]
		movie.title = data["title"]
		movie.area = data["area"]
		movie.length = data["length"]
		movie.release = data["release_time"]
		db.session.add(movie)
		db.session.commit()
		flash("修改电影成功！", "ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="修改电影%s" % data["title"]
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for("admin.movie_edit",id=id))
	return render_template("admin/movie_edit.html", form=form, movie=movie)

# 删除电影
@admin.route("/movie/del/<int:id>", methods=["GET"])
@admin_login_req
def movie_del(id=None):
	movie = Movie.query.get_or_404(int(id))
	db.session.delete(movie)
	db.session.commit()
	flash("删除电影成功！","ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="删除电影id：%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for('admin.movie_list', page=1))

# 编辑電影預告
@admin.route("/preview/add/", methods=["GET","POST"])
@admin_login_req
def preview_add():
	form = PreviewForm()
	if form.validate_on_submit():
		data = form.data
		title_count = Preview.query.filter_by(title=data["title"]).count()
		if title_count == 1:
			flash("预告片名已存在！", "err")
			return redirect(url_for('admin.preview_add'))

		file_logo = secure_filename(form.logo.data.filename)
		# 如果不存在 `UP_DIR`
		if not os.path.exists(app.config["UP_DIR"]):
			# 创建 `UP_DIR`
			os.makedirs(app.config["UP_DIR"])
			# 授权（可读，可写）
			os.chomd(app.config["UP_DIR"],"rw")
		# 修改文件名称，并赋值
		logo = change_filename(file_logo)
		form.logo.data.save(app.config["UP_DIR"]+logo)
		preview = Preview(
			title = data["title"],
			logo = logo
		)
		db.session.add(preview)
		db.session.commit()
		flash("添加预告成功！","ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="添加预告%s" % data["title"]
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for('admin.preview_add'))
	return render_template("admin/preview_add.html", form=form)

# 電影預告列表
@admin.route("/preview/list/<int:page>", methods=["GET"])
@admin_login_req
def preview_list(page=None):
	if page is None:
		page = 1
	page_data = Preview.query.filter_by().order_by(
		Preview.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/preview_list.html",page_data=page_data)

# 编辑电影预告
@admin.route("/preview/edit/<int:id>", methods=["GET","POST"])
@admin_login_req
def preview_edit(id=None):
	form = PreviewForm()
	form.logo.validators = []
	preview = Preview.query.get_or_404(id)
	if request.method == "GET":
		form.title.data = preview.title
	if form.validate_on_submit():
		data = form.data
		title_count = Preview.query.filter_by(title=data["title"]).count()
		if title_count == 1:
			flash("预告片名已存在！", "err")
			return redirect(url_for('admin.preview_edit', id=id))
		# 如果修改了图片，从新命名，并保存！
		if form.logo.data != "":
			file_logo = secure_filename(form.logo.data.filename)
			preview.logo = change_filename(file_logo)
			form.logo.data.save(app.config["UP_DIR"]+preview.logo)
		preview.title = data["title"]
		db.session.add(preview)
		db.session.commit()
		flash("修改预告成功！","ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="修改预告%s" % data["title"]
		)
		db.session.add(oplog)
		db.session.commit()
		return redirect(url_for("admin.preview_edit", id=id))
	return render_template("admin/preview_edit.html", form=form, preview=preview)

# 删除电影预告
@admin.route("/preview/del/<int:id>", methods=["GET"])
@admin_login_req
def preview_del(id=None):
	preview = Preview.query.get_or_404(int(id))
	db.session.delete(preview)
	db.session.commit()
	flash("删除预告成功！","ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="删除预告%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for('admin.preview_list', page=1))

# 会员列表
@admin.route("/user/list/<int:page>", methods=["GET"])
@admin_login_req
def user_list(page=None):
	if page is None:
		page = 1
	page_data = User.query.order_by(
		User.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/user_list.html", page_data=page_data)

# 查看会员
@admin.route("/user/view/<int:id>", methods=["GET"])
@admin_login_req
def user_view(id=None):
	user = User.query.get_or_404(int(id))
	return render_template("admin/user_view.html", user=user)

# 删除会员
@admin.route("/user/del/<int:id>", methods=["GET"])
@admin_login_req
def user_del(id=None):
	user = User.query.get_or_404(int(id))
	db.session.delete(user)
	db.session.commit()
	flash("删除会员成功！","ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="删除预告%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for("admin.user_list", page=1))

# 评论列表
@admin.route("/comment/list/<int:page>", methods=["GET"])
@admin_login_req
def comment_list(page=None):
	if page is None:
		page = 1
	page_data = Comment.query.join(
		Movie,
		User
	).filter(
		Movie.id == Comment.movie_id,
		User.id == Comment.user_id
	).order_by(
		Comment.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/comment_list.html", page_data=page_data)

# 删除评论
@admin.route("/comment/del/<int:id>", methods=["GET"])
@admin_login_req
def comment_del(id=None):
	comment = Comment.query.get_or_404(int(id))
	db.session.delete(comment)
	db.session.commit()
	flash("删除评论成功！","ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="删除评论%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for("admin.comment_list", page=1))

# 电影收藏
@admin.route("/moviecol/list/<int:page>", methods=["GET"])
@admin_login_req
def moviecol_list(page=None):
	if page is None:
		page = 1
	page_data = Moviecol.query.join(
		Movie,
		User
	).filter(
		Movie.id == Moviecol.movie_id,
		User.id == Moviecol.user_id
	).order_by(
		Moviecol.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/moviecol_list.html", page_data=page_data)

# 删除收藏
@admin.route("/moviecol/del/<int:id>", methods=["GET"])
@admin_login_req
def moviecol_del(id=None):
	moviecol = Moviecol.query.get_or_404(int(id))
	db.session.delete(moviecol)
	db.session.commit()
	flash("删除收藏成功！","ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="删除收藏%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for("admin.moviecol_list", page=1))

# 操作日志
@admin.route("/oplog/list/<int:page>", methods=["GET"])
@admin_login_req
def oplog_list(page=None):
	if page is None:
		page = 1
	page_data = Oplog.query.join(
		Admin
	).filter(
		Admin.id == Oplog.admin_id
	).order_by(
		Oplog.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/oplog_list.html", page_data=page_data)

# 管理员登录日志
@admin.route("/adminloginlog/list/<int:page>", methods=["GET"])
@admin_login_req
def adminloginlog_list(page=None):
	if page is None:
		page = 1
	page_data = Adminlog.query.join(
		Admin
	).filter(
		Admin.id == Adminlog.admin_id
	).order_by(
		Adminlog.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/adminloginlog_list.html", page_data=page_data)

# 会员登录日志
@admin.route("/userloginlog/list/<int:page>", methods=["GET"])
@admin_login_req
def userloginlog_list(page=None):
	if page is None:
		page = 1
	page_data = Userlog.query.join(
		User
	).filter(
		User.id == Userlog.user_id
	).order_by(
		Userlog.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/userloginlog_list.html", page_data=page_data)

# 添加角色
@admin.route("/role/add/", methods=["GET","POST"])
@admin_login_req
def role_add():
	form = RoleForm()
	if form.validate_on_submit():
		data = form.data
		role = Role(
			name=data["name"],
			auths=",".join(map(lambda v:str(v), data["auths"]))
		)
		db.session.add(role)
		db.session.commit()
		flash("添加角色成功！","ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="添加角色%s" % data["name"]
		)
		db.session.add(oplog)
		db.session.commit()
	return render_template("admin/role_add.html", form=form)

# 角色列表
@admin.route("/role/list/<int:page>", methods=["GET"])
@admin_login_req
def role_list(page=None):
	if page is None:
		page = 1
	page_data = Role.query.order_by(
		Role.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/role_list.html", page_data=page_data)

# 编辑角色
@admin.route("/role/edit/<int:id>", methods=["GET","POST"])
@admin_login_req
def role_edit(id=None):
	form = RoleForm()
	role = Role.query.get_or_404(id)
	if request.method == "GET":
		auths = role.auths
		form.auths.data = list(map(lambda v: int(v), auths.split(",")))
	if form.validate_on_submit():
		data = form.data
		role.name = data["name"]
		role.auths = ",".join(map(lambda v:str(v), data["auths"]))
		db.session.add(role)
		db.session.commit()
		flash("修改角色成功！","ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="编辑角色%s" % id
		)
		db.session.add(oplog)
		db.session.commit()
	return render_template("admin/role_edit.html", form=form, role=role)

# 删除角色
@admin.route("/role/del/<int:id>", methods=["GET"])
@admin_login_req
def role_del(id=None):
	role = Role.query.filter_by(id=id).first_or_404()
	db.session.delete(role)
	db.session.commit()
	flash("删除角色成功", "ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="删除角色%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for("admin.role_list", page=1))

# 添加权限
@admin.route("/auth/add/", methods=["GET", "POST"])
@admin_login_req
def auth_add():
	form = AuthForm()
	if form.validate_on_submit():
		data = form.data
		auth = Auth(
			name=data["name"],
			url=data["url"]
		)
		db.session.add(auth)
		db.session.commit()
		flash("添加权限成功", "ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="添加权限%s" % data["name"]
		)
		db.session.add(oplog)
		db.session.commit()
	return render_template("admin/auth_add.html", form=form)

# 权限列表
@admin.route("/auth/list/<int:page>", methods=["GET"])
@admin_login_req
def auth_list(page=None):
	if page is None:
		page = 1
	page_data = Auth.query.order_by(
		Auth.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/auth_list.html", page_data=page_data)

# 权限编辑
@admin.route("/auth/edit/<int:id>", methods=["GET","POST"])
@admin_login_req
def auth_edit(id=None):
	form = AuthForm()
	auth = Auth.query.get_or_404(id)
	if form.validate_on_submit():
		data = form.data
		auth.url = data["url"]
		auth.name = data["name"]
		db.session.add(auth)
		db.session.commit()
		flash("权限编辑成功", "ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="权限编辑%s" % data["name"]
		)
		db.session.add(oplog)
		db.session.commit()
		redirect(url_for("admin.auth_edit", id=id))
	return render_template("admin/auth_edit.html", form=form, auth=auth)

# 权限删除
@admin.route("/auth/del/<int:id>", methods=["GET"])
@admin_login_req
def auth_del(id=None):
	auth = Auth.query.filter_by(id=id).first_or_404()
	db.session.delete(auth)
	db.session.commit()
	flash("删除权限成功", "ok")
	# 写入操作日志
	oplog = Oplog(
	    admin_id=session["admin_id"],
	    ip=request.remote_addr,
	    reason="权限删除%s" % id
	)
	db.session.add(oplog)
	db.session.commit()
	return redirect(url_for("admin.auth_list", page=1))

# 添加管理员
@admin.route("/admin/add/", methods=["GET","POST"])
@admin_login_req
def admin_add():
	form = AdminForm()
	from werkzeug.security import generate_password_hash
	if form.validate_on_submit():
		data = form.data
		admin = Admin(
			name=data["name"],
			pwd=generate_password_hash(data["pwd"]),
			role_id=data["role_id"],
			is_super=1
		)
		db.session.add(admin)
		db.session.commit()
		flash("添加管理员成功", "ok")
		# 写入操作日志
		oplog = Oplog(
		    admin_id=session["admin_id"],
		    ip=request.remote_addr,
		    reason="添加管理员%s" % data["name"]
		)
		db.session.add(oplog)
		db.session.commit()
	return render_template("admin/admin_add.html", form=form)

# 管理员列表
@admin.route("/admin/list/page", methods=["GET"])
@admin_login_req
def admin_list(page=None):
	if page is None:
		page = 1
	page_data = Admin.query.order_by(
		Admin.addtime.desc()
	).paginate(page=page, per_page=10)
	return render_template("admin/admin_list.html", page_data=page_data)

