#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import the useful libraries.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


df = pd.read_csv('C:\\Users\\eEdge\\Desktop\\Products.csv')


# In[17]:


df.head(5)


# In[45]:


df.describe()


# **Insights from the above description:-**
# 
# * Only 14% of People reach till checkout page.
# * Only 2.74% of People make the successful purchase(assuming landing on the thankyou page is a successful sell.)
# * Around 11.4% of customers quit the website after landing on the checkout page(assuming landing on the thankyou page is a successful sell).
# * Only 25% of the customers generate 1110$ or more revenue.
# 

# ### Checking missing  values

# In[74]:


df.isnull().sum()


# No missing value

# In[18]:


df.info()


# **Date and revenue are inccoret datatype**

# In[19]:


df['date'] = pd.to_datetime(df["date"])


# In[10]:


df.dtypes


# In[20]:


df['revenue'] = pd.to_numeric(df['revenue'])


# In[28]:


df['device'].value_counts()


# In[140]:


sns.catplot(data = df, x = 'device', y = 'revenue', kind = 'bar')
print("Mobile Revenue",round(df[df['device'] == 'Mobile'].revenue.mean(),2))
print("Desktop Revenue",round(df[df['device'] == 'Desktop'].revenue.mean(),2))
plt.xlabel("Device")
plt.ylabel("Average Revenue")


# **Desktop users generate 5 times more revenue than mobile users**
# 
# * Hence the company should encourage customers to use the desktop version more by giving some promotions.

# In[137]:


sns.catplot(data = df, x = 'landing_page', y = 'revenue', kind = 'bar')
print("Average Revenue:- Landed on Home Page",round(df[df['landing_page'] == 'Home'].revenue.mean(),2))
print("Average Revenue:- Landed on Product Page",round(df[df['landing_page'] == 'Product'].revenue.mean(),2))


# In[109]:


round(((df[df['landing_page'] == 'Home'].revenue.mean())-(df[df['landing_page'] == 'Product'].revenue.mean()))*100/df[df['landing_page'] == 'Product'].revenue.mean(),2)


# **Customers who land on the home page generate 3.14% more revenue than those who land on the product page.**

# In[50]:


df['date'].nunique()


# In[52]:


plt.figure(figsize = (12,6))
sns.lineplot(data = df, x = 'date', y = 'revenue')


# In[85]:


#Converting date into day, month

df['day'] = pd.DatetimeIndex(df['date']).day
df['month'] = pd.DatetimeIndex(df['date']).month


# In[87]:


df['day_name'] = df['date'].dt.day_name()


# In[110]:


df['month_name'] = df['date'].dt.month_name()


# In[111]:


df


# In[73]:


plt.figure(figsize = (12,6))
sns.boxplot(data = df, x = 'day', y = 'revenue')


# **Date wise there is not significant change is revenue**

# In[113]:


plt.figure(figsize = (12,6))
sns.barplot(data = df, x = 'day_name', y = 'landing_pageviews')


# In[ ]:


plt.figure(figsize = (12,6))
sns.barplot(data = df, x = 'day_name', y = 'revenue')


# Sunday we traffic and more revenue compare to other days of the week.

# In[126]:


df['month_name'].value_counts().plot(kind = 'barh')


# In[130]:


df[['month_name','landing_page']].value_counts()


# In[135]:


df[['month_name','device']].value_counts()


# In[142]:


df[df['month_name'] == 'January'].revenue.mean()


# In[154]:


df[df['month_name'] == 'February'].revenue.mean()


# In[153]:


((df[df['month_name'] == 'January'].revenue.mean()-df[df['month_name'] == 'February'].revenue.mean())*100)/df[df['month_name'] == 'January'].revenue.mean()


# **Around 3.92% fall in February, this could be due to various reasons and data do not reveal any causation.**

# In[134]:


df.corr()


# In[151]:


plt.figure(figsize = (18,8))
sns.heatmap(df.corr(), annot = True, cmap = "Greens")


# **There is no significant finding in correlation with respect to revenue**

# ## Conclusion:-
# 
# 
# **Insights from the above description:-**
# 
# * Only 14% of People reach till checkout page.
# * Only 2.74% of People make the successful purchase(assuming landing on the thankyou page is a successful sell.)
# * Around 11.4% of customers quit the website after landing on the checkout page(assuming landing on the thankyou page is a successful sell).
# * Only 25% of the customers generate 1110$ or more revenue.
# 
# 
# **Desktop users generate 5 times more revenue than mobile users**
# 
# * Hence the company should encourage customers to use the desktop version more by giving some promotions.
# 
# 
# **Customers who land on the home page generate 3.14% more revenue than those who land on the product page.**
# 
# Sunday we traffic and more revenue compare to other days of the week.
# 
# **Around 3.92% fall in February, this could be due to various reasons and data do not reveal any causation.**
# 
# 
# 
# 

# ## What can be done to increase revenue
# 
# * Machine learning model can be build to understand the cause of revenue decline(But data is not enough for modeling) we need more data.
# 
# 
# * Company should encourage customers to use desktop(by providing some attractive offers) as it generates 5 times more revenue than mobile.**Maybe due to better layout of the desktop version customer finds it convenient**
# 
# 
# * Online ads can be run and links should be shared for the homepage because it generates 3.14% more revenue.**Maybe on the home page customer gets more offers/products listed and the customer ended up buying an extra product which he/she may not have intended to buy initially**
# 
