def true_cnt(tup):
    if tup.count('true')==len(tup):
        return True
    else:
        return False
tup=tuple(input().split())
if true_cnt(tup):
    print("Yes")
else:
    print("No")