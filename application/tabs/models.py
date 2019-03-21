from application import db

class Tab(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_added = db.Column(db.DateTime, default=db.func.current_timestamp())

	name = db.Column(db.String(150), nullable=False)
	content = db.Column(db.String(2000), nullable=False)
	
	def __init__(self,name,content):
		self.name = name
		self.content = content


