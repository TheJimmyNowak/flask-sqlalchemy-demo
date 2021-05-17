from flask_sqlalchemy import SQLAlchemy
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class TextVault(db.Model):
    categories = ("Science", "Self-development", "Meditation", "Electronics")
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    text = db.Column(db.String(2048))
    category = db.Column(db.Enum(categories, name="category_enum"))
