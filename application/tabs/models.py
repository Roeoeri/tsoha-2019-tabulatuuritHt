from application import db

class Tab(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_added = db.Column(db.DateTime, default=db.func.current_timestamp())

	name = db.Column(db.String(150), nullable=False)
	content = db.Column(db.String(2000), nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

	
	def __init__(self,name,content):
		self.name = name
		self.content = content


class Genre(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	genre = db.Column(db.String(150), nullable=False)

	genreTabs = db.relationship("GenreTab", backref='genre', lazy =True)

	def __init__(self,genre):
		self.genre = genre

class GenreTab(db.Model):
	genre_id = db.Column(db.Integer, db.ForeignKey('tab.id'), primary_key=True)
	tab_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)

	def __init__(self,genre_id,tab_id):
		self.genre_id = genre_id
		self.tab_id = tab_id
	
		
