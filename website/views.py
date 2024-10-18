from flask import Blueprint, abort, jsonify, render_template, request, redirect, session, url_for, flash
from flask_login import login_required, current_user
# from .models import SavedFinancialAid, User, FinancialAid
from . import db
from datetime import date, datetime
from .models import User
from .forms import UpdatePasswordForm, UpdateProfileForm
from werkzeug.security import generate_password_hash, check_password_hash


# courses
courses_list = [
    {"name": "Introduction to Python", "category": "Programming", "image_url": "https://via.placeholder.com/400x300", "price": "Free", "level": "Beginner"},
    {"name": "Web Development Basics", "category": "Web Development", "image_url": "https://via.placeholder.com/400x300", "price": "$49", "level": "Beginner"},
    {"name": "Data Science with Python", "category": "Data Science", "image_url": "https://via.placeholder.com/400x300", "price": "$99", "level": "Intermediate"},
    {"name": "Machine Learning 101", "category": "Artificial Intelligence", "image_url": "https://via.placeholder.com/400x300", "price": "$129", "level": "Intermediate"},
    {"name": "Digital Marketing", "category": "Marketing", "image_url": "https://via.placeholder.com/400x300", "price": "$79", "level": "Beginner"},
    {"name": "Graphic Design Essentials", "category": "Design", "image_url": "https://via.placeholder.com/400x300", "price": "$69", "level": "Beginner"},
    {"name": "Business Management", "category": "Business", "image_url": "https://via.placeholder.com/400x300", "price": "$89", "level": "Intermediate"},
    {"name": "Financial Analysis", "category": "Finance", "image_url": "https://via.placeholder.com/400x300", "price": "$109", "level": "Intermediate"},
    {"name": "Cybersecurity Basics", "category": "IT", "image_url": "https://via.placeholder.com/400x300", "price": "Free", "level": "Beginner"},
    {"name": "Ethical Hacking", "category": "IT", "image_url": "https://via.placeholder.com/400x300", "price": "$149", "level": "Advanced"},
    {"name": "Mobile App Development", "category": "Mobile Development", "image_url": "https://via.placeholder.com/400x300", "price": "$99", "level": "Intermediate"},
    {"name": "Blockchain Fundamentals", "category": "Blockchain", "image_url": "https://via.placeholder.com/400x300", "price": "$119", "level": "Advanced"},
]

views = Blueprint('views', __name__)

@views.route('/')
def index():
    print(current_user.__dict__)
    return render_template("index.html")

@views.route('/home')
@login_required
def home():
    print(current_user.__dict__)
    return render_template("home.html", user=current_user)

@views.route('/courses')
@login_required
def courses():
    return render_template("courses.html", courses=courses_list)


@views.route('/update_profile/<int:user_id>', methods=['GET', 'POST'])
def update_profile(user_id):
    user = User.query.get(user_id)
    form = UpdateProfileForm(obj=user)
    form2 = UpdatePasswordForm()
    if form.validate_on_submit():
        # Handle form submission and update the driver in the database
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.phone_number = form.phone_number.data

        db.session.commit()

        flash(f'User #{user._id} updated successfully!', 'success')
        return redirect(url_for('views.home'))
    print(form.errors)
    return render_template("update_profile.html", form=form, form2=form2, user=current_user)

@views.route('/update_password/<int:user_id>', methods=['GET', 'POST'])
def update_password(user_id):
    user = User.query.get(user_id)
    form = UpdatePasswordForm(obj=user)
    if form.validate_on_submit():
        if not check_password_hash(user.password, form.old_password.data):
            flash('Password provided is invalid.', category='error')
            return redirect(url_for('views.update_profile', user_id=current_user._id))
        if form.new_password.data != form.confirm_new_password.data:
            flash('New password does not match.', category='error')
            return redirect(url_for('views.update_profile', user_id=current_user._id))
        password=generate_password_hash(form.new_password.data, method='pbkdf2:sha256')
        # Handle form submission and update the user in the database
        user.password = password

        db.session.commit()

        flash(f'User #{user._id} updated successfully!', 'success')
        return redirect(url_for('views.home'))
    print(form.errors)
    return render_template("update_profile.html", form=form, user=current_user)


@views.route('/donor_signup')
def donor_signup():
    return render_template('donor_signup.html')