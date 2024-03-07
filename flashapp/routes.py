from flask import render_template, request, redirect, flash, url_for, abort
from flashapp.models import User, Flash
from flashapp.form import NewCard, Registration, Login, UpdateUser
from flashapp import app
from flask_login import login_required,current_user, login_user, logout_user
import random
from sqlalchemy import desc
from flashapp import bcrypt
from flashapp import db


@app.route("/")
@login_required
def home():
	flashes = Flash.query.order_by(desc(Flash.date)).all()
	return render_template('home.html', flashes = flashes)

@app.route("/new-card", methods=['GET', 'POST'])
@login_required
def new_card():
	form = NewCard()
	if form.validate_on_submit():
		# front = request.form.data
		# back = request.form['definition']

		record = Flash(front=form.term.data, back=form.definition.data, author=current_user)

		db.session.add(record)
		db.session.commit()

		flash(f'Card Created!', 'success')
		return redirect(url_for('home'))

	return render_template('new_form.html', form=form)

@app.route("/study")
@login_required
def study():
	page = request.args.get('page', 1, type=int)
	flashes = Flash.query.order_by(desc(Flash.date)).paginate(page = page, per_page=1)
	next_url = url_for('study', page=flashes.next_num) 
	prev_url = url_for('study', page=flashes.prev_num) 


	return render_template('study.html', flashes = flashes, next_url=next_url, prev_url=prev_url, page=page)


@app.route('/card/<int:flash_id>/update', methods=['GET', 'POST'])
@login_required
def update_card(flash_id):
	flashes = Flash.query.get_or_404(flash_id)

	form = NewCard()
	if form.validate_on_submit():
		flashes.front = form.term.data
		flashes.back = form.definition.data

		db.session.commit()

		flash(f'Card Updated!', 'success')
		return redirect(url_for('home'))
	elif request.method == 'GET':
		form.term.data = flashes.front
		form.definition.data = flashes.back

	return render_template('new_form.html', flashes = flashes, form=form)


@app.route("/register", methods=['GET', 'POST'])
def registration():
	form = Registration()

	if form.validate_on_submit():

		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

		user = User(username=form.username.data, email=form.email.data, password=hashed_password)

		db.session.add(user)
		db.session.commit()


		flash(f'Your account has been created! you are able to login now', 'success')
		return redirect(url_for('login'))

	return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = Login()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user)
			next_page = request.args.get('next')
			# login_user(user, remember=form.remember.data)
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check email and password', 'danger')

	return render_template('login.html', form=form)

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


@app.route('/profile')
def profile():
	return render_template('profile.html')


@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
	form = UpdateUser()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your account has been updated', 'success')
		return redirect(url_for('profile'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	return render_template('update_profile.html', form=form)



@app.route('/card/<int:flash_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_card(flash_id):
	flashes = Flash.query.get_or_404(flash_id)

	if flashes.user_id == current_user.id:
		db.session.delete(flashes)

		db.session.commit()

		flash(f'Card deleted!', 'success')
		return redirect(url_for('home'))

	else:
		flash(f'Card you can not access this page', 'success')
		return redirect(url_for('home'))


	return render_template('delete_card.html', flashes = flashes)
