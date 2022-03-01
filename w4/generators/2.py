def even(n):
    for i in range(n):
        if i%2==0:
            yield i
n=int(input())
for i in even(n):
    if int(i/2)==int((n-1)/2):
        print(i)
    else:
        print(i,end="," )