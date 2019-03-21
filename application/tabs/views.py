from application import app, db
from flask import render_template, request,redirect, url_for
from application.tabs.models import Tab


@app.route ("/tabs/", methods=["GET"])
def tabs_index():
	return render_template("tabs/list.html", tabs = Tab.query.all())

@app.route ("/tabs/update/<id>/", methods = ["GET"])
def tabs_update_form(id):
	tab = Tab.query.get(id)
	return render_template("tabs/update.html", tab = tab)

@app.route ("/tabs/<id>/", methods=["POST"])
def tabs_update(id):
	
	tab = Tab.query.get(id)
	tab.name = (request.form.get("name"))
	tab.content = (request.form.get("content"))
	db.session().commit()

	return redirect(url_for("tabs_index"))

@app.route("/tabs/new/")
def tabs_form():
	return render_template("tabs/new.html")

@app.route("/tabs/", methods=["POST"])
def tabs_create():
	print(request.form.get("name"))
	print(request.form.get("content"))
	
	name = request.form.get("name")
	content = request.form.get("content")
	
	tab = Tab(name,content)
	
	db.session().add(tab)
	db.session().commit()

	return redirect(url_for("tabs_index"))

	
