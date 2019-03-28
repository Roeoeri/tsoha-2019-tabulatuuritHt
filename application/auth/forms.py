from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=1, message="Syötä käyttäjätunnus")])
    password = PasswordField("Password", [validators.Length(min=1, message="Syötä salasana")])

    class Meta:
        csrf = False