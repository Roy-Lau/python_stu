#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-09-06 11:12:25
# ==============================

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Email,Regexp,ValidationError
from app.models import User

class RegistForm(FlaskForm):
	"""会员注册表单"""
	name=StringField(
        label="昵称",
        validators=[
            DataRequired("请输入昵称！")
        ],
        description="昵称",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入昵称！",
            # "required": "required"
        }
    )
	email=StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱不正确")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入邮箱！",
            # "required": "required"
        }
    )
	phone=StringField(
	    label="手机",
	    validators=[
	        DataRequired("请输入手机！"),
	        Regexp("1[3458]\d{9}",message="手机格式不正确！")
	    ],
	    description="手机",
	    render_kw={
	        "class": "form-control input-lg",
	        "placeholder": "请输入手机！",
	        # "required": "required"
	    }
	)
	pwd=PasswordField(
	    label="密码",
	    validators=[
	        DataRequired("请输入密码！")
	    ],
	    description="密码",
	    render_kw={
	        "class": "form-control input-lg",
	        "placeholder": "请输入密码!",
	        # "required": "required"
	    }
	)
	repwd=PasswordField(
	    label="确认密码",
	    validators=[
	        DataRequired("请输入确认密码！"),
	        EqualTo('pwd',message="两次密码不一致!")
	    ],
	    description="确认密码",
	    render_kw={
	        "class": "form-control input-lg",
	        "placeholder": "请输入确认密码!",
	        # "required": "required"
	    }
	)
	submit=SubmitField(
	    "注册",
	    render_kw={
	        "class": "btn btn-lg btn-success btn-block"
	    }
	)

def validate_name(self,field):
	name = field.data
	user = User.query.filter_by(name=name).count()
	if user == 1:
		raise ValidationError("昵称已存在！")

def validate_email(self,field):
	email = field.data
	user = User.query.filter_by(email=email).count()
	if user == 1:
		raise ValidationError("邮箱已存在！")

def validate_phone(self,field):
	phone = field.data
	user = User.query.filter_by(phone=phone).count()
	if user == 1:
		raise ValidationError("手机号码已存在！")


class LoginForm(FlaskForm):
	"""登录表单"""
	name=StringField(
        label="账号",
        validators=[
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号！",
            # "required": "required"
        }
    )
	pwd=PasswordField(
	    label="密码",
	    validators=[
	        DataRequired("请输入密码！")
	    ],
	    description="密码",
	    render_kw={
	        "class": "form-control input-lg",
	        "placeholder": "请输入密码!",
	        # "required": "required"
	    }
	)
	submit=SubmitField(
	    "登录",
	    render_kw={
	        "class": "btn btn-lg btn-primary btn-block"
	    }
	)
