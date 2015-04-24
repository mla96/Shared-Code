'''Implements a variable as used in Enzyme Analysis.'''

class Variable(object):
  '''Controlled access to a variable and its data.'''
  
  def __init__(self, name, values):
    # Input: name - string of variable
    #        values - list of data values
    self.name = name
    self.values = values

  def GetName(self):
    # Returns: name of variable
    return self.name

  def GetValues(self):
    # Returns: data for variable
    return self.values

  def Rename(self, new_name):
    # Input: new_name - string name to which the variable is changed
    self.name = new_name

  def __str__(self):
    return "%s: %s" % (self.name, self.values)

def Main():
  v = Variable("var1", range(1,10))
  print v
  v.GetName()
  v.GetValues()
  v.Rename("var2")
    


if __name__ == '__main__':
  Main()
