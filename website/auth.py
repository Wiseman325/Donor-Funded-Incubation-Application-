from flask import Blueprint, render_template, request, flash, redirect, session, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm, RegistrationForm

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            """
            if user.email == "BursaryboostAdmin@gmail.com" and user.password == "BursaryboostAdmin":
                session['email'] = user.email
                # login_user(user, remember=True)
                flash('Logged in successfully as admin!', category='success')
                return redirect(url_for('views.admin'))"""
            if user.email == form.email.data:
                if check_password_hash(user.password, form.password.data):
                    flash('Logged in successfully!', category='success')
                    session['email'] = form.email.data
                    login_user(user, remember=True)
                    return redirect(url_for('views.home'))
                else:
                    flash('Incorrect password, try again.', category='error')
            else:
                flash('Email address not for registered user', category='error')
        else:
            flash('Invalid email address or password. try again.', category='error')
    print(505)
    return render_template("login.html", form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = RegistrationForm()

    if form.validate_on_submit():
        existing_email =    User.query.filter_by(email=form.email_address.data).first()
        if existing_email:
            flash('Email already exists!', category='error')
            return redirect(url_for('auth.sign_up'))

        if form.password.data != form.confirm_password.data:
            flash('Passwords do not match!', category='error')
            return redirect(url_for('auth.sign_up'))

        password=generate_password_hash(form.password.data, method='pbkdf2:sha256')
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email_address.data,
            phone_number=form.phone_number.data,
            password=password
        )


        db.session.add(new_user)
        db.session.commit()

        flash('Registration Successful!', category='success')
        return redirect(url_for('auth.login'))
    else:
        for _, msg in form.errors.items():
            flash(msg[0], category='error')
    return render_template('sign_up.html', form=form)
