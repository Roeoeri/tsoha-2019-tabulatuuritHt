from application import db
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


roles_users = db.Table('roles_users', db.Model.metadata,
        db.Column('user_id', db.Integer(), db.ForeignKey('account.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class User(db.Model):

    __tablename__ = "account"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255), nullable=False, unique = True)
    password = db.Column(db.String(512), nullable=False)

    tabs = db.relationship("Tab", backref='account', lazy =True)

    roles = db.relationship("Role", secondary=roles_users)
  

    def __init__ (self,username,password):
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable = False, unique=True)

    users = db.relationship("User", secondary=roles_users)
    

    def __init__(self,name):
        self.name = name




