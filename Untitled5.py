#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import io


# In[2]:


some_string = '''sleep totwrk age male hrwage
3113   3438  32   1    7.07 
2920   5020  31   1    1.43 
2670   2815  44   1   20.53 
3083   3786  30   0    9.62 
3448   2580  64   1    2.75 
4063   1205  41   1   19.25 '''
some_string


# In[21]:


df = pd.read_csv(io.StringIO(some_string), sep='\s+' )
df


# In[22]:


import statsmodels.formula.api as smf
# подгонка прямой
fitted_line = smf.ols(formula='sleep~-1+totwrk', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[11]:


# подгонка прямой
fitted_line = smf.ols(formula='sleep~age', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[12]:


# подгонка прямой
fitted_line = smf.ols(formula='sleep~-1+age', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[38]:


df = pd.read_csv('https://raw.githubusercontent.com/artamonoff/Econometrica/master/python-notebooks/data-csv/Labour.csv')
df.shape


# In[39]:


df.head(15)


# In[40]:


# подгонка прямой
fitted_line = smf.ols(formula='np.log(output)~np.log(capital)', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[41]:


# подгонка прямой
fitted_line = smf.ols(formula='np.log(output)~-1+np.log(capital)', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[42]:


# подгонка прямой
fitted_line = smf.ols(formula='np.log(output)~np.log(labour)', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[43]:


# подгонка прямой
fitted_line = smf.ols(formula='np.log(output)~-1+np.log(labour)', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[44]:


# подгонка прямой
fitted_line = smf.ols(formula='np.log(output)~np.log(wage)', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[45]:


# подгонка прямой
fitted_line = smf.ols(formula='np.log(output)~-1+np.log(wage)', data=df).fit()
# коэффициенты с округлением
fitted_line.params.round(2)


# In[58]:


df = pd.read_csv('https://raw.githubusercontent.com/artamonoff/Econometrica/master/python-notebooks/data-csv/sleep75.csv')
df


# In[49]:


import seaborn as sns
sns.scatterplot(data=df, y='sleep', x='totwrk')


# In[50]:


sns.scatterplot(data=df, y='sleep', x='age')


# In[51]:


sns.regplot(data=df, y='sleep', x='totwrk', ci=None, order=2, line_kws={"color": "C1"})


# In[52]:


# подгонка параболы
fitted_pol = smf.ols(formula='sleep~totwrk+I(totwrk**2)', data=df).fit()
# коэффициенты с округлением
fitted_pol.params.round(2)


# In[53]:


# подгонка параболы
fitted_pol = smf.ols(formula='sleep~age+I(age**2)', data=df).fit()
# коэффициенты с округлением
fitted_pol.params.round(2)


# In[54]:


# подгонка параболы
fitted_pol = smf.ols(formula='sleep~totwrk+age', data=df).fit()
# коэффициенты с округлением
fitted_pol.params.round(2)


# In[55]:


df = pd.read_csv('https://raw.githubusercontent.com/artamonoff/Econometrica/master/python-notebooks/data-csv/Labour.csv')
df.shape


# In[57]:


# подгонка параболы
fitted_pol = smf.ols(formula='np.log(output)~np.log(capital)+np.log(labour)', data=df).fit()
# коэффициенты с округлением
fitted_pol.params.round(2)


# In[63]:


# подгонка параболы
fitted_pol = smf.ols(formula='sleep~totwrk', data=df).fit()
# коэффициенты с округлением
fitted_pol.params


# In[64]:


# подгонка параболы
fitted_pol = smf.ols(formula='totwrk~sleep', data=df).fit()
# коэффициенты с округлением
fitted_pol.params


# In[65]:


some_string = '''cost q pl pk pf
0.213   8   6869.470 64.945   18  
3.043  869  8372.960 68.227 21.067
9.406  1412 7960.900 40.692 41.530
0.761   65  8971.890 41.243 28.539
2.259  295  8218.400 71.940 39.200
1.342  183  5063.490 74.430 35.510
0.616   50  9204.240 90.470 32.070
0.489   14  5438.890 86.110 34.150
1.147   90  7189.670 79.101 21.503
7.549  2969 8183.340 80.657   9   
2.053  374  7884.940 82.485 26.301
0.636   67  6696.500 58.258 25.400
3.150  378  7895.430 60.277 42.468
10.314 1886 6833.930 67.680 25.600
5.849  1025 7093.320 68.227 22.279 '''
some_string


# In[66]:


df = pd.read_csv(io.StringIO(some_string), sep='\s+' )
df


# In[67]:


# подгонка параболы
fitted_pol = smf.ols(formula='cost~-1+q', data=df).fit()
# коэффициенты с округлением
fitted_pol.params


# In[68]:


# подгонка параболы
fitted_pol = smf.ols(formula='q~-1+cost', data=df).fit()
# коэффициенты с округлением
fitted_pol.params


# In[ ]:




