from flask_wtf import FlaskForm
import string
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
#from security.models import User
import re

class student_registration(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    enrol_number = StringField('Enrollment Number',validators=[DataRequired()])
    contact = StringField('Contact Number',validators=[DataRequired(),Length(min=10,max=10)])
    parent_contact = StringField('Parents Contact', validators=[DataRequired(),Length(min=10,max=10)])
    room_number = StringField('Room Number',validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')   

class Hostel_entry(FlaskForm):
    destination = StringField('Destination',validators=[DataRequired()])
    submit = SubmitField('Submit')

class New_Room(FlaskForm):
    enrol = StringField('Enrolment Number',validators=[DataRequired()])
    new_room = StringField('New Room', validators=[DataRequired()])
    submit = SubmitField('Update')   

class New_Contact(FlaskForm):
    enrol = StringField('Enrolment Number',validators=[DataRequired()])
    new_contact = StringField('New Contact', validators=[DataRequired()])
    submit = SubmitField('Update')   

class Parent_new_contact(FlaskForm):
    enrol = StringField('Enrolment Number',validators=[DataRequired()])
    parent_new_contact = StringField("Parent's New Contact", validators=[DataRequired()])
    submit = SubmitField('Update')   

class Single_student(FlaskForm):
    enrol = StringField('Enrolment Number',validators=[DataRequired()])
    submit = SubmitField('Delete')

class Input_enrol(FlaskForm):
    enrol = StringField('Enrolment Number',validators=[DataRequired()])
    submit = SubmitField('Submit')

class Batch(FlaskForm):
    batch = StringField('Batch Year',validators=[DataRequired()])
    submit = SubmitField('Delete')

class Input_date(FlaskForm):
    date = StringField('Date',validators=[DataRequired()], render_kw={"placeholder":"YYYY-MM-DD"})
    submit = SubmitField('Submit')