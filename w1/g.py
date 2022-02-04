s=str(input())
dec=0
cnt=0
c=s[: : -1]
for i in c:
    if ord(i)-48==0 :
        cnt=cnt+1
    else :
        dec=dec+2**cnt
        cnt=cnt+1
print(dec)