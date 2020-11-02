n=int(input("Enter the number you want to check: "))
try:
    assert n%2==0
except:
    print("Not an even number")
else:
    result=1/n
    print(result)
finally:    
    print("I am out of program")
