
a=1
dates=[]
while a==1:
    date=input()
    if date=="0":
        break
    date=date.split()
    date[0],date[2]=date[2],date[0]
    dates.append(date)
dates.sort()
for i in range(len(dates)):
    dates[i][0],dates[i][2]=dates[i][2],dates[i][0]
for i in dates:
    print(*i)