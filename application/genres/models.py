from application import db

class Genre(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	genre = db.Column(db.String(150), nullable=False)
	genreTabs = db.relationship("GenreTab", backref='Genre', lazy =True)
	
	@staticmethod
	def find_tabs_in_genre():
		stmt = "Select genre.genre, count(*) from genre_tab join genre on genre.id = genre_tab.genre_id group by genre.genre"

		res = db.engine.execute(stmt)
		response = []
		for row in res:
			genre = row[0]
			amount = row[1]
			genreId = Genre.query.filter_by(genre = genre).first().id

			response.append({"genre": genre, "amount": amount, "id": genreId})
		return response

	def __init__(self,genre):
		self.genre = genre




	
