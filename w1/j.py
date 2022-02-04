s=input()
list=s.split()
c=""
for i in list:
    if len(i)>=3:
       c=c+" "+i
print(c.strip()) 