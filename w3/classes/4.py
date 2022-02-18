class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x,self.y)
    def move(self,x1,y1):
        self.x=self.x+x1
        self.y=self.y+y1
        print(self.x,self.y)
    def dist(self):
        print(abs(self.x-self.y))
x,y=map(int,input().split())
p1=Point(x,y)
p1.show()
x1,y1=map(int,input().split())
p1.move(x1,y1)
p1.show()
p1.dist()
