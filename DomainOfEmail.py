str=input("Enter your Email ID: ")
if "@" in str:
    result=str.split("@")
    print("Domain name of Email ID is: ",result[1])
else:
    print("Not a valid Email address")
