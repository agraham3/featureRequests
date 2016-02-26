from flask import render_template, flash, redirect
from app import app, db
from .forms import FeatureRequestForm
from .models import FeatureRequestDB

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/featureRequest', methods=['GET', 'POST'])
def featureRequest():
  form = FeatureRequestForm()
  if form.validate_on_submit():
    featureRequest = FeatureRequestDB(title = form.title.data,
                                      description = form.description.data,
                                      client = form.client.data,
                                      clientPriority = form.clientPriority.data,
                                      targetDate = form.targetDate.data,
                                      ticketURL = form.ticketURL.data, 
                                      productArea = form.productArea.data)
    db.session.add(featureRequest)
    db.session.commit()
    return redirect('/index')

  return render_template('featureRequest.html', 
                         title='Feature Request', 
                         form=form)