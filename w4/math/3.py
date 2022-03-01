import math
num=int(input("Input number of sides: "))
lenght=float(input("Input the length of a side: "))
print((num*lenght**2)/4*math.tanh(180/num))