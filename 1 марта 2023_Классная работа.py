#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# stats models: regression fitting via formulas
import statsmodels.formula.api as smf
# stats models: regression fitting via matrices of regression design
import statsmodels.api as sm


# In[2]:


df = pd.read_csv('https://raw.githubusercontent.com/artamonoff/Econometrica/master/python-notebooks/data-csv/sleep75.csv')


# In[4]:


df


# # Спецификация
# $$
# sleep = \beta_0 + \beta_1*totwrk + \beta_2 * male
# $$

# In[8]:


# специфицируем модель через формулу
sleep_eq1 = smf.ols(formula='sleep~totwrk+male', data=df).fit()
# Коэфициенты модели с округление
sleep_eq1.params.round(2)


# $$
# sleep = 3573.2 -0.17*totwrk + 88.84 * male
# $$

# 1. При увеличении количества рабочего времени на одну минуту в неделю количество сна уменьшается на 0.17 минут в неделю при прочих равных
# 2. Мужчины спят на 88.84 минуты в неделю больше женщин

# In[9]:


df = pd.read_csv('https://raw.githubusercontent.com/artamonoff/Econometrica/master/python-notebooks/data-csv/Labour.csv')
df


# In[12]:


# специфицируем модель через формулу
output_eq1 = smf.ols(formula='np.log(output)~np.log(capital)+np.log(labour)', data=df).fit()
# Коэфициенты модели с округление
output_eq1.params.round(3)


# $$
# log(output) = -1.711+0.208*capital+0.715*labour
# $$

# 1. При увеличении капитала на 1% выпуск увеличивается на 0.208%
# 2. При увеличении числа сотрудников на 1% выпуск увеличивается на 0.715%

# In[13]:


# специфицируем модель через формулу
output_eq1 = smf.ols(formula='np.log(output)~np.log(capital)+np.log(labour)+np.log(wage)', data=df).fit()
# Коэфициенты модели с округление
output_eq1.params.round(3)


# $$
# log(output) = -5.007+0.149*capital+0.720*labour+0.921*wage
# $$

# 1. При увеличении капитала на 1% выпуск увеличивается на 0.149%
# 2. При увеличении числа сотрудников на 1% выпуск увеличивается на 0.720%
# 3. При увеличении зарплаты на одного сотрудника на 1% выпуск увеличивается на 0.921%

# In[ ]:




