def histogram(list):
    for i in list:
        for j in range(i):
            print("*",end="")
        print("")
    exit()
list=list(map(int,input().split()))
print(histogram(list))