
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd 
 
d = { 'NAME': ['Bob','Bart','Bobby'],
      'OCCUPATION': ['Lawyer','Programmer','Teacher']}
 
frame = pd.DataFrame(d, columns=['NAME','OCCUPATION'])
print(frame)