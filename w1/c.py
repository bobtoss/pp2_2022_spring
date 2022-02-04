def toLowercase (  s ) :
    c=""
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            i=chr(ord(i)+32)
            c=c+i
        else:
            c=c+i
    print(c)

s=input()
toLowercase(s)
