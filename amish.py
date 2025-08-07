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

from matplotlib import pyplot as plt
a.plot(kind='bar', x='A', y='B')    
plt.title('Bar Plot of B by A')
plt.xlabel('A')
plt.ylabel('B')     
plt.show()
a.plot(kind='line', x='A', y='C')
plt.title('Line Plot of C by A')
plt.xlabel('A')

plt.ylabel('C')
plt.show()
a.plot(kind='scatter', x='A', y='B')
plt.title('Scatter Plot of B by A')
plt.xlabel('A')
plt.ylabel('B')

plt.show()
a.plot(kind='hist', y='C', bins=5)
plt.title('Histogram of C')
plt.xlabel('C')
plt.ylabel('Frequency')
plt.show()  
a.plot(kind='box')
plt.title('Box Plot of DataFrame')
plt.show()
a.plot(kind='area', x='A', y='B')
plt.title('Area Plot of B by A')
plt.xlabel('A')
plt.ylabel('B')
plt.show()  

a.plot(kind='pie', y='C', labels=a['A'], autopct='%1.1f%%')

plt.title('Pie Chart of C by A')

plt.ylabel('C')
plt.show()      
a.to_csv('amish.csv', index=False)  # Save DataFrame to CSV
import seaborn as sns
sns.heatmap(a.corr(), annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()
import numpy as np
a['D'] = np.random.rand(len(a))  # Add a new column with random
a['E'] = np.random.randint(1, 10, size=len(a))  # Add another column with random integers
print(a)
print(a.describe())  # Describe the updated DataFrame
print(a.info())  # Info of the updated DataFrame
print(a.dtypes)  # Data types of the updated DataFrame
print(a.shape)  # Shape of the updated DataFrame

print(a.head())  # First few rows of the updated DataFrame
print(a.tail())  # Last few rows of the updated DataFrame
