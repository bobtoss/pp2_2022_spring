s=input().split()
f = open('list.txt', 'w')
f.write('[')
cnt=1
for i in s:
    f.write(i)
    cnt+=1
    if cnt==len(s):
        break
    f.write(',')
f.write(']')
f.close()