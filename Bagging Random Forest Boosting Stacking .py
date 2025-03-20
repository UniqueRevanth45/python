#!/usr/bin/env python
# coding: utf-8

# In[14]:


from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


# In[15]:


filename="C:\pima-indians-diabetes.data.csv"


# In[16]:


names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8]
y = array[:, 8]
print(dataframe)
seed = 7
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)  # Shuffle enabled
cart = DecisionTreeClassifier()
num_trees = 100
model = BaggingClassifier(estimator=cart, n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold)
print(results.mean())


# In[17]:


#Random Forest
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier


# In[18]:


x=array[:,0:8]
y=array[:,0]


# In[19]:


num_trees=100
max_features=3


# In[20]:


KFold=KFold(n_splits=10,shuffle=True,random_state=7)


# In[21]:


model=RandomForestClassifier(n_estimators=num_trees,max_features=max_features)


# In[22]:


results=cross_val_score(model,x,y,cv=KFold)


# In[23]:


print(results.mean())


# In[ ]:




