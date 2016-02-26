from flask.ext.wtf import Form
from wtforms import validators, StringField, \
                    TextAreaField, SelectField, \
                    DateField, IntegerField

class FeatureRequestForm(Form):
  urlRegex = '^https?://www.[\w||\d||.||-||/]+.[\w||\d||.||-||/]+$'
  title = StringField('Title', [validators.Required(), validators.length(max=50)])
  description = TextAreaField('Description', [validators.Required(),
                                              validators.length(max=200)])
  client = SelectField('Client', choices=[('Client A', 'Client A'), 
                                          ('Client B', 'Client B'),
                                          ('Client C', 'Client C')])
  clientPriority = IntegerField('Client Priority', 
                                [validators.Required(), validators.NumberRange(min=1)])
  targetDate = DateField('Target Date (yy/mm/dd)',
                         format='%y/%m/%d')
  ticketURLMessage = 'Must be a url in form of (you may add an s after http): http://www.*.*'
  ticketURL = StringField('Ticket URL', 
                          [validators.Optional(),
                          validators.Regexp(urlRegex, message=ticketURLMessage)])
  productArea = SelectField('Product', choices=[('polices', 'Policies'),
                                                ('billing', 'Billing'),
                                                ('claims', 'Claims'),
                                                ('Reports', 'Reports')])