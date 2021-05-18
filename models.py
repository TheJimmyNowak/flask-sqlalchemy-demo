from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    text_vault = relationship("TextVault", uselist=False, backref="users")

    def __str__(self):
        return str(self.name)


class TextVault(db.Model):
    __tablename__ = 'text_vaults'
    categories = ("Science", "Self-development", "Meditation", "Electronics")
    id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, ForeignKey('users.id'))
    title = db.Column(db.String(50))
    text = db.Column(db.String(2048))
    category = db.Column(db.Enum(categories, name="category_enum"))
