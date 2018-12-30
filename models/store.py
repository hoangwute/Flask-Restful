from db import db

class StoreModel(db.Model):
	__tablename__ = 'stores'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	items = db.relationship('ItemModel', lazy='dynamic') #avoid creating store in item everytime store model is used

	def __init__(self, name):
		self.name = name

	def json(self):
		return {'name': self.name, 'items': [item.json() for item in self.items.all()]} #when we use lazy='dynamic' self.items is a query builder

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name=name LIMIT 1

	@classmethod
	def find_all(cls):
		return cls.query.all()

	def save_to_db(self): #both inserting and updating
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()	