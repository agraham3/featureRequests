from app import db

class ClientTable(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(10), index=True, unique=True)
  request = db.relationship('FeatureRequestTable', backref='client')

  def __repr__(self):
    return "Client Name: %r" % (self.name)

class ProductAreaTable(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(10), index=True, unique=True)
  request = db.relationship('FeatureRequestTable', backref='productArea')

  def __repr__(self):
    return "Product Area: %r" % (self.name)

class FeatureRequestTable(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), index=False, unique=False)
  description = db.Column(db.String(200), index=False, unique=False)
  ticketURL = db.Column(db.String(200), index=False, unique=False)
  priorityNumber = db.Column(db.Integer, index=False, unique=False)
  targetDate = db.Column(db.Date, index=False, unique=False)
  clientID = db.Column(db.Integer, db.ForeignKey('client_table.id'))
  productAreaID = db.Column(db.Integer, db.ForeignKey('product_area_table.id'))

  def __repr__(self):
    return "Title: %r\n \
            Description: %r\n \
            Ticket URL: %r\n \
            Priority Number: %r\n \
            Target Date: %r\n \
            Client ID: %r\n \
            Product Area ID: %r\n " % (self.title, self.description,
                                       self.ticketURL, self.priorityNumber,
                                       self.targetDate, self.clientID,
                                       self.productAreaID)