#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)

d = pd.DataFrame({
    'value': np.concatenate([np.random.normal(0, 1, 100), np.random.normal(10, 1, 10)])
})
q1 = d['value'].quantile(0.25)
q3 = d['value'].quantile(0.75)
iq = q3 - q1
lowerbound = q1 - 1.5 * iq
upperbound = q3 + 1.5 * iq
outliers = d[(d['value'] < lowerbound) | (d['value'] > upperbound)]
print("Outliers:")
print(outliers)
plt.figure(figsize=(10, 6))
plt.boxplot(d['value'], vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.scatter(outliers['value'], np.ones(len(outliers)), color='red', label='Outliers', zorder=3)
plt.title('Boxplot with Outliers')
plt.xlabel('Value')
plt.legend()
plt.show()


# In[ ]:




