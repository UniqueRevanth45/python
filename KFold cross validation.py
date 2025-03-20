#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BaggingClassifier

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
filename = "C:\pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8]
y = array[:, 8]
print(dataframe)
seed = 7
kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
cart = DecisionTreeClassifier()
num_trees = 100
model = BaggingClassifier(estimator=cart, n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold)
print(results.mean())


# In[2]:


#RandomForestClassifier

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
x=array[:,0:8]
y=array[:,8]
num_trees=100
max_features=3
kfold=KFold(n_splits=10,shuffle=True,random_state=7)
model=RandomForestClassifier(n_estimators=num_trees,max_features=max_features)
results=cross_val_score(model,x,y,cv=kfold)
print(results.mean())


# In[3]:


#AdaBoostClassifier

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import AdaBoostClassifier
import pandas as pd
filename = "C:\pima-indians-diabetes.data.csv"
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
model = AdaBoostClassifier(estimator=cart, n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, y, cv=kfold)
print(results.mean())


# In[ ]:




