#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv(r"C:\Datasetss\Day_8_sales_data.csv")
df
df.head(5)
df.describe()
total=df.groupby('Region')['Sales'].sum()
total
total_quantity_by_product = df.groupby('Product')['Quantity'].sum()
most_sold_product = total_quantity_by_product.idxmax()
print("Most Sold Product:", most_sold_product)
avg=df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100
average = df.groupby('Product')['Profit_Margin'].mean()
print("Average Profit Margin by Product:\n", average)



# In[ ]:




