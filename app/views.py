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
    flash('Login requested for OpenID="%s", remember_me="%s"' % 
          (form.openid.data, str(form.remember_me.data)))
    return redirect('/index')

  return render_template('featureRequest.html', 
                         title='Feature Request', 
                         form=form)