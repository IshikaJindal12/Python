str=input("Enter your string: ")
dict={}
for i in str:
    dict[i]=dict.get(i,0)+1
BC=0
BE=None
for key,value in dict.items():
    if(BC is None or BC < value):
        BC=value
        BE=key
print(BE,BC)
