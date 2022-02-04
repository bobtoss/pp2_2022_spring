s=input()
t=input()
list=[]
cnt=0
for i in range(len(s)):
    if s[i]==t:
        cnt=cnt+1
        list.append(i)

if cnt==1:
    print(list[0])
    exit()
else:
    print(list[0],list[len(list)-1])