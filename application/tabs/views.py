from application import app, db,login_required, login_manager
from flask import render_template, request,redirect, url_for
from flask_login import  current_user
from application.tabs.models import Tab
from application.auth.models import Role
from application.genreTab.models import GenreTab
from application.genres.models import Genre
from application.tabs.forms import TabForm, TabUpdateForm

def canEdit(tab_id):

	isAuthorized = False

	if current_user.is_authenticated:
		for user_role in current_user.roles:
			if user_role.name == "ADMIN":
				isAuthorized = True 

	tab = Tab.query.get(tab_id)
	if current_user.is_authenticated:
		if tab.account_id == current_user.id:
			isAuthorized = True

	
	return isAuthorized


@app.route ("/tabs/genres/", methods=["GET"])
def tabs_by_genre():
	return render_template("tabs/tabsByGenre.html", genres = Genre.find_tabs_in_genre())


@app.route ("/tabs/genres/<id>", methods=["GET"])
def tabs_in_genre(id):
    stmt = "select tab.name, tab.id from genre join genre_tab on genre.id = genre_tab.genre_id join tab on tab.id = genre_tab.tab_id where genre.id =" +id

    genreName = Genre.query.get(id).genre

    res = db.engine.execute(stmt)
    response = []
    for row in res:
	    response.append({"name": row[0], "id": row[1]})
    
    return render_template("tabs/tabsInGenre.html", name = genreName, tabs = response)



@app.route ("/tabs/", methods=["GET"])
def tabs_index():
	return render_template("tabs/list.html", tabs = Tab.query.all())


@app.route ("/tabs/update/<id>/", methods = ["GET"])
@login_required()
def tabs_update_form(id):
	canUpdate = canEdit(id)

	if not canUpdate:
		return login_manager.unauthorized()

	
	tab = Tab.query.get(id)
	return render_template("tabs/update.html", tab = tab, form = TabUpdateForm())

@app.route ("/tabs/<id>", methods=["GET"])
def tabs_single(id):

	tab = Tab.query.get(id)
	
	return render_template("tabs/single.html", tab = tab, canEdit = canEdit(id))


@app.route ("/tabs/delete/<id>", methods=["POST"])
@login_required()
def tabs_delete(id):
	tab = Tab.query.get(id)
	GenreTab.query.filter_by(tab_id = id).delete()

	canDelete = canEdit(id)

	if not canDelete:
		return login_manager.unauthorized()

	db.session.delete(tab)
	db.session.commit()

	return redirect(url_for("tabs_index"))

@app.route ("/tabs/<id>/", methods=["POST"])
@login_required()
def tabs_update(id):

	canUpdate = canEdit(id)
	

	if not canUpdate:
		return login_manager.unauthorized()


	form = TabUpdateForm(request.form)
	tab = Tab.query.get(id)

	if not form.validate():
		rejectedName = request.form.get("name")
		rejectedContent = request.form.get("content")
		rejectedTab = Tab(rejectedName,rejectedContent)
		rejectedTab.id = tab.id
		
		return render_template("tabs/update.html", form = form, tab = rejectedTab)
	
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
			return render_template("tabs/new.html", form = form, genres = Genre.query.all())
	

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

	
