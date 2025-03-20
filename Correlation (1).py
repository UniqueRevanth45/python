#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv(r'C:\Users\yerra\OneDrive\Pictures\Desktop\car_price_dataset.csv')
df.head()


# In[4]:


f1="Engine_Size"
f2="Price"
correlation=df[f1].corr(df[f2])
print(f"correlation between {f1} and {f2}:{correlation:.2f}")


# In[5]:


f1="Owner_Count"
f2="Price"
correlation=df[f1].corr(df[f2])
print(f"correlation between {f1} and {f2}:{correlation:.2f}")


# In[6]:


f1="Doors"
f2="Price"
correlation=df[f1].corr(df[f2])
print(f"correlation between {f1} and {f2}:{correlation:.2f}")


# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
np.random.seed(42)

data = {
    'Study Hours': np.random.randint(1, 10, 50),
    'Marks': np.random.randint(50, 100, 50),
    'Screen Time':np.random.randint(1,7,50),
    'Travelling Time':np.random.randint(0,3,50),
    'Sleep Hours':np.random.randint(4,10,50)
}
df = pd.DataFrame(data)
correlation_matrix = df.corr()
f1="Study Hours"
f2="Marks"
correlation=df[f1].corr(df[f2])
print(f"correlation between {f1} and {f2}:{correlation:.2f}")
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()


# In[ ]:




