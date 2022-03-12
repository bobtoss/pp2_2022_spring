import re
s=input()
txt="afdfb"
x=re.findall('^a.+b$',txt)
print(x)