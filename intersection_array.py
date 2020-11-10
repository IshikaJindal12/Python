t=int(input("Enter number of testcases: "))
for i in range(t):
    n=input("Enter size of array1: ")
    arr1=input("Enter elements of array1: ").split(" ")
    m=input("Enter size of array2: ")
    arr2=input("Enter elements of array2: ").split(" ")
    for x in arr1:
        if x in arr2:
            print(x,end=" ")
