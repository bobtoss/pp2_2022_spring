def rev(s):
    c=""
    for i in s:
        c=c+" "+i
    c=c+" ->"
    for i in s[::-1]:
        c=c+" "+i
    print(c.strip())
    exit()
s=input().split()
print(rev(s))
