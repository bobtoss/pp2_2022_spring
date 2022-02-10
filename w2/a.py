list=list(map(int,input().split()))
last=len(list)-1
for i in range(len(list)-2,-1,-1):
    if i+list[i]>=last:
        last=i
if last==0:
    print(1)
else:
    print(0)