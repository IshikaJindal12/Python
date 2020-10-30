quantity=float(input("Enter quantity: "))
total=quantity*100
if(total>1000):
    total=total-total*10/100
print("Price after discount is: ",total)
