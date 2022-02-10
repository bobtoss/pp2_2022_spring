def cmp(s):
    a=s.split()
    return int(a[0])

x,y=input().split()
x=int(x)
y=int(y)
n=int(input())
pair={}
for i in range(n):
    x2,y2=input().split()
    x1=int(x2)
    y1=int(y2)
    s=x2+" "+y2
    res=str(((x-x1)**2+(y-y1)**2))+" "+str(i)
    pair[res]=s
keys = sorted(pair)
keys.sort(key=cmp)
for i in keys:
    print(pair[i])


