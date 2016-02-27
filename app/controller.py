from app import db
from .models import ClientTable, FeatureRequestTable, ProductAreaTable

def priorityNumberReOrder(form, clientID):
  clientRequests = FeatureRequestTable.query.filter(FeatureRequestTable.clientID == clientID).order_by('priorityNumber').all()
  nxtNum = form.clientPriority.data + 1
  for item in clientRequests:
    pNum = item.priorityNumber
    if pNum >= form.clientPriority.data:
      if pNum + 1 == nxtNum:
        item.priorityNumber += 1
        nxtNum = item.priorityNumber + 1
      else:
        break

def insert_db(form):
  c = form.client.data
  ClientTB = ClientTable.query.filter(ClientTable.name == c).first()
  if not ClientTB:
    client = ClientTable(name = c)    
    db.session.add(client)

  pa = form.productArea.data
  ProductAreaTB = ProductAreaTable.query.filter(ProductAreaTable.name == pa).first()
  if not ProductAreaTB:
    product = ProductAreaTable(name=pa)
    db.session.add(product)


  ClientTB = ClientTable.query.filter(ClientTable.name == c).first()
  ProductAreaTB = ProductAreaTable.query.filter(ProductAreaTable.name == pa).first()
  clientID = ClientTB.id
  productAreaID = ProductAreaTB.id
  featureRequest = FeatureRequestTable(title = form.title.data,
                                       description = form.description.data,
                                       ticketURL = form.ticketURL.data,
                                       priorityNumber = form.clientPriority.data,
                                       targetDate = form.targetDate.data,
                                       clientID = clientID,
                                       productAreaID = productAreaID)


  priorityNumberReOrder(form, clientID)
  db.session.add(featureRequest)
  db.session.commit()