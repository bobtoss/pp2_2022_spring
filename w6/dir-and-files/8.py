import os
s=input()
a='c:\\Users\\orazg\\OneDrive\\Рабочий стол\\pp2_2022_spring\\w6\\dir-and-files\\Z.txt'
if os.access(a, os.F_OK):
    os.remove(a)
else:
    print("Don't exist")