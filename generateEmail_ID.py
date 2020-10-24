name=str(input("Enter your name: "))
roll_no=str(input("Roll number: "))
branch=str(input("Branch: "))
batch=str(input("Batch: "))
temp=roll_no[-4:]
temp1=batch[-2:]
email=name+temp+"."+branch+temp1+"@chitkara.edu.in"
print(email)
