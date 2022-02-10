x,y=input().split()
x=int(x)
y=int(y)
n=int(input())
pair=[]
for i in range(n):
    x2,y2=input().split()
    x1=int(x2)
    y1=int(y2)
    s=x2+" "+y2
    res=((x-x1)**2+(y-y1)**2)
    list=[res,s]
    pair.append(list)
pair.sort()
for i in pair:
    print(i[1])
