from flask import render_template, flash, redirect
from app import app
from .forms import FeatureRequestForm, ClientRequestForm
from .controller import insert_db
from .models import ClientTable, FeatureRequestTable

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
  clientList = ''
  clientName = ''
  if form.validate_on_submit():
    clientName = form.client.data
    clientID = ClientTable.query.filter(ClientTable.name == clientName).first()
    if clientID:
      clientID = clientID.id
      clientList = FeatureRequestTable.query.filter(FeatureRequestTable.clientID == clientID).order_by('priorityNumber').all()

  return render_template('viewClientsRequests.html',
                         form=form,
                         clientList=clientList,
                         clientName=clientName)