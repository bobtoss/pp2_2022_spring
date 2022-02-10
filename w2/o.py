s=input()
s1=s.replace("+"," ")
s1=s1.split()
dict={}
cnt=3
step=0
dict['ONE']='1'
dict['TWO']='2'
dict['THR']='3'
dict['FOU']='4'
dict['FIV']='5'
dict['SIX']='6'
dict['SEV']='7'
dict['EIG']='8'
dict['NIN']='9'
dict['ZER']='0'
c1=''
c2=''
while cnt!=len(s1[0])+3:
    a=s1[0][step:cnt]
    for key,value in dict.items():
        if a==key:
            c1+=value
            break
    step+=3
    cnt+=3
step=0
cnt=3
while cnt!=len(s1[1])+3:
    a=s1[1][step:cnt]
    for key,value in dict.items():
        if a==key:
            c2+=value
            break
    step+=3
    cnt+=3
final=''
sum=int(c1)+int(c2)
for i in str(sum):
    for key,value in dict.items():
        if i==value:
            final+=key
print(final)



