#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
data=[5,7,7,8,9,10,10,10,11,12,11,11]
plt.hist(data, bins=10, edgecolor='black')
plt.title('Simple Histogram Example')
plt.xlabel('Numbers')
plt.ylabel('Count')
plt.show()


# In[ ]:




