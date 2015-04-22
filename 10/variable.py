'''Implements a variable as used in Enzyme Analysis.'''

from util import Report

class Variable(object):
  '''Controlled access to a variable and its data.'''
  
  def __init__(self, name, values):
    # Input: name - string of variable
    #        values - list of data values
    Report("Variable.__init__ for %s" % name)
    self.name = name
    self.values = values

  def GetName(self):
    # Returns: name of variable
    Report("Variable.GetName for variable %s" % self.name)
    return self.name

  def GetValues(self):
    # Returns: data for variable
    Report("Variable.GetValues for variable %s" % self.name)
    return self.values

  def Rename(self, new_name):
    # Input: new_name - string name to which the variable is changed
    Report("Variable.Rename for variable %s to %s" % 
        (self.name, new_name))
    self.name = new_name

def Main():
  v = Variable("var1", range(1,10))
  v.GetName()
  v.GetValues()
  v.Rename("var2")
    


if __name__ == '__main__':
  Main()
