#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data={
    "age":[25,30,35,40,45],
    "height":[150,160,170,180,190],
    "weight":[50,60,70,80,90],
}
df=pd.DataFrame(data)
print("Original DataFrame")
print(df)
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
print("\nScaled DataFrame")
print(df_scaled)


# In[ ]:




