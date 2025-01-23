#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data={'Name':['John','Alice','Bob','Diana'],
     'Age':[28,34,23,29],
     'Department':['HR','IT','Marketing','Finance'],
     'Salary':[45000,60000,35000,50000]}
df=pd.DataFrame(data)
df


# In[3]:


df.head(2)


# In[5]:


df['Bonus']=df['Salary']*0.1
print(df)


# In[6]:


df['Salary'].mean()


# In[7]:


df[df['Age']>25]

