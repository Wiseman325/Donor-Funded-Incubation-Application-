from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date, datetime
from sqlalchemy import Column, Date, DateTime, String, Integer, Text
import os
from werkzeug.utils import secure_filename


class User(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone_number = db.Column(db.String(15))
    password = db.Column(db.String(150))
    gender = db.Column(db.String(150))
    id_number = db.Column(db.String(13))
    age = db.Column(db.Integer)
    status = db.Column(db.String(150))
    certified_id_document = db.Column(db.String(255))
    matric_statement = db.Column(db.String(255))
    cv = db.Column(db.String(255))
    other_supporting_documents = db.Column(db.String(255))
    # course_id = db.Column(db.Integer, db.ForeignKey('course._id'), nullable=False)


    def get_id(self):
        return str(self._id)

    def upload_file(self, field_name, file):
        file_ext = os.path.splitext(file.filename)[1]
        filename = secure_filename(field_name + '_' + str(self.id) + file_ext)
        filepath = os.path.join('website/static/uploads', filename)
        file.save(filepath)
        setattr(self, field_name, filename)

    def upload_certified_id_document(self, file):
        self.upload_file('certified_id_document', file)

    def upload_matric_statement(self, file):
        self.upload_file('matric_statement', file)

    def upload_cv(self, file):
        self.upload_file('cv', file)

    def upload_other_supporting_documents(self, file):
        self.upload_file('other_supporting_documents', file)

    def delete_file(self, field_name):
        filepath = os.path.join('app/static/uploads', getattr(self, field_name))
        if os.path.isfile(filepath):
            os.remove(filepath)
        setattr(self, field_name, None)

    def delete_certified_id_document(self):
        self.delete_file('certified_id_document')

    def delete_matric_statement(self):
        self.delete_file('matric_statement')

    def delete_cv(self):
        self.delete_file('cv')

    def delete_other_supporting_documents(self):
        self.delete_file('other_supporting_documents')

"""
class Course(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80))
    duration = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    # students = db.relationship('User', backref='course', lazy=True)

class Donor(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(80))
    organisation = db.Column(db.String(80))
    amount = db.Column(db.Integer)
    payments = db.relationship('Payment', backref='donor', lazy=True)
    certificates = db.relationship('Certificate', backref='donor', lazy=True)

class Certificate(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    issue_date = db.Column(db.Date)
    message = db.Column(db.String(80))
    signature = db.Column(db.String(80))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)

class Payment(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date = db.Column(db.Date)
    payment_method = db.Column(db.String(100))
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)

class FinancialAid(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user._id'), nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor._id'), nullable=False)
    application_status = db.Column(db.String(100))
    application_date = db.Column(db.Date)


# Create a database model for the application
class Application(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    financial_need = db.Column(db.Text, nullable=False)
    last_grade = db.Column(db.String(50), nullable=False)
"""

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(250))
    duration = db.Column(db.String(25))
    price = db.Column(db.Integer)

class Student(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_number = db.Column(db.Integer, unique=True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    DOB = db.Column(db.Date)
    race = db.Column(db.String(25))
    nationality = db.Column(db.String(25))
    phone_number = db.Column(db.Integer)
    email_address = db.Column(db.String(50))
    physical_address = db.Column(db.String(100))
    highest_grade = db.Column(db.String(25))
    financial_status = db.Column(String(25))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))

class FinancialAid(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Donor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

