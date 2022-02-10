s=input()
c=""
i=0
while i!=len(s):
    if s[i]=="," or s[i]=="!" or s[i]==":" or s[i]=="." or s[i]=="?":
        i=i+1
    else:
        c=c+s[i]
        i+=1
list=c.split()
dic={}
for i in list:
    dic[i]=0
print(len(dic))
for key,value in sorted(dic.items()):
    print(key)