from flask_wtf import FlaskForm
from wtforms import (TextAreaField, StringField, SubmitField, TelField, EmailField,
                      PasswordField, SelectField, DateField, RadioField, BooleanField)
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_btn = SubmitField('Login')

class RegistrationForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    email_address = EmailField(label='Email Address', validators=[DataRequired(), Email()])
    phone_number = TelField(label='Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password', 'password does not match')])
    submit_btn = SubmitField('Register')

class UserForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    email_address = EmailField(label='Email Address', validators=[DataRequired(), Email()])
    phone_number = TelField(label='Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=20)])
    submit_btn = SubmitField('Register')


class UpdateProfileForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[DataRequired()])
    last_name = StringField(label='Last Name', validators=[DataRequired()])
    email = EmailField(label='Email Address', validators=[DataRequired(), Email()])
    phone_number = TelField(label='Phone Number', validators=[DataRequired(), Length(min=10, max=10)])


class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField(label='Old Password', validators=[DataRequired(), Length(min=8, max=20)])
    new_password = PasswordField(label='New Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_new_password = PasswordField(label='Confirm New Password',
                                     validators=[DataRequired(),
                                                 EqualTo('new_password', 'password does not match')])
    submit_btn = SubmitField('Update')