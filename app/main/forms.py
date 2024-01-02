from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models import User


class RegisterForm(FlaskForm):
    username = StringField(label="User Name:", validators=[
                           DataRequired(), Length(2, 30)])
    email_address = StringField(
        label="Email Address: ", validators=[DataRequired(), Email(), Length(3, 64)])
    password1 = PasswordField(label="Password:", validators=[Length(min=6),
                              DataRequired()])
    password2 = PasswordField(
        label="Confirm Password:", validators=[DataRequired(), EqualTo('password1', message="Passwords must match.")])
    submit = SubmitField('Create Account')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already in use")

    def validate_email_address(self, field):
        if User.query.filter_by(email_address=field.data).first():
            raise ValidationError("Email already in use")


class LoginForm(FlaskForm):
    username = StringField(label="User Name: ", validators=[
                           DataRequired(), Length(2, 30)])

    password = PasswordField(label="Password:", validators=[Length(min=6),
                                                            DataRequired()])

    remember_me = BooleanField(label="Keep me logged in", default=False)

    submit = SubmitField('Sign In')
