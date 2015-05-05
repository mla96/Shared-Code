'''Reads a CSV file and provides access to its data.'''

from variable import Variable


class CSVFileReader(object):
  '''
     Reads one or more names from a comma separated variable file
     file a header.
  '''
  
  def __init__(self, filename):
    # Input: filename - string of file path to read
    self.filename = filename
    self.names = []
    self.data = {}


  def Read(self):
    raw_data = {}
    raw_names = []
    got_header = False
    try:
      for line in open(self.filename, 'r'):
        fields = line.strip().split(",")
        if not got_header:
          for i in range(0, len(fields)):
            raw_names.append(fields[i])
            raw_data[raw_names[i]] = []
          got_header = True
        else:
          for i in range(0, len(fields)):
            raw_data[raw_names[i]].append(float(fields[i]))
    except:
      print "%s file not found. Please enter a valid file" % self.filename
      exit()
    for i in range(0, len(raw_names)):
      col = raw_names[i]
      stripped_col = col.replace("'", "")  # remove single quotes
      self.data[stripped_col] = Variable(stripped_col, raw_data[col])
      self.names.append(stripped_col)


if __name__ == '__main__':
  Main()
