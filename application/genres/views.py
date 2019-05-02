
from application import app, db, login_required
from flask import render_template, request,redirect, url_for
from flask_login import current_user
from application.tabs.models import Tab
from application.genres.models import Genre
from application.genres.forms import GenreForm
from application.genreTab.models import GenreTab


@app.route ("/genres/", methods =["GET"])
@login_required(role="ADMIN")
def genre_index():
    return render_template("genres/list.html", genres = Genre.query.all())

@app.route ("/genres/delete/<id>", methods=["POST"])
@login_required(role="ADMIN")
def genre_delete(id):
	genre = Genre.query.get(id)
	GenreTab.query.filter_by(genre_id = id).delete()

	db.session.delete(genre)
	db.session.commit()

	return redirect(url_for("genre_index"))

@app.route("/genres/update<id>", methods=["GET"])
@login_required(role="ADMIN")
def genre_update_form(id):
    genre = Genre.query.get(id)
    return render_template("genres/update.html", genre=genre, form = GenreForm())


@app.route ("/genres/<id>/", methods=["POST"])
@login_required(role = "ADMIN")
def genre_update(id):

    form = GenreForm(request.form)
    genre = Genre.query.get(id)

    if not form.validate():
	    return render_template("genres/update.html", form = form, genre = genre)
    
    genreExists = Genre.query.filter_by(genre = form.genre.data).first()
    if genreExists:
        return render_template("genres/update.html", form = form, genre = genre, error ="Genre on jo olemassa")



    genre.genre = (request.form.get("genre"))
    db.session().commit()

    return redirect(url_for("genre_index"))


@app.route ("/genres/new/", methods=["GET"])
@login_required(role="USER")
def genre_form():
	return render_template("genres/new.html", form = GenreForm())


@app.route ("/genres/new/", methods=["POST"])
@login_required(role="USER")
def genre_create():

    form = GenreForm(request.form)

    if not form.validate():
        return render_template("/genres/new.html", form = form)
    
    genreExists = Genre.query.filter_by(genre = form.genre.data).first()

    if genreExists:
        return render_template("/genres/new.html", form = form, error = "Genre on jo olemassa")
        

    genreFormContent = (form.genre.data)

    genre = Genre(genreFormContent)
	
    db.session().add(genre)
    db.session().commit()

    return redirect(url_for("tabs_form"))
    



