class Shape:
    def area(self,lenght=0):
        print(lenght**2)
class Square(Shape):
    def __init__(self,lenght=0):
        self.lenght=lenght
p1=Square()
p1.area(int(input()))