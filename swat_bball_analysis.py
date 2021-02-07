#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


df = pd.read_csv(r'raw_trends1.csv')


# In[3]:


df.head()


# In[4]:


ad = pd.read_csv(r'agg_data.csv')


# In[5]:


ad.head()


# In[6]:


rb_1920 = pd.read_csv(r'rb_1920.csv')


# In[7]:


rb_1920.head(10)


# In[8]:


pd.to_numeric(rb_1920.iloc[35][1])-pd.to_numeric(rb_1920.iloc[35][2])


# In[9]:


rb_1819 = pd.read_csv(r'rb_1819.csv')


# In[10]:


rb_1718 = pd.read_csv(r'rb_1718.csv')


# In[11]:


rb1 = []
rb1_gf = []
rb1_ga = []
rb2 = []
rb2_gf = []
rb2_ga = []
rb3 = []
rb3_gf = []
rb3_ga = []
rounds = np.arange(1,11)


# In[12]:


for i in range(1,20,2):
    b = pd.to_numeric(rb_1920.iloc[35][i])
    c = pd.to_numeric(rb_1920.iloc[35][i+1])
    a = b-c
    rb1.append(a)
    rb1_gf.append(b)
    rb1_ga.append(c)


# In[13]:


print(rb1)


# In[14]:


for i in range(1,20,2):
    b = pd.to_numeric(rb_1819.iloc[36][i])
    c = pd.to_numeric(rb_1819.iloc[36][i+1])
    a = b-c
    rb2.append(a)
    rb2_gf.append(b)
    rb2_ga.append(c)


# In[15]:


for i in range(1,20,2):
    b = pd.to_numeric(rb_1718.iloc[34][i])
    c = pd.to_numeric(rb_1718.iloc[34][i+1])
    a = b-c
    rb3.append(a)
    rb3_gf.append(b)
    rb3_ga.append(c)


# In[16]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=rounds, y=rb1,
                    mode='lines+markers',
                    name='19_20'))
fig.add_trace(go.Scatter(x=rounds, y=rb2,
                    mode='lines+markers',
                    name='18-19'))
fig.add_trace(go.Scatter(x=rounds, y=rb3,
                    mode='lines+markers', name='17-18'))

fig.show()


# In[17]:


print(np.std(rb1))
print(np.std(rb2))
print(np.std(rb3))


# ## Swarthmore's 19-20 teams looks the most balanced out of the past 3 seasons, as seen by the lowest sd of point difference in rounds; they fell off quite hard in the two earlier seasons but they have seemingly gotten better at sealing off the game

# In[18]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=rounds, y=rb1_gf,
                    mode='lines+markers',
                    name='19_20'))
fig.add_trace(go.Scatter(x=rounds, y=rb2_gf,
                    mode='lines+markers',
                    name='18-19'))
fig.add_trace(go.Scatter(x=rounds, y=rb3_gf,
                    mode='lines+markers', name='17-18'))
fig.update_layout(title='Goals scored by Swarthmore (by rounds)')
fig.show()


# ## can see dips in rounds 2 and 7; in the 19-20 season, the team started slower but grew into the game better as well as finishing off a lot stronger than they did in 18-19

# In[19]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=rounds, y=rb1_ga,
                    mode='lines+markers',
                    name='19_20'))
fig.add_trace(go.Scatter(x=rounds, y=rb2_ga,
                    mode='lines+markers',
                    name='18-19'))
fig.add_trace(go.Scatter(x=rounds, y=rb3_ga,
                    mode='lines+markers', name='17-18'))
fig.update_layout(title='Goals conceded by Swarthmore (by rounds)')
fig.show()


# ## seems like per-round defensive performance hasn't changed much over the past 3 seasons

# In[ ]:




