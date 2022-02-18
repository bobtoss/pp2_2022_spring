def has_33(list):
    for i in range(len(list)):
        if list[i]==3:
            j=i+1
            if list[j]==3:
                print("OK")
                exit()
            else:
                return False
        if i+1==len(list):
            return False
list=list(map(int,input().split()))
print(has_33(list))
