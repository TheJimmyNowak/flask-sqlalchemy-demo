from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Here insert your db in my case it's my local postgres
# And remember never add passwords to public repos :p
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://testuser:dupa1234@localhost/test"
db = SQLAlchemy(app)

from models import *

print("Creating database...")
db.create_all()
print("Created")

import routes

if __name__ == '__main__':
    app.run()
