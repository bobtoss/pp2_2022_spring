class Shape:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def area(self):
        print(self.lenght*self.width)
class Rectangle(Shape):
    def __init__(self,lenght,width):
        Shape.__init__(self,lenght,width)
    def area(self):
        print(self.lenght*self.width)
x,y=map(int,input().split())
p1=Rectangle(x,y)
p1.area()

