#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from datetime import datetime
df = pd.read_csv("C:\Datasetss\Day 19_E-Commerce_Data.csv")
print("Initial Dataset Info:")
print(df.info())
missing_data = df.isna().sum()
missing_percentage = (df.isna().sum() / len(df)) * 100
print("\nMissing Data Summary:")
print(missing_data)
print("\nPercentage of Missing Data:")
print(missing_percentage)
plt.figure(figsize=(10, 6))
sns.heatmap(df.isna(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].median())
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])
df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df['Order_Date'] = df['Order_Date'].fillna(method='ffill')
knn_imputer = KNNImputer(n_neighbors=5)
df_imputed_knn = pd.DataFrame(knn_imputer.fit_transform(df[numerical_columns]), columns=numerical_columns)
print("\nBefore Imputation Summary:")
print(df.describe())
df_imputed_knn[numerical_columns] = df_imputed_knn[numerical_columns].fillna(df[numerical_columns].mean())
print("\nAfter KNN Imputation Summary:")
print(df_imputed_knn.describe())
plt.figure(figsize=(12, 6))
sns.histplot(df['Product_Price'], kde=True, color='blue', label='Before Imputation')
sns.histplot(df_imputed_knn['Product_Price'], kde=True, color='red', label='After KNN Imputation')
plt.legend()
plt.title('Histogram: Before and After KNN Imputation (Product_Price)')
plt.show()
plt.figure(figsize=(12, 6))
sns.boxplot(data=[df['Product_Price'], df_imputed_knn['Product_Price']], notch=True)
plt.xticks([0, 1], ['Before Imputation', 'After KNN Imputation'])
plt.title('Boxplot: Before and After KNN Imputation (Product_Price)')
plt.show()
label_encoder = LabelEncoder()
df['Product_Category'] = label_encoder.fit_transform(df['Product_Category'])
assert df.isna().sum().sum() == 0, "There are still missing values in the dataset!"
df.to_csv('cleaned_ecommerce_orders.csv', index=False)
df_imputed_knn.to_csv('cleaned_ecommerce_orders_knn.csv', index=False)
print("\nData cleaning complete. The cleaned dataset has been saved as 'cleaned_ecommerce_orders.csv' and 'cleaned_ecommerce_orders_knn.csv'.")


# In[ ]:




