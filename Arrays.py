import numpy
n=int(input("Enter number of elements: "))
list=[]
for i in range(0,n):
    num=int(input())
    list.append(num)
arr=numpy.array(list)
flag=0
for i in arr:
    if(i!=0):
        flag=1
if(flag==1):
    print("Array have non-zero elements")
else:
    print("Array do not have non-zero elements")
