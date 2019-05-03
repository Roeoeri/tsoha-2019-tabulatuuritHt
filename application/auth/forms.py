from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators



class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.Length(min=1, message="Syötä käyttäjätunnus")])
    password = PasswordField("Salasana", [validators.Length(min=1, message="Syötä salasana")])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.data_required(message= "Syötä nimimerkki"), validators.Length(min=1, message="Syötä käyttäjätunnus"), validators.Length(max=10, message = "Käyttäjätunnus saa olla korkeintaan 10 merkkiä")])
    password = PasswordField("Salasana", [validators.Length(max = 32, message = "Salasana saa olla korkeintaan 32 merkkiä"),validators.data_required(message = "Syötä salasana"),validators.Length(min=1, message="Syötä salasana")])

    class Meta:
        csrf = False