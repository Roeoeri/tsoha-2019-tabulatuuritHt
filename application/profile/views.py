from application import app, db,login_required, login_manager
from flask import render_template, request,redirect, url_for
from flask_login import  current_user
from application.tabs.models import Tab
from application.auth.models import Role, User
from application.genreTab.models import GenreTab
from application.genres.models import Genre
from application.tabs.forms import TabForm


@app.route ("/profile/<id>", methods =["GET"])
def single_profile(id):
    tabs = Tab.query.filter_by(account_id = id)

    return render_template("profile/single.html", user = User.query.get(id), tabs = tabs)


    
