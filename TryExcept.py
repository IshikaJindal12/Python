list=[5,9,12,10,0,'a',"Hello",[5,7]]
for i in list:
    try:
        result=1/int(i)
        print("result is : ",result)
    except (ValueError,ZeroDivisionError):
        print("Exception raised due to string value or 0 value")
    except:
        print("Exception raised due to other problems")
