#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\李宏洋\Desktop\南洋理工大学人工智能项目\课程资源\第一节课\Course Materials_Week 1  2 Intro to NTU AI Lab  Regression  Decision Tree-20220705\DBS_SingDollar.csv")


# In[5]:


c=sqlite3.connect(r"C:\Users\李宏洋\Desktop\南洋理工大学人工智能项目\课程资源\第一节课\Course Materials_Week 1  2 Intro to NTU AI Lab  Regression  Decision Tree-20220705\DBS.db")


# In[6]:


df=df.iloc[:,2:4]


# In[7]:


df


# In[8]:


df.to_sql(name='DBS',con=c)
for row in c.execute("select * from DBS"):
    print(row)


# In[9]:


c.close()


# In[ ]:




