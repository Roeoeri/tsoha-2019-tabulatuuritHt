
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class GenreForm(FlaskForm):

    genre = StringField("Kappaleen genre ", [validators.Length(max=150, message ="Genre saa olla korkeintaan 150 merkkiä"), validators.Length(min=1, message="Genreä ei voi jätttää tyhjäksi"), validators.data_required(message = "Genreä ei voi jättää tyhjäksi")])
    
    class Meta:
        csrf = False