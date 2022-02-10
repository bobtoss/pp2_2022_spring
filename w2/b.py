n=int(input())
list=list(map(int,input().split()))
max=0
max1=0
for i in list:
    if i>max:
        max=i
list.remove(max)
for i in list:
    if i>max1:
        max1=i
print(max*max1)
