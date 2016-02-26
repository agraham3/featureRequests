from app import db

class FeatureRequestDB(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50), index=False, unique=False)
  description = db.Column(db.String(200), index=False, unique=False)
  client = db.Column(db.String(10), index=True, unique=False)
  clientPriority = db.Column(db.Integer, index=False, unique=False)
  targetDate = db.Column(db.Date, index=False, unique=False)
  ticketURL = db.Column(db.String(200), index=False, unique=False)
  productArea = db.Column(db.String(10), index=True, unique=False)

  def __repr__(self):
    p = "Title: %r\n \
    Description: %r\n \
    Client: %r\n \
    Client Priority Number: %r\n \
    Target Date: %r\n \
    Ticket URL: %r\n \
    Product Area: %r\n" % (self.title, self.description, 
                         self.client, self.clientPriority,
                         self.targetDate, self.ticketURL, 
                         self.productArea)
    return p