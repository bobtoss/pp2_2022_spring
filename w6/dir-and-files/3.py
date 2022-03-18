import os
s=input()
if os.access(s, os.F_OK):
    for i in os.listdir(s):
        print(i)
else:
    print("Don't exist")