from application import db

class Tab(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date_added = db.Column(db.DateTime, default=db.func.current_timestamp())

	name = db.Column(db.String(150), nullable=False)
	content = db.Column(db.String(12000), nullable=False)

	account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable = False)

	def __init__(self,name,content):
		self.name = name
		self.content = content




	
		
