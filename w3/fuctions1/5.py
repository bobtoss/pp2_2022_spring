def permut(arr,text,text1):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            b=arr[j]
            arr[j]=arr[i]
            arr[i]=b
            for k in arr:
                text1+=k
            text2=text1[::-1]
            if text2 not in arr2:
                arr2.append(text2)
            if text1 not in arr2:
                arr2.append(text1)
            arr=[]
            text1=""
            for k in text:
                arr.append(k)
    for i in arr2:
        print(i)
text1=""          
text=input()
arr=[]
arr2=[]
for i in text:
    arr.append(i)
permut(arr,text,text1)