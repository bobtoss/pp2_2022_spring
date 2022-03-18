from functools import reduce
arr=map(int,input().split())
print(reduce(lambda a,b : a*b , arr))
