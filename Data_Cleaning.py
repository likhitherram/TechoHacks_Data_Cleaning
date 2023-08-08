#importing the libraries
import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\LIKHITH\Desktop\python_ws\test.csv")
df

#Identifying Missing Values
df.isnull().sum()
df.head()

#Handling Problem of Missing Values
df.dropna()

#Identifying Outliers
df.plot.box()
df.plot.scatter('Age','Fare')

#Removing Outliers
df=df[df['Fare']<300]
df.plot.scatter('Age','Fare')
