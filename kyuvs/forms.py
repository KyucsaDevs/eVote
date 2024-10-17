from flask_wtf import FlaskForm
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired,FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired,Length, Email, EqualTo, ValidationError
from kyuvs.models import db

#Student Login form
class LoginForm(FlaskForm):
    username = StringField('Username: ',validators=[DataRequired(),Length(min=10, max=10)])
    password = PasswordField('Password: ',validators=[DataRequired()])
    submit = SubmitField('Login')


#Student Login password-reset form
class PassresetForm(FlaskForm):
    token = StringField('Reset Token: ',validators=[DataRequired()])
    password = StringField('Password: ',validators=[DataRequired(),Length(min=8)])
    confirm_password = StringField('Confirm Password: ',validators=[DataRequired(),Length(min=8)])
    submit = SubmitField('Change Password')


#admin loginform
class AdminLoginForm(FlaskForm):
    email = StringField('Email: ',validators=[DataRequired(),Length(min=5, max=15)])
    password = PasswordField('Password: ',validators=[DataRequired()])
    submit = SubmitField('Login')



#photo upload forms
class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired(),FileAllowed(['jpg','png'], 'Images only')])
    submit = SubmitField('Upload')


#adding candidate details
class AddCandidate(FlaskForm):
    fullname = StringField('Full Name:',validators=[DataRequired(),Length(min=5, max=30)])
    regnumber = StringField('Reg_No: ',validators=[DataRequired(),Length(min=10, max=30)])
    position = StringField('Position: ',validators=[DataRequired(),Length(max=15)])
    school = StringField('School:',validators=[DataRequired(),Length(max=10)])
    course = StringField('Course: ',validators=[DataRequired(),Length(max=10)])
    slogan = StringField('Slogan: ',validators=[DataRequired(),Length(max=30)])
    party = StringField('Party: ',validators=[DataRequired(),Length(min=3, max=15)])
    avater = FileField('Candidate Photo',validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images Only')])
    submit = SubmitField('Save')


#voting candidate
class Vote(FlaskForm):
     checkbox = BooleanField('')
     submit = SubmitField('VOTE')

#removing candidate
class RemoveCandidate(FlaskForm):
     regnumber = StringField('Reg Number: ',validators=[DataRequired(),Length(min=10, max=30)])
     position = StringField('Position: ',validators=[DataRequired(),Length(max=15)])
     submit = SubmitField('Delete Record')