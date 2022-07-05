#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sqlite3
import pandas as pd
df = pd.read_csv(r"C:\Users\李宏洋\Desktop\南洋理工大学人工智能项目\课程资源\第一节课\Course Materials_Week 1  2 Intro to NTU AI Lab  Regression  Decision Tree-20220705\DBS_SingDollar.csv")
c=sqlite3.connect(r"C:\Users\李宏洋\Desktop\南洋理工大学人工智能项目\课程资源\第一节课\Course Materials_Week 1  2 Intro to NTU AI Lab  Regression  Decision Tree-20220705\DBS.db")
df=df.iloc[:,2:4]
df.to_sql(name='DBS',con=c)
for row in c.execute("select * from DBS"):
    print(row)


# In[3]:


import pandas as pd
df = pd.read_csv(r"C:\Users\李宏洋\Desktop\南洋理工大学人工智能项目\课程资源\第一节课\Course Materials_Week 1  2 Intro to NTU AI Lab  Regression  Decision Tree-20220705\DBS_SingDollar.csv")
X=df.loc[:,["SGD"]]
Y=df.loc[:,["DBS"]]


# In[4]:


X


# In[5]:


Y


# In[6]:


from sklearn import linear_model


# In[7]:


model = linear_model.LinearRegression()


# In[8]:


model.fit(X,Y)


# In[9]:


model.coef_


# In[10]:


model.intercept_


# In[11]:


pred=model.predict(X)


# In[12]:


pred


# In[13]:


from sklearn.metrics import mean_squared_error


# In[14]:


rmse=mean_squared_error(Y,pred)**0.5


# In[15]:


rmse


# In[16]:


from sklearn import tree


# In[17]:


model=tree.DecisionTreeRegressor()


# In[18]:


model.fit(X,Y)


# In[19]:


pred=model.predict(X)


# In[20]:


rmse=mean_squared_error(Y,pred)**0.5


# In[21]:


rmse


# In[22]:


import joblib


# In[24]:


joblib.dump(model, "decision_tree")


# In[25]:


model = linear_model.LinearRegression()


# In[32]:


model.fit(X,Y)


# In[35]:


joblib.dump(model, "regression")


# In[36]:


model=joblib.load("regression")


# In[37]:


print(model.predict([[1.4]]))


# In[38]:


model=joblib.load("decision_tree")


# In[39]:


print(model.predict([[1.4]]))


# In[ ]:




