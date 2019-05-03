from flask import Flask
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tabs.db"
    app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

from functools import wraps

from flask_login import LoginManager, current_user
from application.auth.models import  Role
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi"


def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                for user_role in current_user.roles:
                    id = user_role.id
                    userRole = Role.query.get(id)
                    roleName = userRole.name
                    print(roleName)

                    if roleName == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper



from application import views

from application.tabs import models
from application.tabs import views

from application.auth.models import User, roles_users
from application.auth import views

from application.genres import views
from application.genres import models

from application.genreTab import models

from application.profile import views

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)


@app.before_first_request
def create_user():
    try: 
         db.create_all()
         username = os.getenv("USERNAME")
         password = bcrypt.generate_password_hash(os.getenv("PASSWORD")).decode('utf-8')
         admin = User(username,password)
         adminRole = Role("ADMIN")
         userRole = Role("USER")

         db.session().add(admin)
         db.session().flush

         db.session().add(adminRole)
         db.session().flush()

         db.session().add(userRole)
         db.session().flush()

         admin.roles.append(adminRole)
         admin.roles.append(userRole)

         db.session().commit()
    except:
        pass

 
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
except:
    pass
