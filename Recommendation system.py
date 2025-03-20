#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


file_path="C:\Movie.csv"


# In[4]:


df=pd.read_csv(file_path)


# In[5]:


df[0:5]


# In[6]:


len(df.userId.unique())


# In[7]:


len(df.movie.unique())


# In[8]:


user_movies_df=df.pivot(index='userId',columns='movie',values='rating')


# In[34]:


user_movies_df


# In[35]:


user_movies_df.fillna(0,inplace=True)


# In[36]:


user_movies_df


# In[37]:


user_movies_df.index=df.userId.unique()


# In[38]:


user_movies_df


# In[39]:


from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation
vec1=[5,4,0,0]
vec2=[4,5,3,0]
correlation_distance=correlation(vec1,vec2)
correlation_distance


# In[40]:


user_sim=1-pairwise_distances(user_movies_df.values,metric='cosine')
user_sim


# In[41]:


user_sim_df=pd.DataFrame(user_sim)
user_sim_df


# In[42]:


user_sim_df.index=df.userId.unique()
user_sim_df


# In[43]:


user_sim_df.iloc[0:5,0:5]


# In[44]:


np.fill_diagonal(user_sim,0)
user_sim_df.iloc[0:5,0:5]


# In[45]:


user_sim_df.idxmax(axis=1)


# In[46]:


df[(df['userId']==6)]


# In[47]:


[(df['userId']==168)]


# In[48]:


user1=df[df['userId']==6]


# In[49]:


user2=df[df['userId']==168]


# In[50]:


user1.movie


# In[51]:


user2.movie


# In[52]:


pd.merge(user1,user2,on='movie',how='outer')


# In[ ]:




