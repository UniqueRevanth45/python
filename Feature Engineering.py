#!/usr/bin/env python
# coding: utf-8

# In[24]:


from  pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd


# In[25]:


filename="C:\pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
name=['preg','plas','pres','skin','test','mass','pedi','age']
print(name)


# In[26]:


dataframe=read_csv(filename,names=names)
print(dataframe)


# In[27]:


array=dataframe.values
x=array[:,0:8]
y=array[:,8]
test=SelectKBest(score_func=chi2,k=5)
fit=test.fit(x,y)


# In[28]:


set_printoptions(precision=3)
print(fit.scores_)
features=fit.transform(x)

