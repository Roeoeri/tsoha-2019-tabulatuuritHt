
from application import app, db
from flask import render_template, request,redirect, url_for
from flask_login import login_required, current_user
from application.tabs.models import Tab
from application.genres.models import Genre
from application.genres.forms import GenreForm


@app.route ("/genres/", methods=["GET"])
def genres_index():
	return render_template("genres/list.html", genres = Genre.find_tabs_in_genre())


@app.route ("/genres/new/", methods=["GET"])
@login_required
def genre_form():
	return render_template("genres/new.html", form = GenreForm())


@app.route ("/genres/new/", methods=["POST"])
@login_required
def genre_create():

    form = GenreForm(request.form)

    if not form.validate():
        return render_template("/genres/new.html", form = form)

    genreFormContent = (form.genre.data)

    genre = Genre(genreFormContent)
	
    db.session().add(genre)
    db.session().commit()

    return redirect(url_for("genres_index"))
    



