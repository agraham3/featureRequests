from flask.ext.wtf import Form
from wtforms import validators, StringField, TextAreaField, SelectField, DateField

class FeatureRequest(Form):
  title = StringField('Title', [validators.Required(), validators.length(max=50)])
  description = TextAreaField('Description', [validators.Required(), 
                                              validators.length(max=200)])
  client = SelectField('Client', choices=[('Client A', 'Client A'), 
                                          ('Client B', 'Client B'),
                                          ('Client C', 'Client C')])
  targetDate = DateField('Target Date (yy/mm/dd)',
                         format='%y/%m/%d')
  ticketURL = StringField('Ticket URL')
  productArea = SelectField('Product', choices=[('polices', 'Policies'),
                                                ('billing', 'Billing'),
                                                ('claims', 'Claims'),
                                                ('Reports', 'Reports')])