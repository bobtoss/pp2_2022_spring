n=int(input())
demons={}
for i in range(n):
    d,w=input().split()
    if w not in demons.keys():
        demons[w]=1
    else:
        demons[w]+=1
m=int(input())
hunters={}
for i in range(m):
    h,a,k=input().split()
    k=int(k)
    if a not in hunters.keys():
        hunters[a]=k
    else:
        hunters[a]+=k
left=0
for key,value in hunters.items():
    if key in demons and demons[key]>value:
        left=left+demons[key]-value
for key,value in demons.items():
    if key not in hunters:
        left+=value
print("Demons left:",left)