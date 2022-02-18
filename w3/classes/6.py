class prime():
    def __init__(self):
        self.pr=[]
    def add_number(self,number):
        self.pr.append(number)
    def find_prime(self):
        a=filter(lambda x:((x**2-1)%24==0 or x==2 or x==3), self.pr)
        print(*(list(a)))
arr=list(map(int,input().split()))
p1=prime()
for i in range(len(arr)):
    p1.add_number(arr[i])
p1.find_prime()
