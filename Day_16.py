#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.impute import SimpleImputer
df = pd.read_csv("C:\Datasetss\Day_16_Healthcare_Data.csv")
missing_data = df.isna().sum()
missing_percentage = (df.isna().sum() / len(df)) * 100
print("Missing Data Summary:")
print(missing_data)
print(missing_percentage)
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
imputer_num = SimpleImputer(strategy='median')
df[numerical_columns] = imputer_num.fit_transform(df[numerical_columns])
categorical_columns = df.select_dtypes(include=['object']).columns
imputer_cat = SimpleImputer(strategy='most_frequent')
df[categorical_columns] = imputer_cat.fit_transform(df[categorical_columns])
duplicates = df[df.duplicated()]
print(f"\nFound {len(duplicates)} duplicate records.")
df = df.drop_duplicates()
plt.figure(figsize=(12, 8))
sns.boxplot(data=df[numerical_columns])
plt.title('Boxplot for Numerical Columns')
plt.show()
for col in numerical_columns:
    lower_quantile = df[col].quantile(0.01)
    upper_quantile = df[col].quantile(0.99)
    df[col] = np.where(df[col] < lower_quantile, lower_quantile, df[col])
    df[col] = np.where(df[col] > upper_quantile, upper_quantile, df[col])
df = pd.get_dummies(df, drop_first=True) 
scaler = MinMaxScaler()  
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])
assert df.isna().sum().sum() == 0, "There are still missing values in the dataset!"
assert df.duplicated().sum() == 0, "There are still duplicate records in the dataset!"
print("\nData Types Before Correction:")
print(df.dtypes)
df.to_csv('cleaned_healthcare_dataset.csv', index=False)
print("\nData cleaning complete. The cleaned dataset has been saved as 'cleaned_healthcare_dataset.csv'.")


# In[ ]:




