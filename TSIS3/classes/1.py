class string(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = raw_input()
    def printString(self):
        print self.s.upper()   #to uppercase
strObj = InputOutString()
strObj.getString()
strObj.printString()

