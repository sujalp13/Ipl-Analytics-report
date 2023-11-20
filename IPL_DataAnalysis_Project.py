#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data = pd.read_csv("IPL_2022.csv")


# In[3]:


data


# # number of matches won by each team in IPL

# In[4]:


figure = px.bar(data, x=data['match_winner'],title = "Number of matches won by IPL Teams")
figure.show()


# # Number of matches won by defending or chasing

# In[5]:


data['won_by'] = data[ 'won_by']. map({'Wickets': 'Chasing',
                                        'Runs' : 'Defending'})                                
won_by = data["won_by"].value_counts()
label = won_by.index
counts = won_by. values

colors = ['red', 'lightgreen']

fig = go.Figure(data=[go.Pie(labels= label, values = counts)])
fig.update_layout(title_text = "Number of matches won by defending or chasing")
fig. update_traces(hoverinfo = 'label+percent', textinfo = 'value', textfont_size = 30,
marker = dict(colors = colors, line = dict(color = 'black', width= 3)))


# # Best Bowler in IPL 2022

# In[16]:


figure = px.bar(data, x = data["best_bowling"],
                color = data['best_bowling'],
                title = "Best Bowler in IPL 2022")
figure.show()


# # Most Player of the match Awards in IPL 2022

# In[15]:


figure = px.bar(data, y = data["player_of_the_match"], 
                 color = data['player_of_the_match'],
                title = "Most Player of the match Awards in IPL 2022")
figure.show()


# # Top Scrorers in IPL 2022

# In[14]:


figure = px.bar(data,x = data ["top_scorer"],
                color = data['highscore'],
                title = "Top Scrorers in IPL 2022")
figure. show()


# In[ ]:




