#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


# In[4]:


data = pd.read_csv(r"C:\Shipments_Data.csv")


# In[5]:


data


# In[6]:


display(data.head())
print("Missing Values:\n", data.isnull().sum())


# In[8]:


plt.figure(figsize=(8, 5))
sns.boxplot(x='Reached.on.Time_Y.N', y='Discount_offered', data=data, palette='coolwarm')
plt.title("Effect of Discount on Delivery Time")
plt.xlabel("Reached on Time (1 = Yes, 0 = No)")
plt.ylabel("Discount Offered")
plt.show()


# In[10]:


sns.pairplot(data[['Cost_of_the_Product', 'Discount_offered', 'Weight_in_gms', 'Customer_rating', 'Reached.on.Time_Y.N']], hue='Reached.on.Time_Y.N', palette='coolwarm')
plt.show()


# In[14]:


X = data.drop('Reached.on.Time_Y.N', axis=1)
y = data['Reached.on.Time_Y.N']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\n Classification Report:\n", classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))


# In[19]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, f_classif
data = pd.read_csv(r"C:\Shipments_Data.csv")
X = data.drop(columns=['Reached.on.Time_Y.N'])
y = data['Reached.on.Time_Y.N']
label_encoder = LabelEncoder()
categorical_cols = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']
for col in categorical_cols:
    X[col] = label_encoder.fit_transform(X[col])
if y.dtype == "object":
    y = label_encoder.fit_transform(y)
selector = SelectKBest(score_func=f_classif, k=5)
X_new = selector.fit_transform(X, y)
feature_scores = pd.Series(selector.scores_, index=X.columns).sort_values(ascending=False)
print("\n Feature Scores:\n", feature_scores)
selected_features = X.columns[selector.get_support()]
print("\n Selected Features:", selected_features.tolist())


# In[ ]:




