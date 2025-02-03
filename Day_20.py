#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from spellchecker import SpellChecker
df = pd.read_csv("C:\Datasetss\Day 20_E-Commerce_Data.csv")
missing_data = df.isna().sum()
missing_percentage = (df.isna().sum() / len(df)) * 100
print("Missing Data Summary:")
print(missing_data)
print("\nPercentage of Missing Data:")
print(missing_percentage)
numerical_columns = ['Customer_Age', 'Rating']
imputer_num = SimpleImputer(strategy='median')
df[numerical_columns] = imputer_num.fit_transform(df[numerical_columns])
df['Review_Text'] = df['Review_Text'].fillna('No Review')
df['Product_Category'] = df['Product_Category'].fillna(df['Product_Category'].mode()[0])

# Checking for duplicates
duplicates = df[df.duplicated()]
print(f"\nFound {len(duplicates)} duplicate reviews.")
df = df.drop_duplicates()
df['Rating'] = df['Rating'].apply(lambda x: max(1, min(5, x)))
spell = SpellChecker()
df['Product_Category'] = df['Product_Category'].apply(lambda x: ' '.join([spell.correction(word) for word in x.split()]))
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Product_Price', 'Rating']])
plt.title('Boxplot for Product_Price and Rating')
plt.show()
for col in ['Product_Price', 'Rating']:
    lower_quantile = df[col].quantile(0.01)
    upper_quantile = df[col].quantile(0.99)
    df[col] = np.where(df[col] < lower_quantile, lower_quantile, df[col])
    df[col] = np.where(df[col] > upper_quantile, upper_quantile, df[col])
label_encoder = LabelEncoder()
df['Product_Category'] = label_encoder.fit_transform(df['Product_Category'])
scaler = MinMaxScaler()
df[['Product_Price', 'Rating']] = scaler.fit_transform(df[['Product_Price', 'Rating']])
missing_after_cleaning = df.isna().sum()
print("\nMissing values after cleaning:")
print(missing_after_cleaning)
if missing_after_cleaning.sum() > 0:
    print("\nImputing remaining missing values...")
    df[numerical_columns] = imputer_num.fit_transform(df[numerical_columns])
    df['Product_Category'] = df['Product_Category'].fillna(df['Product_Category'].mode()[0])
    df['Review_Text'] = df['Review_Text'].fillna('No Review')
    missing_after_imputation = df.isna().sum()
    print("\nMissing values after imputation:")
    print(missing_after_imputation)
if df.isna().sum().sum() > 0:
    print("\nThere are still missing values. Reviewing specific rows with missing values...")
    missing_rows = df[df.isna().any(axis=1)]
    print(missing_rows)
df.to_csv('cleaned_ecommerce_reviews.csv', index=False)
print("\nData cleaning complete. The cleaned dataset has been saved as 'cleaned_ecommerce_reviews.csv'.")


# In[ ]:




