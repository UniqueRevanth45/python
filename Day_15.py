#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df = pd.read_csv(r"C:\Datasetss\Day_15_Healthcare_Data.csv")
print("Initial Dataset Info")
print(df.info())  
print("\nInitial Dataset Statistics")
print(df.describe())
print("\nMissing Data Summary")
missing_data = df.isna().sum()
missing_percentage = (df.isna().sum() / len(df)) * 100
print(missing_data)
print(missing_percentage)
plt.figure(figsize=(10, 6))
sns.heatmap(df.isna(), cbar=False, cmap='viridis')
plt.title('Missing Data Heatmap')
plt.show()
numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].mean())
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])
for col in categorical_columns:
    df[col] = df[col].astype('category').cat.codes
knn_imputer = KNNImputer(n_neighbors=5)
df_knn_imputed = pd.DataFrame(knn_imputer.fit_transform(df), columns=df.columns)
target_column = 'Heart_Disease'  
X = df.drop(columns=[target_column])
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
predicted_values = model.predict(X_test)
df.loc[y_test.index, target_column] = predicted_values
mean_before = df[target_column].mean()
std_before = df[target_column].std()
mean_after_knn = df_knn_imputed[target_column].mean()
std_after_knn = df_knn_imputed[target_column].std()
print(f"Before Imputation - Mean: {mean_before}, Std: {std_before}")
print(f"After KNN Imputation - Mean: {mean_after_knn}, Std: {std_after_knn}")
plt.figure(figsize=(10, 6))
sns.boxplot(data=[df[target_column], df_knn_imputed[target_column]], notch=True)
plt.xticks([0, 1], ['Before Imputation', 'After KNN Imputation'])
plt.title('Boxplot: Before and After Imputation')
plt.show()
plt.hist(df[target_column], bins=30, alpha=0.5, label='Before Imputation')
plt.hist(df_knn_imputed[target_column], bins=30, alpha=0.5, label='After KNN Imputation')
plt.legend()
plt.title('Histogram: Before and After Imputation')
plt.show()
df.to_csv('healthcare_dataset_imputed.csv', index=False)
df_knn_imputed.to_csv('healthcare_dataset_imputed_knn.csv', index=False)


# In[ ]:




