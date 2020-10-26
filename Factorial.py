def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
    
num=int(input("Enter a number: "))    
print("Factorial of a number is: ",fact(num))
