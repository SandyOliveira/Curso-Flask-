from flask import render_template
from app import app

from app.models.tables import User, db
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else: 
        print(form.errors)

    return render_template('login.html', form=form)






@app.route("/create/<info>")
@app.route("/create", defaults={"info": None})
def create(info):
    i = User("Sandy1", "123", "SA", "s@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "Ok"



@app.route("/select/<info>")
@app.route("/select", defaults={"info": None})
def select(info):
    r = User.query.filter_by(username="Sandy").all()
    print(r)
    return "ok"

@app.route("/update/<info>")
@app.route("/update", defaults={"info": None})
def update(info):
    r = User.query.filter_by(username="Sandy").first()
    r.name = "Sandy Oliveira"
    db.session.add(r)
    db.session.commit()
    print(r)
    return "ok"


@app.route("/delete/<info>")
@app.route("/delete", defaults={"info": None})
def delete(info):
    r = User.query.filter_by(username="Sandy").first()
    db.session.delete(r)
    db.session.commit()
   
    return "ok"