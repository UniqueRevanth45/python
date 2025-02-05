#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
np.random.seed(10)
data = pd.DataFrame({'value': np.concatenate([np.random.normal(0, 10, 5000), np.random.normal(10, 1, 100)])})
Q1 = data['value'].quantile(0.25)
Q3 = data['value'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = data[(data['value'] < lower_bound) | (data['value'] > upper_bound)]
print("Outliers: ",outliers)


# In[ ]:




