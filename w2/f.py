n=int(input())
thisdict={}
max=0
for i in range(n):
    s,t=input().split()
    t=int(t)
    if s not in thisdict.keys():
        thisdict[s]=t
    else:
        thisdict[s]+=t
for i in thisdict.values():
        if i>max:
            max=i
for key,value in sorted(thisdict.items()):
    if value==max:
            print(key,"is lucky!")
    else:
            print(key,"has to receive",max-value,"tenge")
