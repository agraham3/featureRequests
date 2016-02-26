from flask import render_template, flash, redirect
from app import app, db
from .forms import FeatureRequestForm
from .controller import insert_db

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/featureRequest', methods=['GET', 'POST'])
def featureRequest():
  form = FeatureRequestForm()
  if form.validate_on_submit():
    insert_db(form)
    return redirect('/index')

  return render_template('featureRequest.html', 
                         title='Feature Request', 
                         form=form)