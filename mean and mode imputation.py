#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
data = {
    'square_feet_area': [8500, 9600, np.nan, 11250, np.nan, 9550, 14260, np.nan, 13830, 11500],  # Numeric
    'Year_built': [2003, 1976, 2001, np.nan, 1998, 2000, 2006, 1978, 1950, np.nan],  # Numeric
    'over_all_condition': [5, 8, 6, 7, np.nan, 7, 8, 6, np.nan, 7],  # Numeric
    'ready_to_move': ['Yes', 'No', 'NO', np.nan, 'No', np.nan, 'No', 'Yes', 'No', 'Yes'],  # Categorical (Yes/No)
    'Sale_price': [200000, 180000, 215000, 250000, 210000, 190000, 230000, 225000, 220000, 240000]  # Target Variable
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print(df.isnull().sum())
numeric_imputer = SimpleImputer(strategy="mean")
df[['square_feet_area', 'Year_built', 'over_all_condition']] = numeric_imputer.fit_transform(df[['square_feet_area', 'Year_built', 'over_all_condition']])
categorical_imputer = SimpleImputer(strategy='most_frequent')
df[['ready_to_move']] = categorical_imputer.fit_transform(df[['ready_to_move']])
print("\nDataFrame after replacing missing values with SimpleImputer (mean for numeric, mode for categorical):")
df


# In[ ]:




