from flask import render_template, flash
from flask_login import login_user

from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and user.password == form.password.data:
      login_user(user)
      flash('logado...')
    else:
        flash('Verifique as informações e tente novamente...')

  return render_template('login.html', form=form)
  


@app.route("/create/<info>")
@app.route("/create", defaults={"info": None})
def create(info):
    i = User("Sandy1", "1234", "SAa", "ss@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "Ok"
