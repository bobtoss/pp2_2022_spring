import re
s=input()
txt="afdfb abcvd djbvjjds "
x=re.sub('[\s,.]',':',txt)
print(x)