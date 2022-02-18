class Myclass:
    '''def __init__(self,string):
        self.string=string'''
    def getString(self,string):
        self.string=string
    def printString(self):
        print(self.string.upper())
p1=Myclass()
p1.getString(input())
p1.printString()