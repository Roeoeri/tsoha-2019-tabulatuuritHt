from application import app, db,login_required, login_manager
from flask import render_template, request,redirect, url_for
from flask_login import  current_user
from application.tabs.models import Tab
from application.auth.models import Role, User
from application.genreTab.models import GenreTab
from application.genres.models import Genre
from application.tabs.forms import TabForm


@app.route("/profile/walloffame", methods = ["GET"])
def wall_of_fame():
    stmt = "select account.id,  account.username, count(*) As amount  from account join tab on tab.account_id = account.id group by account.id,  account.username order by amount desc limit 3;"
    res = db.engine.execute(stmt)
    response = []
    for row in res:
	    response.append({"id":row[0], "username": row[1], "tabs": row[2]})
    
    return render_template("profile/wallOfFame.html", users = response)
    

@app.route ("/profile/<id>", methods =["GET"])
def single_profile(id):
    page = request.args.get('page', 1, type=int)

    tabs = Tab.query.filter_by(account_id = id).paginate(page,5,False)


    next_url = url_for("single_profile", page=tabs.next_num, id = id) \
        if tabs.has_next else None

    prev_url = url_for("single_profile", page=tabs.prev_num, id = id) \
        if tabs.has_prev else None

    return render_template("profile/single.html", user = User.query.get(id), tabs = tabs.items, next = next_url, prev = prev_url)


    
