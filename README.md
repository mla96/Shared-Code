# Shared-Code
Code used in lectures
# homework 9

class EnzymeData(Data):
    def __init__(self):
        super(EnzymeData, self).__init__(data)
        
a = EnzymeData("09_THDPA.csv")
print a.getVarNames()
print a.getCol()
print a.getData()
