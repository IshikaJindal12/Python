import pandas as pd
ser1=pd.Series([1,2,3,4],['USA','Germany','France','Italy'])
ser2=pd.Series([1,2,5,4],['USA','Paris','France','Italy'])
print(ser1+ser2)
