def unique(list):
    list.sort()
    for i in range(len(list)-1):
        if list[i]==list[i+1]:
            list.pop(i+1)
            i-=1
    return list
list=list(map(int,input().split()))
unique(list)
print(*list)