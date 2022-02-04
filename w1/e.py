
n1, n2 = map(int, input().split()) 
n=n1
f=n2
cnt=0
for i in range(2,n):
    if n%i==0:
        cnt=cnt+1
if cnt==0 and f%2==0 and n<500:
    print("Good job!")
else:
    print("Try next time!")