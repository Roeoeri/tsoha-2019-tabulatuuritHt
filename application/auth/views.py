from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app,db,bcrypt
from application.auth.models import User, Role
from application.auth.forms import LoginForm, RegisterForm



@app.route("/auth/login", methods  = ["GET", "POST"])
def auth_login():
    form = LoginForm(request.form)
    if request.method == "GET":
        return render_template("auth/loginform.html", form  = form)
    
    

    if not form.validate:
        return render_template("auth/loginform.html", form = form)

    
    users = User.query.filter_by(username=form.username.data)
    user = None
    
    for u in users:
        if bcrypt.check_password_hash(u.password.encode('utf-8'), form.password.data):
            user = u

    if not user:
        return render_template("auth/loginform.html", form = form, error = "Käyttäjää tai salasanaa ei ole olemassa")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))



@app.route("/auth/register")
def auth_register():
    form = RegisterForm(request.form)

    return render_template("auth/registerform.html", form = form)


@app.route("/auth/", methods=["POST"])
def auth_create():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form = form)

    user = User.query.filter_by(username = form.username.data).first()
    
    if user:
        return render_template("auth/registerform.html", form = form, error = "Käyttäjä on jo olemassa")

    userRole = Role.query.filter_by(name="USER").first()
    
    username = (form.username.data)
    password = bcrypt.generate_password_hash((form.password.data)).decode('utf-8')
	
    user = User(username,password)
	
    db.session().add(user)
    db.session().flush()

    user.roles.append(userRole)
    db.session().commit()

    return redirect(url_for("index"))



    
    