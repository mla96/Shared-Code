#!/bin/python
''' This file implements the Enzyme Analysis use case.'''

from csv_file_reader import CSVFileReader
from variable import Variable
from util import Report


class EnzymeAnalyzer(object):
  '''Implements the Enzyme Analysis Use Case. Assumes that the reaction
     rate column is labelled 'V'.'''
  REACTION_RATE_NAME = "V"

  def __init__(self, filename):
    # Input: filename - string of complete path to file
    Report("EnzymeAnalyzer.__init__ for file %s" % filename)
    self.filename = filename
    self.substrate_concentration = None
    self.reaction_rate = None

  def Analyze(self):
    # Construct and displays the plot
    Report("EnzymeAnalyzer.Analyze for file %s" % self.filename)
    csv_file_reader = CSVFileReader(self.filename)
    csv_file_reader.Read()
    column_names = csv_file_reader.GetColumnNames()
    substrate_name = [c for c in column_names if 
        c != EnzymeAnalyzer.REACTION_RATE_NAME][0]
    self.substrate_concentration = (
        csv_file_reader.GetColumnData(substrate_name))
    self.substrate_concentration = (
        csv_file_reader.GetColumnData(EnzymeAnalyzer.REACTION_RATE_NAME))


def Main():
  enzyme_analyzer = EnzymeAnalyzer("test.csv")
  enzyme_analyzer.Analyze()
    

if __name__ == '__main__':
  Main()
