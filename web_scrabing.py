#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests

result = requests.get("http://www.example.com")

type(result)

requests.models.Response


# In[2]:


result.text


# In[4]:


import bs4


# In[5]:


soup = bs4.BeautifulSoup(result.text,"lxml")


# In[6]:


soup


# In[10]:


soup.select('title')[0].getText()


# In[11]:


site_p = soup.select('p')


# In[12]:


site_p[0]


# In[13]:


type(site_p)


# In[14]:


site_p[0].getText()


# In[ ]:




