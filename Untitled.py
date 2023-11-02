#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt


# In[3]:


df = pd.read_csv("Diwali Sales Data.csv", encoding = 'unicode_escape')


# In[5]:


df.shape


# In[6]:


df.head()


# In[8]:


df.info()


# In[10]:


df.drop(['Status', 'unnamed1'], axis =1 , inplace= True)


# In[14]:


pd.isnull(df).sum()


# In[16]:


df.shape


# In[17]:


df.dropna(inplace=True)


# In[18]:


df.shape


# In[19]:


df['Amount'] = df['Amount'].astype('int')


# In[20]:


df['Amount'].dtypes


# In[21]:


df.columns


# In[22]:


df.describe()


# # Exploratory Data Analysis

# In[24]:


df.to_csv('cleaned_diwali_data.csv', index=False)


# In[ ]:




