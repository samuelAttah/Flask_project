from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    username = StringField(label="User Name:", validators=[DataRequired()])
    email_address = StringField(
        label="Email Address: ", validators=[DataRequired()])
    password1 = PasswordField(label="Password:")
    password2 = PasswordField(label="Confirm Password:")
    submit = SubmitField('Submit')
