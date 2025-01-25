#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df=pd.read_csv(r"C:\Datasetss\Day_7_sales_data.csv")
df
df[df['Sales']>1000]
df['Profit_Per_Unit']=df['Profit']/df['Quantity']
df
df['High_Sales']=((df['Sales']>1000)=='Yes')
df







# In[ ]:




