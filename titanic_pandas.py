#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.random import randn, randint, uniform, sample


# In[2]:


df = pd.read_csv('titanic.csv')
df


# In[3]:


df.shape


# In[4]:


df.isnull().sum()


# In[5]:


df.dropna()


# In[6]:


df


# In[7]:


df.dropna(thresh=4, axis=0)


# In[8]:


df


# In[9]:


df.fillna("New value")


# In[10]:


df['Age'].fillna("Empty")


# In[11]:


df['Age'] = df['Age'].fillna("Empty")
df


# In[12]:


df['Fare'].mean()


# In[13]:


df['Fare'].fillna(df['Fare'].mean())


# In[14]:


df.fillna(df.mean())


# In[16]:


df.set_index('PassengerId',inplace=True)
df


# In[17]:


df.head()


# In[18]:


df.head(19)


# In[19]:


df.isnull().sum()


# In[20]:


new_df =df.fillna(0)
new_df


# In[21]:


df.columns


# In[23]:


new_df=df.fillna({"Cabin":'no'})
new_df.head()


# In[25]:


df=new_df
df


# In[26]:


df1=df.fillna(method='ffill',limit=3)
df1.head(10)


# In[27]:


df1


# In[29]:


df1=df1.replace({'no':'yes'})
df1


# In[ ]:




