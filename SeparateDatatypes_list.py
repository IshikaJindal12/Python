list=[1,4.5,"say",67,3.45,12,6.987,"python","data"]
list1=[]
list2=[]
list3=[]
for i in list:
    if (type(i)==int):
        list1.append(i)
    elif (type(i)==float):
        list2.append(i)
    else:
        list3.append(i)
print(list1)
print(list2)
print(list3)
