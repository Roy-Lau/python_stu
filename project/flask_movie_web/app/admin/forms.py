#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 18:28:11
# ==============================

from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskFrom):
    """管理员登录表单"""
    account = StringField(
            label = "账号",
            validators = [
                DataRequired("请输入账号")
                ],
            description = "账号",
            reder_kw = {
                    "class": "form-control",
                    "placeholder": "请输入账号！",
                    "required": "required"
                }
            )
    pwd = passwordField(
            label = "密码"，
            validators = [
                DataRequired("请输入密码！")
                ],
            description = "密码",
            reder_kw = {
                "class": "form-control",
                "placeholder": "请输入密码!",
                "required": "required"
                }
            )
    submit = SubmitField(
            '登录',
            reder_kw = {
                "class": "btn btn-primary btn-block btn-flat"
                }
            )
