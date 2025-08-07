import pandas as pd
a=pd.DataFrame()
a['A']=[1,2,3]
a['B']=[4,5,6]
a['C']=[7,8,9]
print(a)
print(a.describe()) 
print(a.info())
print(a.dtypes) 
print(a.shape)
print(a.head())     
print(a.tail())
print(a.columns)        
print(a.index)
print(a.values)

print(a.T)
print(a.sort_values(by='B'))    
print(a.sort_values(by=['B','A'], ascending=[True, False]))
print(a.isnull())
print(a.dropna())
print(a.fillna(0))
print(a.duplicated())
print(a.drop_duplicates())
print(a.groupby('A').sum())

print(a.groupby('A').mean())
print(a.groupby('A').count())

print(a.groupby('A').max())
print(a.groupby('A').min())

    