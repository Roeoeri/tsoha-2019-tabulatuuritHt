from application import app, db
from flask import render_template, request,redirect, url_for
from flask_login import login_required, current_user
from application.tabs.models import Tab
from application.genreTab.models import GenreTab
from application.genres.models import Genre
from application.tabs.forms import TabForm


@app.route ("/tabs/", methods=["GET"])
def tabs_index():
	return render_template("tabs/list.html", tabs = Tab.query.all())


@app.route ("/tabs/update/<id>/", methods = ["GET"])
@login_required
def tabs_update_form(id):
	tab = Tab.query.get(id)
	return render_template("tabs/update.html", tab = tab)

@app.route ("/tabs/<id>", methods=["GET"])
def tabs_single(id):
	
	tab = Tab.query.get(id)
	return render_template("tabs/single.html", tab = tab)


@app.route ("/tabs/delete/<id>", methods=["POST"])
@login_required
def tabs_delete(id):
	tab = Tab.query.get(id)
	db.session.delete(tab)
	db.session.commit()
	return redirect(url_for("tabs_index"))

@app.route ("/tabs/<id>/", methods=["POST"])
@login_required
def tabs_update(id):
	
	tab = Tab.query.get(id)
	tab.name = (request.form.get("name"))
	tab.content = (request.form.get("content"))
	db.session().commit()

	return redirect(url_for("tabs_index"))

@app.route("/tabs/new/")
@login_required
def tabs_form():
	return render_template("tabs/new.html", form = TabForm(), genres = Genre.query.all())

@app.route("/tabs/", methods=["POST"])
@login_required
def tabs_create():

	form = TabForm(request.form)

	if not form.validate():
			return render_template("tabs/new.html", form = form)
	

	name = (form.name.data)
	content = (form.content.data)




	tab = Tab(name,content)
	tab.account_id = current_user.id

	

	genres = request.form.getlist('genre_switch')
	
	
	db.session().add(tab)

	db.session.flush()

	for g in genres:
		genretab = GenreTab(g,tab.id)
		db.session.add(genretab)

	db.session().commit()

	return redirect(url_for("tabs_index"))

	
