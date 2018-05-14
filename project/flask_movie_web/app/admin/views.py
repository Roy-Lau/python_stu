#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 18:28:11
# ==============================

from . import admin
from flask import render_template, redirect, url_for, flash, session
from app.admin.forms import LoginForm
from app.models import Admin


@admin.route("/")
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
			print("\n ============",admin.check_pwd(data["pwd"]))
			flash("密码错误！")
			return redirect(url_for("admin.login"))
		session["admin"] = data["account"]
		return redirect(request.args.get("next") or url_for("admin.index"))
	return render_template("admin/login.html", form=form )


# 退出
@admin.route("/logout/")
def logout():
	return redirect(url_for('admin.login'))

# 修改密码
@admin.route("/pwd/")
def pwd():
	return redirect('admin/pwd.html')

# 编辑标签
@admin.route("/tag/add/")
def tag_add():
	return render_template("admin/tag_add.html")

# 编辑列表
@admin.route("/tag/list/")
def tag_lsit():
	return render_template("admin/tag_list.html")

# 编辑電影
@admin.route("/movie/add/")
def movie_add():
	return render_template("admin/movie_add.html")

# 電影列表
@admin.route("/movie/list/")
def movie_lsit():
	return render_template("admin/movie_list.html")

# 编辑電影預告
@admin.route("/preview/add/")
def preview_add():
	return render_template("admin/preview_add.html")

# 電影預告列表
@admin.route("/preview/list/")
def preview_lsit():
	return render_template("admin/preview_list.html")

# 会员列表
@admin.route("/user/list/")
def user_add():
	return render_template("admin/user_add.html")

# 查看会员
@admin.route("/user/view/")
def user_lsit():
	return render_template("admin/user_list.html")

# 评论列表
@admin.route("/comment/list/")
def comment_list():
	return render_template("admin/comment_list.html")

# 电影收藏
@admin.route("/moviecol/list/")
def moviecol_list():
	return render_template("admin/moviecol_list.html")

# 操作日志
@admin.route("/onlog/list/")
def onlog_list():
	return render_template("admin/onlog_list.html")

# 管理员登录日志
@admin.route("/adminloginlog/list/")
def adminloginlog_list():
	return render_template("admin/adminloginlog_list.html")

# 会员登录日志
@admin.route("/userloginlog/list/")
def userloginlog_list():
	return render_template("admin/userloginlog_list.html")

# 添加角色
@admin.route("/role/add/")
def role_add():
	return render_template("admin/role_add.html")

# 角色列表
@admin.route("/role/list/")
def role_list():
	return render_template("admin/role_list.html")

# 添加权限
@admin.route("/auth/add/")
def auth_add():
	return render_template("admin/auth_add.html")

# 权限列表
@admin.route("/auth/list/")
def auth_list():
	return render_template("admin/auth_list.html")

# 添加管理员
@admin.route("/admin/add/")
def admin_add():
	return render_template("admin/admin_add.html")

# 管理员列表
@admin.route("/admin/list/")
def admin_list():
	return render_template("admin/admin_list.html")

