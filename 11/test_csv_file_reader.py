import unittest
from csv_file_reader import CSVFileReader

FILENAME = "11_THDPA.csv"
COLUMN_NAMES = ["S", "r"]
DATA_r = [0.11, 0.19, 0.21, 0.22, 0.21, 0.21]

class TestCSVFileReader(unittest.TestCase):

  def setUp(self):
    self.csv = CSVFileReader(FILENAME)

  def testConstructor(self):
    self.csv = CSVFileReader(FILENAME)
    self.assertTrue(self.csv.filename == FILENAME, "Wrong filename")
    self.assertTrue(len(self.csv.names) == 0, "Bad names")
    self.assertTrue(len(self.csv.data.keys()) == 0) 
    
if __name__ == '__main__':
    unittest.main()
