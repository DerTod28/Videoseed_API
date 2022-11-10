from gevent import monkey
monkey.patch_all()

from flask_app.app import app
