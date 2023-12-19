from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="username", validators=[DataRequired()])
    email_address = StringField(label="email", validators=[DataRequired()])
    password1 = PasswordField(label="password1")
    password2 = PasswordField(label="password2")
    submit = SubmitField('Submit')
