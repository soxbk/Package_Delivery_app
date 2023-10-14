import datetime


class Package:
    deliveryTime = datetime.time

    def __init__(self, packageID, address, city, state, zipCode, deliveryDeadline, mass, specialNotes=None,
                 deliveryStatus='At hub', enrouteStartTime= None, deliveryTime=None):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.mass = mass
        self.specialNotes = specialNotes
        self.deliveryTime = deliveryTime
        self.enrouteStartTime = enrouteStartTime
        self.deliveryStatus = deliveryStatus
