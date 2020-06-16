import flask
from application import db


class Diamonds(db.Document):
    skus = db.StringField()
    carat = db.IntField()
    price = db.IntField()
    cut = db.StringField()
    color = db.StringField()
    clarity = db.StringField()
    shapeCode = db.StringField()