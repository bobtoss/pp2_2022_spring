n=int(input())
list=[]
i=0
while i<n:
    s=input()
    list.append(s)
    i=i+1

for i in range(len(list)):
    if list[i].find('@gmail.com')!=-1:
        s=""
        for x in list[i]:
            if x!='@':
                s=s+x
            elif x=='@':
                break
        print(s)