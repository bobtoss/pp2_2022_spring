import re
def camel(match):
    return match.group(1) + match.group(2).upper()
s=input()
txt="afdfb abcvd djbvjjds zxc_zxc asdf_asdf snake_case"
x=re.sub("(.*?)_([a-zA-Z])", camel, txt)
print(x)
