import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ababu1'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQL_DATABASE_URI'] = 'sqlite:///'+ os.path(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = flask_migrate

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(db)
login_manager.login_view = 'login'