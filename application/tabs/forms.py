
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class TabForm(FlaskForm):
    name = StringField("Kappaleen nimi", [validators.Length(max=150, message= "Nimi saa olla 150 merkkiä pitkä"),validators.data_required(),validators.Length(min=1, message="Nimeä ei voi jättää tyhjäksi")])
    content = TextAreaField("Lisää tabulatuuri" , [validators.Length(max=12000, message= "Tabulatuuri saa olla 12000 merkkiä pitkä"),validators.data_required(), validators.Length(min=1,message="Tabulatuuri ei voi olla tyhjä")], default="Lisää tabulatuuri....")
    class Meta:
        csrf = False

class TabUpdateForm(FlaskForm):
    name = StringField("Kappaleen nimi", [validators.Length(max=150, message = "Nimi saa olla 150 merkkiä pitkä"), validators.data_required(), validators.Length(min=1, message="Nimeä ei voi jättää tyhjäksi")])
    content = TextAreaField("Lisää tabulatuuri" , [validators.Length(max=12000, message= "Tabulatuuri saa olla 12000 merkkiä pitkä"), validators.data_required(), validators.Length(min=1,message="Tabulatuuri ei voi olla tyhjä")])
    class Meta:
        csrf = False
