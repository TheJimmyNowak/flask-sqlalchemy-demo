from flask import render_template, request

from app import app
from models import db, User
from models import TextVault


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    if request.method == "GET":
        return render_template('adduser.html')

    db.session.add(User(name=request.form["name"]))
    db.session.commit()
    return "Yes"


@app.route('/vault/add', methods=['GET', 'POST'])
def add_vault():
    if request.method == "GET":
        return render_template('addvault.html', categories=TextVault.categories)

    db.session.add(TextVault(
        title=request.form['title'],
        text=request.form['text'],
        category=request.form['category']
    ))
    print('dupa')
    db.session.commit()
    return "Yes"
