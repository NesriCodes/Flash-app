from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

from flashapp.models import User


class Registration(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8, max=50), EqualTo('password')])
	submit = SubmitField('Sign up')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('user name taken please choose another one.')

	def validate_email(self, email):
		email = User.query.filter_by(email=email.data).first()
		if email:
			raise ValidationError('email name taken please choose another one.')

class Login(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=50)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')



class NewCard(FlaskForm):
	term = StringField('Term',
	 validators=[DataRequired()])
	definition = TextAreaField('Definition', 
		validators = [DataRequired()])
	submit = SubmitField('Done')



class UpdateUser(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('user name taken please choose another one.')

	def validate_email(self, email):
		if email.data != current_user.email:
			email = User.query.filter_by(email=email.data).first()
			if email:
				raise ValidationError('email name taken please choose another one.')

