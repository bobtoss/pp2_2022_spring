def gen(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
print(*gen(n))

