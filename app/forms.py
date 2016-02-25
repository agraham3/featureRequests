from flask.ext.wtf import Form
from wtforms import validators, StringField, TextAreaField, SelectField, DateField

class FeatureRequest(Form):
  title = StringField('Title', [validators.Required(), validators.length(max=50)])
  description = TextAreaField('Description', [validators.Required(), 
                                              validators.length(max=200)])
  client = SelectField('Client', choices=[('A', 'Client A'), 
                                          ('B', 'Client B'),
                                          ('C', 'Client C')])
  targetDate = DateField('Target Date (dd/mm/yyyy)', 
                         [validators.Required()], 
                         format='%d-%m-%y')
  ticketURL = StringField('Ticket URL')
  productArea = SelectField('Product', choices=[('polices', 'Policies'),
                                                ('billing', 'Billing'),
                                                ('claims', 'Claims'),
                                                ('Reports', 'Reports')])