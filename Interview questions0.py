#!/usr/bin/env python
# coding: utf-8

# In[126]:


import numpy as np
import pandas as pd
import datetime


# In[127]:


today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)


# In[128]:


today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print("Yesterday:",yesterday)
print("Today is:",today)
print("Tomorrow will be:",tomorrow)


# In[129]:


store_id=[5,7,9]
dates=[today,yesterday,tomorrow]


# In[130]:


sra=pd.DataFrame(columns=["index","store_id","date","sales"])


# In[131]:


sra


# In[132]:


import warnings
warnings.filterwarnings("ignore")


# In[133]:


for i in store_id:
    for j in dates:
         sra=sra.append({"store_id":i,"date":j},ignore_index=True)


# In[134]:


sra


# In[135]:


np.random.seed(151)
sra["sales"]=np.random.randint(300,3000,9)
sra["index"]=np.arange(0,9)


# In[136]:


sra


# # write a function that fetches the previous days sales as output once we give store_id&date as input?

# In[137]:


date0=[]
for i in sra["date"].astype(str):
    date0.append(i.split(" ")[0])
sra["date"]=date0


# In[138]:


sra


# In[160]:


def prev_sales(dataframe,store_id,date):
    san=dataframe[dataframe["store_id"]==store_id]
    for i,j,p in zip(san["store_id"],san["date"],san["index"]):
        if j==date:
            try:
                return san["sales"][p-1]
            except:
                return "data not found"


# In[161]:


sra


# In[164]:


prev_sales(sra,5,"2023-03-02")


# In[ ]:





# In[ ]:





# In[ ]:




