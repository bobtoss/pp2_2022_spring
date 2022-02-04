n=int(input())
s=str(input())

if s=="k":
    x=int(input())
    print(round(n/1024,x))
else:
    print(n*1024)