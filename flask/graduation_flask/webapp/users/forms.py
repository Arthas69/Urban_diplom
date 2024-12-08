from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, ValidationError, BooleanField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from webapp.users.models import User


class RegistrationForm(FlaskForm):
    """
    Form for user registration.
    """
    username = StringField('Username: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Password: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    confirm = PasswordField('Repeat password:', validators=[DataRequired(), EqualTo('password', message='Passwords must match')], render_kw={'class': 'form-control'})
    email = StringField('E-mail: ', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    firstname = StringField('Firstname: ', render_kw={'class': 'form-control'})
    lastname = StringField('Lastname: ', render_kw={'class': 'form-control'})
    submit = SubmitField('Sign Up', render_kw={'class': "btn btn-success"})

    def validate_username(self, username):
        """
        Validates username uniqueness.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')

    def validate_email(self, email):
        """
        Validates email uniqueness.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail already registered')


class LoginForm(FlaskForm):
    """
    Form for user login.
    """
    username = StringField('Username: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Password: ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Remember me ', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Log In', render_kw={'class': "btn btn-success"})


class EditProfileForm(FlaskForm):
    """
    Form for editing user profile.
    """
    visible_name = StringField('Visible name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    firstname = StringField('Firstname', validators=[Length(min=0, max=20)], render_kw={'class': 'form-control'})
    lastname = StringField('Lastname', validators=[Length(min=0, max=20)], render_kw={'class': 'form-control'})
    submit = SubmitField('Accept changes', render_kw={'class': 'btn btn-success'})
