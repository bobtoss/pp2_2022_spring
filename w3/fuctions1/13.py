import random
n=random.randint(1,20)
def guess():
    print("Hello! What is your name?")
    name=input()
    print()
    print("Well,",name,"I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    i=0
    cnt=0
    while i==0:
        num=int(input())
        print()
        if num>n:
            print("Your guess is too high.")
            print("Take a guess.") 
            cnt+=1
        elif num<n:
            print("Your guess is too low.")
            print("Take a guess.")
            cnt+=1
        else:
            print("Good job, KBTU! You guessed my number in",cnt,"guesses!")
            exit()
guess()