import re
def space(match):
    return match.group(1) + " " + match.group(2)
s=input()
txt="CamelCaseWithoutSpaces"
x=re.sub('(.+?)([A-Z])',space,txt)
print(x)