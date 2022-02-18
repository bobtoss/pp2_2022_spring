def solve(numheads, numlegs):
    y=2*numheads-(numlegs/2)
    x=(numlegs/4)-(y/2)
    x=int(x)
    y=int(y)
    return f"rabbits {x}, chicken {y}"
r,c=map(int,input().split())
print(solve(r,c))