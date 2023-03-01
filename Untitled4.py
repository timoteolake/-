#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# stats models: regression fitting
import statsmodels.formula.api as smf
# data visualization
import seaborn as sns


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/artamonoff/Econometrica/master/python-notebooks/data-csv/Labour.csv')
df.shape


# In[3]:


df.head()


# In[4]:


sns.histplot(data=df, x='output')


# In[5]:



sns.histplot(data=df, x='output', log_scale=True)


# In[6]:


sns.histplot(data=df, x='capital')


# In[7]:


sns.histplot(data=df, x='capital', log_scale=True)


# In[8]:


sns.regplot(data=df, x='capital', y='output', ci=None, line_kws={"color": "r"})


# In[9]:


# подгонка прямой
fitted_line = smf.ols(formula='output~capital', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[10]:


sns.regplot(x=np.log(df['capital']), y=np.log(df['output']), ci=None, line_kws={"color": "r"})


# In[12]:


# подгонка прямой
fitted_line = smf.ols(formula='np.log(output)~-1+np.log(capital)', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[13]:


# подгонка прямой
fitted_line = smf.ols(formula='output~labour', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[14]:


# подгонка прямой
fitted_line = smf.ols(formula='output~-1+labour', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[19]:


sns.regplot(x=np.log(df['capital']), y=np.log(df['output']), ci=None, order=2, line_kws={"color": "r"})


# In[16]:


# подгонка прямой
fitted_polynom = smf.ols(formula='np.log(output)~np.log(capital)+I(np.log(capital)**2)', data=df).fit()
# коэффициенты с округлением
fitted_polynom.params.round(2)


# In[20]:


sns.regplot(x=np.log(df['output']), y=np.log(df['labour']), ci=None, order=2, line_kws={"color": "r"})


# In[21]:


# подгонка прямой
fitted_polynom = smf.ols(formula='np.log(output)~np.log(labour)+I(np.log(labour)**2)', data=df).fit()
# коэффициенты с округлением
fitted_polynom.params.round(2)


# In[ ]:




