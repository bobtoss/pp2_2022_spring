s=input()
ok=True
list=[]
for i in s:
    if i=="{" or i=="(" or i=="[":
        list.append(i)
    else:
        if len(list)==0:
            ok=False
            break
        else:
            if i=="}" and list[-1]=="{":
                list.pop(-1)
            elif i=="]" and list[-1]=="[":
                list.pop(-1)
            elif i==")" and list[-1]=="(":
                list.pop(-1)
            else:
                ok=False
                break 
if len(list)==0 and ok==True:
    print("Yes")
else:
    print("No")
    