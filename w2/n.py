a=1
arr=[]
while a==1:
    n=int(input())
    if n==0:
        break
    arr.append(n)
sum=[]
if len(arr)%2==1:
    cnt=int(len(arr)/2+1)
    for i in range(cnt):
        if i==cnt-1:
            s=arr[i]
            sum.append(s)
        else:
            s=arr[i]+arr[n-1-i]
            sum.append(s)
else:
    cnt=int(len(arr)/2)
    for i in range(cnt):
        s=arr[i]+arr[n-1-i]
        sum.append(s)
print(*sum)