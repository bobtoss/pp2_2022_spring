'''def square(a,b):
    for i in range(a,b):
        yield i*i '''
a,b=map(int,input().split())

squares=(i**2 for i in range(a,b))
for i in squares:
    print(i)