import re
def space(match):
    return match.group(1) + "_" + match.group(2).lower()
s=input()
txt="CamelCaseWithoutSpaces wordSpace"
x=re.sub('(.+?)([A-Z])',space,txt)
print(x)