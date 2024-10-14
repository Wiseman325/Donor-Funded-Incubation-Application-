from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import date, datetime
from sqlalchemy import Column, Date, DateTime, String, Integer, Text
import os
from werkzeug.utils import secure_filename

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
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
    saved_financial_aid = db.relationship('SavedFinancialAid')
    userAlert = db.relationship('UserAlert')

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


class FinancialAid(db.Model):
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String(255), nullable=False)
    type = db.Column(String(150), nullable=False)
    description = db.Column(Text, nullable=False)
    eligibility_criteria = db.Column(Text, nullable=False)
    opening_date = db.Column(Date, nullable=False)
    deadline = db.Column(Date, nullable=False)
    contact_details = db.Column(String(255), nullable=False)
    link_to_more_information = db.Column(String(255))  # Allow null values for optional link
    date_added = db.Column(Date, nullable=False, default=date.today)
    saved_financial_aid = db.relationship('SavedFinancialAid')
    userAlert = db.relationship('UserAlert')


class SavedFinancialAid(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    financial_aid_id = db.Column(db.Integer, db.ForeignKey('financial_aid.id'), nullable=False)
    date_saved = db.Column(db.DateTime)


class UserAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    financial_aid_id = db.Column(db.Integer, db.ForeignKey('financial_aid.id'), nullable=False)
    reminder_date = db.Column(db.DateTime)
    reminder_message = db.Column(db.Text)


