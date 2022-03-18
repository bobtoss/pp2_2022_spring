def upper(s):
    for i in range(len(s)):
        cnt=0
        if ord(s[i])>=65 and ord(s[i])<=90:
            cnt+=1
    return cnt
def lower(s):
    for i in range(len(s)):
        cnt=0
        if ord(s[i])>=97 and ord(s[i])<=122:
            cnt+=1
    return cnt
s=input()
a=s
s=filter(upper,s)
print(len(list(s)))
a=filter(lower,a)
print(len(list(a)))