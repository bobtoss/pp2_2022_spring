n=int(input())
set={}
for i in range(n):
    s=input()
    cap=0
    low=0
    num=0
    for j in range(len(s)):
        if ord(s[j])>=65 and ord(s[j])<=90:
            cap+=1
        elif ord(s[j])>=48 and ord(s[j])<=57:
            num+=1
        elif ord(s[j])>=97 and ord(s[j])<=122:
            low+=1
    if cap>0 and low>0 and num>0:
        set[s]=0
print(len(set))
for key,value in sorted(set.items()):
    print(key)
