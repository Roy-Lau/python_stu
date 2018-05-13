#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ==============================
# @Author:   RoyLau
# @Version:  1.0
# @DateTime: 2018-05-11 10:27:00
# ==============================

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABAE_URL'] = "mysql://root@toor139.199.99.154:3306/flask_movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


app = Flask(__name__)
app.debug = True

db = SQLAlchemy(app)


from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
