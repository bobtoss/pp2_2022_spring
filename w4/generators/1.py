def square(n):
    for i in range(n):
        yield i*i
n=int(input())
for i in square(n):
    print(i)