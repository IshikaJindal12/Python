lst=["1","Hello","3.4","Bye"]
lst1=['google','facebook','microsoft','tesla','apple']
lst2=lst+lst1
rn=str(input("Roll num: "))
roll_num=list(rn)
lst2.extend(roll_num)
lst2.sort()
print(lst2)
