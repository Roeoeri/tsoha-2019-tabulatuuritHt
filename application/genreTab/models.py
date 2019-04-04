from application import db

class GenreTab(db.Model):
	genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)
	tab_id = db.Column(db.Integer, db.ForeignKey('tab.id'), primary_key=True)

	def __init__(self,genre_id,tab_id):
		self.genre_id = genre_id
		self.tab_id = tab_id