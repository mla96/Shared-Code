'''Reads a CSV file and provides access to its data.'''

from util import Report
from variable import Variable


class CSVFileReader(object):
  '''
     Reads one or more columns from a comma separated variable file
     file a header.
     This is a skeleton implementation using the class variables below.
  '''
  COLUMNS = ["S", "V"]
  DATA = {"S": [range(1,10)], "V": [range(11, 20)]}
  
  def __init__(self, filename):
    # Input: filename - string of file path to read
    Report("CSVFileReader.__init__ for %s" % filename)
    self.filename = filename
    self.columns = []
    self.data = {}

  def Read(self):
    Report("CSVFileReader.Read for %s" % self.filename)
    self.columns.extend(CSVFileReader.COLUMNS)
    for i in [0, 1]:
      key =CSVFileReader.COLUMNS[i]
      self.data[key] = Variable(key, CSVFileReader.DATA[key])

  def GetColumnNames(self):
    # Returns: list of column names
    Report("CSVFileReader.GetColumnNames for %s" % self.filename)
    result = self.columns
    return(self.columns)

  def GetColumnData(self, name):
    # Returns: Variable associated with the column name
    Report("CSVFileReader.GetColumnData for %s" % self.filename)
    return(self.data[name])


def Main():
  csv = CSVFileReader("test.csv")
  csv.Read()
  print csv.GetColumnNames()
  print csv.GetColumnData("S").GetValues()
  

if __name__ == '__main__':
  Main()
