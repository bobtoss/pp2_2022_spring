import re
s=input()
txt="a_b_c_d zxc_zxc abbbbbbb acd ab sabdA sabfbaF"
x=re.findall('[a-z]*[A-Z]',txt)
print(x)