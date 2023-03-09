#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np # linear algebra 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# stats models: regression fitting via formulas
import statsmodels.formula.api as smf
# stats models: regression fitting via matrices of regression design
import statsmodels.api as sm


# In[3]:


df = pd.read_csv('https://raw.githubusercontent.com/artamonoff/Econometrica/master/python-notebooks/data-csv/Electricity.csv')


# In[4]:


df


# In[5]:


# специфицируем модель через формулу
output_eq1 = smf.ols(formula='np.log(cost)~np.log(q)', data=df).fit()
# Коэфициенты модели с округление
output_eq1.params.round(3)


# $$
# log(cost) = -3.841+0.836*log(q)
# $$

# При увеличении общего выпуска электроэнергии на 1% общие издержки увеличиваются на 0.836%

# In[6]:


# специфицируем модель через формулу
output_eq1 = smf.ols(formula='np.log(cost)~np.log(q)+np.log(pl)+np.log(pf)+np.log(pk)', data=df).fit()
# Коэфициенты модели с округление
output_eq1.params.round(3)


# $$
# log(cost) = -7.472+0.838*log(q)+ 0.044*log(pl)+0.713* log(pf)+0.188*log(pk)
# $$
# 

# 1. При увеличении общего выпуска электроэнергии на 1% общие издержки увеличиваются на 0.838%
# 2. При увеличении уровня зарплаты на 1% общие издержки увеличиваются на 0.044%
# 3. При увеличении цены на топливо на 1% общие издержки увеличиваются на 0.713%
# 4. При увеличении цены привлечения капитала на 1% общие издержки увеличиваются на 0.188%

# In[ ]:




