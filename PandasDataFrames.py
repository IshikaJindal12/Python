import numpy as np
import pandas as pd
from numpy.random import randn
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)
