#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 10:27:00
# ==============================

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:toor@139.199.99.154:3306/flask_movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SECRET_KEY"] = "1ce3ada741844f90ab3e2a3a24221d11"
app.debug = True
db = SQLAlchemy(app)


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
