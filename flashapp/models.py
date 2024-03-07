from flashapp import db
from datetime import datetime
from flashapp import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	flash = db.relationship('Flash', backref="author", lazy=True)


	# def __init__(self, username, email, password):
	# 	self.username = username
	# 	self.email = email
	# 	self.password = password

class Flash(db.Model):
	__tablename__ = 'flash'
	id = db.Column(db.Integer, primary_key=True)
	front = db.Column(db.String)
	back = db.Column(db.String)
	date = db.Column(db.DateTime, default = datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



	# def __init__(self, front, back, user_id):
	# 	self.front = front
	# 	self.back = back
	# 	self.user_id = user_id
