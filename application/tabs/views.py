from application import app, db,login_required
from flask import render_template, request,redirect, url_for
from flask_login import  current_user
from application.tabs.models import Tab
from application.auth.models import Role
from application.genreTab.models import GenreTab
from application.genres.models import Genre
from application.tabs.forms import TabForm


@app.route ("/tabs/", methods=["GET"])
def tabs_index():
	return render_template("tabs/list.html", tabs = Tab.query.all())


@app.route ("/tabs/update/<id>/", methods = ["GET"])
@login_required(role="ADMIN")
def tabs_update_form(id):
	tab = Tab.query.get(id)
	return render_template("tabs/update.html", tab = tab)

@app.route ("/tabs/<id>", methods=["GET"])
def tabs_single(id):

	isAdmin = False
	if current_user.is_authenticated:
		for user_role in current_user.roles:
			user_id=user_role.id
			role = Role.query.get(user_id).name
			if role == "ADMIN":
				isAdmin = True

	

	tab = Tab.query.get(id)
	return render_template("tabs/single.html", tab = tab, isAdmin = isAdmin)


@app.route ("/tabs/delete/<id>", methods=["POST"])
@login_required(role="ADMIN")
def tabs_delete(id):
	tab = Tab.query.get(id)
	GenreTab.query.filter_by(tab_id = id).delete()
	
	db.session.delete(tab)
	db.session.commit()

	
	return redirect(url_for("tabs_index"))

@app.route ("/tabs/<id>/", methods=["POST"])
@login_required(role="ADMIN")
def tabs_update(id):
	
	tab = Tab.query.get(id)
	tab.name = (request.form.get("name"))
	tab.content = (request.form.get("content"))
	db.session().commit()

	return redirect(url_for("tabs_index"))

@app.route("/tabs/new/")
@login_required(role="USER")
def tabs_form():
	return render_template("tabs/new.html", form = TabForm(), genres = Genre.query.all())

@app.route("/tabs/", methods=["POST"])
@login_required(role="USER")
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

	
