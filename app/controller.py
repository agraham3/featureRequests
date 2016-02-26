from app import db
from .models import FeatureRequestDB

def insert_db(form):
  featureRequest = FeatureRequestDB(title = form.title.data,
                                    description = form.description.data,
                                    client = form.client.data,
                                    clientPriority = form.clientPriority.data,
                                    targetDate = form.targetDate.data,
                                    ticketURL = form.ticketURL.data, 
                                    productArea = form.productArea.data)
  db.session.add(featureRequest)
  db.session.commit()