list=[]
n=int(input("Enter number of elements: "))
for num in range(n):
    num=int(input("Enter element: "))
    list.append(num)
list1=[]
for num1 in list:
    n=num1*num1
    list1.append(n)
print(list1)    
