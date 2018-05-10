#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Blueprint

admin = Blueprint("admin", __name__)

import app.admin.views
