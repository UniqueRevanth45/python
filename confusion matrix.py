#!/usr/bin/env python
# coding: utf-8

# In[13]:


from sklearn import metrics
C="Cat"
D="Dog"
F="Fox"
G="Monkey"
y_true=[C,C,C,C,C,F,F,F,F,F,F,F,F,F,F,D,D,D,D,D,D,D,D,D,D,G,G,G,G,G,G]
y_pred=[C,C,C,C,D,F,C,C,C,C,C,C,D,D,F,C,C,C,C,D,D,D,D,D,D,G,G,G,G,G,G]
print(metrics.confusion_matrix(y_true,y_pred))


# In[14]:


print(metrics.accuracy_score(y_true,y_pred))


# In[17]:


print(metrics.classification_report(y_true,y_pred))


# In[ ]:




