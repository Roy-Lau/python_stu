#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app import app
from flask_script import Manager

manage = Manager(app)

if __name__ == "__main__":
    # manage.run()
	app.run()


# >>> from app import db
# >>> db.create_all()