def palindrome(s):
    for i,j in zip(s,reversed(s)):
        if i!=j:
            return False
    return True
s=input()
if palindrome(s):
    print("Yes")
else:
    print("No")