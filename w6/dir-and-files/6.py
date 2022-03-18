arr=list(map(chr, range(ord('A'), ord('Z')+1)))
for i in arr:
    s=i+'.txt'
    open(s, 'x')

