#!/usr/bin/env python
# coding: utf-8

# # Day 4: Write a Python program to calculate the sum of all even numbers between 1 and a given positive integer n

# In[2]:


def even(num):
    sum=0
    for i in range(0,num,2):
        sum=sum+i
    return sum
num=int(input())
even(num)


# In[ ]:




