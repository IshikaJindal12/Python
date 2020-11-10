str1=str(input("Enter string 1: "))
str2=str(input("Enter string 2: "))
if(len(str1)==len(str2)):
    lst1=list(str1)
    lst2=list(str2)
    lst1.sort()
    lst2.sort()
    if(lst1==lst2):
        print("true")
    else:
        print("false")
else:
    print("false")
