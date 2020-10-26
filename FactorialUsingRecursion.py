def fact(a):
    if(a==1):
        return 1
    else:
        return a*fact(a-1)
    
num=int(input("Enter a number: "))    
print("Factorial of a number is: ",fact(num))
