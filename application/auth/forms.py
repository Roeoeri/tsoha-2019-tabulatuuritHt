from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators



class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.Length(min=1, message="Syötä käyttäjätunnus")])
    password = PasswordField("Salasana", [validators.Length(min=1, message="Syötä salasana")])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.Length(min=1, message="Syötä käyttäjätunnus")])
    password = PasswordField("Salasana", [validators.Length(min=1, message="Syötä salasana")])

    class Meta:
        csrf = False