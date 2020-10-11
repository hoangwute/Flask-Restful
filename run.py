from app import app
from db import db

db.init_app(app)


@app.before_first_request  # before the first request runs then run this (create all tables)
def create_tables():
    db.create_all()
