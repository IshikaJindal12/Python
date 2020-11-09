import math
num=int(input("Enter a number in range 0 to 10: "))
class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
try:
    if num<0:
        raise ValueTooSmallError
    elif num>10:
        raise ValueTooLargeError
    else:
        print("Square root of the number entered is: ",math.sqrt(num))    
except ValueTooSmallError:
    print("You have entered a value less than 0")
except ValueTooLargeError:
    print("You have entered a value greater than 10")

    
