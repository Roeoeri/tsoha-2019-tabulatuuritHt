from wtforms import TextAreaField
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import validators



class TabForm(FlaskForm):
    name = StringField("Kirjoita nimi", [validators.Length(min=1, message="Nimeä ei voi jättää tyhjäksi")])
    content = TextAreaField("Lisää tabulatuuri" , [validators.Length(min=1,message="Tabulatuuri ei voi olla tyhjä")], default="Lisää tabulatuuri....")
    class Meta:
        csrf = False