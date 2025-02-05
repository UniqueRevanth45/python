#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)  
data = np.random.randint(20, 81, 1000)
plt.hist(data, bins=15, edgecolor='black', color='skyblue')
plt.title('Histogram of Cancer Patients Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.show()


# In[ ]:




