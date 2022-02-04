n=int(input())
for i in range(n):
    x=int(input())
    if x<=10:
        print(" Go to work!")
    elif x>10 and x<=25 :
        print(" You are weak")
    elif x>25 and x<=45 :
        print("Okay, fine")
    else :
        print(" Burn! Burn! Burn Young!")
