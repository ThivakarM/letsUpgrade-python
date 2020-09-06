#!/usr/bin/env python
# coding: utf-8

# # List and default functions

# In[4]:


myList=["thiv",14,29.08,[1,3,2.4]]


# In[5]:


len(myList)


# In[6]:


myList.append(123)
print(myList)


# In[7]:


myList.pop()
print(myList)


# In[8]:


myList.index(14)
print(myList)


# In[9]:


numList=[3,45,221,44,22,1,46]
numList.sort()
print(numList)


# In[10]:


max(numList)


# In[11]:


myList.insert(3,'thiv')
print(myList)


# In[12]:


myList.count('thiv')


# In[13]:


myList.remove('thiv')


# In[14]:


print(myList)


# In[15]:


numList.reverse()
print(numList)


# In[16]:


list2=myList.copy()+numList
print(list2)


# # Dictionary and its default functions

# In[17]:


days={1:'sunday',2:'monday',3:'tuesday',4:'wednesday',5:'thursday',6:'friday',7:'saturday'}


# In[18]:


days.get(4)


# In[19]:


days[4]


# In[20]:


days.items()


# In[21]:


days.keys()


# In[22]:


days.values()


# In[23]:


days.update({0:'unknown'})


# In[24]:


print(days)


# In[25]:


days.pop(0)


# In[26]:


print(days)


# # Sets and its default functions

# In[27]:


mySet={1,3,4,56,32,21}


# In[28]:


mySet1={1,3,58,98,234}


# In[29]:


mySet.add(75)
print(mySet)


# In[30]:


set3=mySet.difference(mySet1)


# In[31]:


print(set3)


# In[32]:


set3=mySet.intersection(mySet1)


# In[33]:


print(set3)


# In[35]:


set3.issubset(mySet)


# In[36]:


mySet.issuperset(set3)


# In[38]:


set3=mySet.union(mySet1)


# In[39]:


print(set3)


# In[40]:


set3.intersection_update(mySet)


# In[41]:


print(set3)


# # Strings and default functions
# 

# In[42]:


string='hello welcome'
print(string)


# In[43]:


string.capitalize()


# In[45]:


string.upper()


# In[47]:


string=string+', how are you?'


# In[48]:


print(string)


# In[54]:


string=string.capitalize()


# In[55]:


string=string.swapcase()
print(string)


# In[56]:


mylist=string.split(' ')
print(mylist)


# In[57]:


string.isdigit()


# In[58]:


string.isalnum()


# In[59]:


string.isalpha()


# In[63]:


str2='1234'
str3=string.join(str2)


# In[64]:


print(str3)


# In[65]:


string.find('HOW')


# In[67]:


string.replace('HOW','WHO')


# In[68]:


string


# In[69]:


string[1].isupper()


# In[ ]:




