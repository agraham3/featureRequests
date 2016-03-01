from flask import render_template, flash, redirect
from app import app, db
from .forms import FeatureRequestForm, ClientRequestForm
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
                         form=form)

@app.route('/viewClientsRequests', methods=['GET', 'POST'])
def viewClientsRequests():
  form = ClientRequestForm()
  client = ''
  if form.validate_on_submit():
    client = form.client.data # to change to database info

  return render_template('viewClientsRequests.html',
                         form=form,
                         client=client)