from flask import render_template, flash, redirect
from app import app
from .forms import FeatureRequest

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

# To change: from tutorial
@app.route('/featureRequest', methods=['GET', 'POST'])
def featureRequest():
  form = FeatureRequest()
  if form.validate_on_submit():
    flash('Form Data < %s > < %s > < %s >  < %s > < %s > < %s > < %s >' 
          % (form.title.data, form.description.data, 
             form.client.data, form.clientPriority.data,
             form.targetDate.data, form.ticketURL.data, 
             form.productArea.data))
    return redirect('/index')

  return render_template('featureRequest.html', 
                         title='Feature Request', 
                         form=form)