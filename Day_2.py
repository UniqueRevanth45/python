#!/usr/bin/env python
# coding: utf-8

# # """Create a List, tuple and Dictionary with 5 elements in it and how to access few elements based on the index. Try  with different examples"""

# In[17]:


l1=[34,'apple',4.567,78,456]
print(l1)#prints the list
print(l1[0])#prints the first element from the list
print(l1[-1])#prints the last element from the list
print(l1[0::])#prints the list from the starting index
print(l1[::-1])#prints the list in reverse
print(len(l1))#prints length of the list
print(l1[1:3])#Slicing the list
l2=[24,56,35]
print(l1+l2)#Concatenating the list


# In[5]:


t1=(24,45,67,'Alice',4.67)
print(t1)#prints the tuple
print(t1[0])#prints the first element from the tuple
print(t1[-1])#prints the last element from the tuple
print(t1[0::])#prints the tuple from the starting index
print(t1[::-1])#prints the tuple in reverse
print(len(t1))#prints length of the tuple
print(t1[2:3])#Slicing the tuple
t2=(34,76,70)
print(t1+t2)#Concatenating the tuple


# In[16]:


dict1={1:'English',2:'Hindi',3:'Telugu',4:'Tamil',5:'Kannada'}
print(dict1)#print the dictionary
print(dict1[1])#indexing
dict1[2]='Assamese'#modification
print(dict1.keys())#retrieving the keys
print(dict1.items())#retrieving the keys and values

