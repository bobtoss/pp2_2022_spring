def filter_prime(list):
    primes=[]
    for i in list:
        cnt=0
        for j in range(2,i):
            if i%j==0:
                cnt+=1
        if cnt==0:
            primes.append(i)
    print(*primes)
    exit()
list=list(map(int,input().split()))
print(filter_prime(list))

