def spy_game(list):
    for i in range(len(list)):
        if list[i]==0:
            for j in range(i+1,len(list)):
                if list[j]==0:
                    for m in range(j+1,len(list)):
                        if list[m]==7:
                            print("OK")
                            exit()
        if i+1==len(list):
            return False
list=list(map(int,input().split()))
print(spy_game(list))