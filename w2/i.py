n=int(input())
disk=[]
taked=[]
for i in range(n):
    s=input()
    if s[0]=="1":
        s=s.split()
        disk.append(s[1])
    else:
        taked.append(disk[0])
        disk.pop(0)
print(*taked)
    
