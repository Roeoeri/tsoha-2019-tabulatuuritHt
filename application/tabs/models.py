from application import db

class Tab(db.Model):
	id = db.Column(db.Integer, primary_key=True)

	name = db.Column(db.String(150), nullable=False)
	content = db.Column(db.String(12000), nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

	genreTabs = db.relationship("GenreTab", backref='Tab', lazy =True)

	def __init__(self,name,content):
		self.name = name
		self.content = content




	
		
