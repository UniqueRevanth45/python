#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import loadtxt
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[2]:


dataset=loadtxt("C:\pima-indians-diabetes.data.csv",delimiter=",")
x=dataset[:,0:8]
y=dataset[:,8]


# In[3]:


seed=7
test_size=0.33
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=test_size,random_state=42)


# In[4]:


model=XGBClassifier()
model.fit(x_train,y_train)


# In[ ]:




