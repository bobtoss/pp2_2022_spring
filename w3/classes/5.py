class account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposite(self,dep_money):
        cnt=dep_money
        if cnt>self.balance:
            print("not enough money on balance")
        else :
            self.dep_money=0
            self.dep_money+=cnt
            self.balance=self.balance-self.dep_money
            print(f"transfer {cnt} was successfully done",f"deposite money is {self.dep_money} and balance is {self.balance}")
    def withdraw(self,with_money):
        self.with_money=with_money
        if self.with_money>self.dep_money+self.balance:
            print("not enough money")
        else:
            if self.with_money>self.balance:
                self.dep_money=self.dep_money+self.balance-self.with_money
                self.balance=0
                print(f"balance is {self.balance}", f"deposite is {self.dep_money}")
            else:
                self.balance=self.balance-self.with_money
                print(f"balance is {self.balance}")
s=input().split()
s1=s[0]
x=int(s[1])
p1=account(s1,x)
p1.deposite(int(input()))
p1.withdraw(int(input()))

