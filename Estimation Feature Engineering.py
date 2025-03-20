#!/usr/bin/env python
# coding: utf-8

# In[2]:


from  pandas import read_csv
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE


# In[3]:


filename="C:\pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
name=['preg','plas','pres','skin','test','mass','pedi','age']
print(name)


# In[4]:


dataframe=read_csv(filename,names=names)
print(dataframe)


# In[5]:


array=dataframe.values
x=array[:,0:8]
y=array[:,8]


# In[6]:


model1=LogisticRegression(max_iter=400)
rfe=RFE(estimator=model1,n_features_to_select=3)
fit=rfe.fit(x,y)


# In[7]:


fit.n_features_


# In[8]:


fit.support_


# In[9]:


fit.ranking_


# In[ ]:




