#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("C:\Datasetss\Civil_Engineering_Regression_Dataset.csv")
print("First 5 rows of the dataset:")
print(df.head())
dependent_variable = "Construction Cost"
independent_variables = [col for col in df.columns if col != dependent_variable]
print("\nDependent Variable:", dependent_variable)
print("Independent Variables:", independent_variables)
print("\nMissing Values:")
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)
print("\nSummary Statistics:")
print(df.describe())
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Construction Data")
plt.show()


# In[ ]:




