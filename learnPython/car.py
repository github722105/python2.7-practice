#
# Sample Python program for creating JSON file from a class.
#


#
#
#
class Car(object):

  def __init__(self, make, model, transmission, color, doors=4, features={}):
    '''Extremely basic class. All we're doing is setting up the objects.'''
    self.make = make
    self.model = model
    self.transmission = transmission
    self.color = color
    self.doors = doors
    self.features = features
