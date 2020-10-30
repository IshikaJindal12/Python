n=int(input("Enter number of elements: "))
list=[]
for i in range(0,n):
    num=int(input())
    list.append(num)
value=int(input("Enter value you want to remove: "))
for i in list:
    if(i==value):
        list.remove(i)
print(list)
