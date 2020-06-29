#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import bs4


# In[2]:


'http://books.toscrape.com/catalogue/page-2.html'


# In[3]:


'http://books.toscrape.com/catalogue/page-3.html'


# In[4]:


base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


# In[5]:


base_url.format('20')


# In[9]:


page_num = 18


# In[7]:


'http://books.toscrape.com/catalogue/page-{page_num}.html'


# In[10]:


base_url.format(page_num)


# In[12]:


res = requests.get(base_url.format(1))


# In[13]:


soup = bs4.BeautifulSoup(res.text,'lxml')


# In[14]:


soup


# In[15]:


soup.select(".product_pod")


# In[17]:


len(soup.select(".product_pod"))


# In[18]:


products = soup.select(".product_pod")


# In[19]:


example = products[0]


# In[20]:


example


# In[21]:


'star-rating Thr' in str(example)


# In[22]:


example.select(".star-rating.Two")


# In[23]:


example.select('a')


# In[24]:


example.select('a')[1]


# In[25]:


example.select('a')[1]['title']


# In[28]:


two_star_titles = []
for n in range(1,51):
   scrape_url = base_url.format(n)
   res = requests.get(scrape_url) 

   soup = bs4.BeautifulSoup(res.text, 'lxml')
   books = soup.select(".product_pod") 
   
   for book in books:
    if len(book.select('.star-rating.Two')) != 0:
        book_title = book.select('a')[1]['title']
        two_star_titles.append(book_title)
    


# In[29]:


two_star_titles


# In[ ]:




