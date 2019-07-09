# -*-encoding=utf-8-*-

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')
app.secret_key='kjl'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = '/regloginpage/'

from honor import views,models
