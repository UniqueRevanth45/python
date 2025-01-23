#!/usr/bin/env python
# coding: utf-8

# In[4]:


n = int(input("Enter a positive integer: "))
print("Numbers from 1 to", n, "are:")
for i in range(1, n+1):
    print(i)
sum_of_numbers = 0
i = 1
while i <= n:
    sum_of_numbers += i
    i += 1
print("The sum of all numbers from 1 to", n, "is:", sum_of_numbers)


# In[5]:


def calculate_square(n):
    return n * n
n = int(input("Enter a positive integer: "))
square = calculate_square(n)
print("The square of", n, "is:", square)

