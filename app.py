from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://testuser:dupa1234@localhost/test"
db = SQLAlchemy(app)
from models import *

print("Creating database...")
db.create_all()
print("Created")

import routes

if __name__ == '__main__':
    app.run()
