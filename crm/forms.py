"""All forms are defined here"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,\
    SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from crm.models import User, Lead


class RegistrationForm(FlaskForm):
    """Form to create new user/admin for the portal

    Form consists of username, email, password and confirm password input fields
    """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Validate username does not already exists"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username duplicate not allowed')

    def validate_email(self, email):
        """Validate email does not already exists"""
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email duplicate not allowed')


class LoginForm(FlaskForm):
    """Form to login user into portal"""
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember')
    submit = SubmitField('Login')


class LeadForm(FlaskForm):
    """Form to create new lead.

    Form consists of name, company, phone, and email input fields
    """
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    company = StringField('Company', validators=[DataRequired(), Length(min=2, max=50)])
    phone = StringField('Phone', validators=[Length(min=4, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Create Lead')

    def validate_phone(self, phone):
        """Validate phone contains numeric characters"""
        phone = phone.data.replace("-", "").replace("+", "")
        if not phone.isnumeric():
            raise ValidationError('Phone format no allowed')


class TouchForm(FlaskForm):
    """Form to create new touch.

    Form consists of description and select box for list of leads
    """
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2)])
    lead_id = SelectField('Lead', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Create Touch')

    def validate_lead_id(self, lead_id):
        """Validate selected lead already exists"""
        lead = Lead.query.filter_by(id=lead_id.data).first()
        if not lead:
            raise ValidationError('Lead not exists')