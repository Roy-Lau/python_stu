#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABAE_URL'] = "mysql://root@toor139.199.99.154:3306/flask_movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

# 会员（用户）
class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True) 		# id 是 整型，主键，自动递增
	name = db.Column(db.String(100), unique=True) 		# 长度100，字段唯一
	pwd  = db.Column(db.String(100))
	email  = db.Column(db.String(100), unique=True)
	phone  = db.Column(db.String(11), unique=True)
	info  = db.Column(db.Text) 							# 个人简介
	face  = db.Column(db.String(255), unique=True)		# 用户头像
	addtime  = db.Column(db.DateTime, index = True, default = datetime.utcnow) 	# 注册时间
	uuid = db.Column(db.String(255), unique=True) 		# 唯一标志符

	def __repr__(self):
		return "<User %r>" % self.name

# 会员登录日志
class Userlog(db.Model):
	__tablename__ = "userlog"
	id = db.Column(db.Integer, primary_key=True) 		# id 是 整型，主键，自动递增