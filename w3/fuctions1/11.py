def pal(d):
    s=[]
    for i in d:
        s.append(i)
    c=s
    s.sort(reverse=True)
    if c==s:
        return True
    else:
        return False
s=input()
print(pal(s))