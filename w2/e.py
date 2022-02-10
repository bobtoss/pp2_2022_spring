n1=input()
ok=0
arr=[]
cnt=0
for i in n1:
    if i==" ":
        ok=1
        break
if ok==0:
    n1=int(n1)
    x=int(input())
    for i in range(n1):
        arr.append(x+2*i)
    for i in arr:
        cnt=cnt^i
    print(cnt)
else:
    list=n1.split()
    n=int(list[0])
    x=int(list[1])
    for i in range(n):
        arr.append(x+2*i)
    for i in arr:
        cnt=cnt^i
    print(cnt)