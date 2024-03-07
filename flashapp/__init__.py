from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



app = Flask(__name__)

app.config['SECRET_KEY'] = 'sladjfk643kj24j2l6klj24'
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'


db_name = 'flash.db'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+ db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)

from flashapp import routes

with app.app_context():
	db.create_all()

