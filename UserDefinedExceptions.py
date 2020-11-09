age=int(input("Enter your age: "))
class AgeTooSmallError(Exception):
    pass
try:
    if(age<18):
        raise AgeTooSmallError
    if(age>=18):
        print("Your age is: ",age)
except AgeTooSmallError:
    print("You entered age less than 18")
    age=int(input("Enter number greater than 18: "))
    while(age<18):
        age=int(input("Oops! Invalid input, Enter number greater than 18: "))
    print("Your age is: ",age)    
