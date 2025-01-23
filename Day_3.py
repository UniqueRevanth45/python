#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Day 3:Write a Python program that takes a student's marks in three subjects as input.
•	If the average is greater than or equal to 90, print "Grade: A".
•	If the average is between 80 and 89, print "Grade: B".
•	If the average is between 70 and 79, print "Grade: C".
•	Otherwise, print "Grade: Fail"."""


# In[1]:


sub1=int(input())
sub2=int(input())
sub3=int(input())
avg=(sub1+sub2+sub3)/2
if avg>=90:
    print("Grade: A")
elif 80<=avg<=89:
    print("Grade: B")
else:
    print("Grade: Fail")


# In[2]:


sub1=int(input())
sub2=int(input())
sub3=int(input())
avg=(sub1+sub2+sub3)/2
if avg>=90:
    print("Grade: A")
elif 80<=avg<=89:
    print("Grade: B")
else:
    print("Grade: Fail")

