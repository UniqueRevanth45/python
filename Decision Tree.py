#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.model_selection  import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn import preprocessing


# In[2]:


file_name="C:\iris.csv"
iris=pd.read_csv('\iris.csv',index_col=0)


# In[3]:


iris.head()


# In[4]:


iris = iris.rename(columns={"Species": "Flower_types"})


# In[5]:


iris.head()


# In[6]:


x=iris.iloc[:,0:4]


# In[7]:


x


# In[8]:


y=iris['Flower_types']


# In[9]:


y


# In[10]:


colnames=list(iris.columns)


# In[11]:


colnames


# In[12]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)


# In[13]:


model=DecisionTreeClassifier(criterion='entropy',max_depth=3)


# In[14]:


model.fit(x_train,y_train)


# In[15]:


tree.plot_tree(model)


# In[16]:


fn=['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
cn=['setosa','versicolor','virginica']
fig,axes=plt.subplots(nrows=1,ncols=1,figsize=(4,4),dpi=300)
tree.plot_tree(model,feature_names=fn,class_names=cn,filled=True)


# In[17]:


preds=model.predict(x_test)
pd.Series(preds).value_counts()


# In[18]:


preds


# In[19]:


pd.crosstab(y_test,preds)


# In[20]:


np.mean(preds==y_test)


# In[21]:


#Regression
from sklearn.tree import DecisionTreeRegressor


# In[22]:


array=iris.values
x=array[:,0:3]
y=array[:,3]


# In[23]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=42)


# In[24]:


model=DecisionTreeRegressor()
model.fit(x_train,y_train)


# In[25]:


model.score(x_test,y_test)


# In[ ]:




