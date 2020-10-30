list=[]
flag=1
for i in range(1000,3001):
    flag=1
    n=i
    while(n!=0 and flag):
        r=n%10
        if(r%2!=0):
            flag=0
        n=n//10
    if(flag==1):
        list.append(i)
print(list)        
