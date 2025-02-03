#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
file_path = r"C:\Datasetss\Day_18_Tours_and_Travels.csv"
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()
print("Missing Data Summary:")
print(df.isna().sum())
imputer = SimpleImputer(strategy='median')
for col in ['Customer_Age', 'Rating']:
    if col in df.columns:
        df[col] = imputer.fit_transform(df[[col]])
if 'Review_Text' in df.columns:
    df['Review_Text'].fillna('No Review', inplace=True)
df.drop_duplicates(inplace=True)
if 'Rating' in df.columns:
    df['Rating'] = df['Rating'].clip(1, 5)
for col in ['Package_Price', 'Rating']:
    if col in df.columns:
        lower_quantile, upper_quantile = df[col].quantile([0.01, 0.99])
        df[col] = np.clip(df[col], lower_quantile, upper_quantile)
if 'Tour_Package' in df.columns:
    label_encoder = LabelEncoder()
    df['Tour_Package'] = label_encoder.fit_transform(df['Tour_Package'].astype(str))
scaler = MinMaxScaler()
scale_columns = [col for col in ['Package_Price', 'Rating'] if col in df.columns]
if scale_columns:
    df[scale_columns] = scaler.fit_transform(df[scale_columns])
output_file = 'cleaned_travel_customer_reviews.csv'
df.to_csv(output_file, index=False)
print(f"Data cleaning complete. The cleaned dataset has been saved as '{output_file}'.")


# In[ ]:




