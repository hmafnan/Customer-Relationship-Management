from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from crm.models import User, Lead


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username duplicate not allowed')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email duplicate not allowed')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')


class LeadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    company = StringField('Company', validators=[DataRequired(), Length(min=2, max=50)])
    phone = StringField('Phone', validators=[Length(min=4, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Create Lead')


class TouchForm(FlaskForm):
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2)])
    lead_id = SelectField('Lead', validators=[DataRequired()], coerce=int)

    submit = SubmitField('Create Touch')

    def validate_lead_id(self, lead_id):
        lead = Lead.query.filter_by(id=lead_id.data).first()
        if not lead:
            raise ValidationError('Lead not exists')