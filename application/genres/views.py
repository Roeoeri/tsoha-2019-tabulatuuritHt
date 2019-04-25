
from application import app, db, login_required
from flask import render_template, request,redirect, url_for
from flask_login import current_user
from application.tabs.models import Tab
from application.genres.models import Genre
from application.genres.forms import GenreForm


@app.route ("/genres/", methods=["GET"])
def genres_index():
	return render_template("genres/list.html", genres = Genre.find_tabs_in_genre())


@app.route ("/genres/<id>", methods=["GET"])
def genre_single(id):
    stmt = "select tab.name, tab.id from genre join genre_tab on genre.id = genre_tab.genre_id join tab on tab.id = genre_tab.tab_id where genre.id =" +id

    genreName = Genre.query.get(id).genre

    res = db.engine.execute(stmt)
    response = []
    for row in res:
	    response.append({"name": row[0], "id": row[1]})
    
    return render_template("genres/tabsInGenre.html", name = genreName, tabs = response)



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

    return redirect(url_for("genres_index"))
    



