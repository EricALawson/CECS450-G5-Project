
# coding: utf-8

# In[3]:


get_ipython().system('pip install plotly')


# In[11]:


get_ipython().system('python -m pip install --upgrade pip')


# In[1]:


import plotly.offline as pyo
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


task = pd.read_csv('E:/Additional Participant Data.csv')


# In[3]:


task.head()


# In[4]:


plt.plot(task.Task_Success)
plt.show()


# In[5]:


task.sort_values(["ID", "Task_Success"], axis=0, 
                 ascending=True, inplace=True) 
#for tree easy take viz =1, ontology=1 and for graph easy take viz=2 and ontology=1
#for tree hard take viz =1, ontology=2 and for graph hard take viz=2 and ontology=2


# In[6]:


pyo.plot([{
    'x' : task.ID,
    'y' : task.Task_Success
}])


# In[7]:


#plt.plot(pd.DataFrame[pd.DataFrame['Visualization'] == 1])
#https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/

#tree easy take viz =1, ontology=1
treeEasy = task[(task.Visualization == 1) & (task.Ontologies == 1)]
pyo.plot([{
    'x' : treeEasy.ID,
    'y' : treeEasy.Task_Success
}])


# In[57]:


#graph easy take viz=2 and ontology=1
graphEasy = task[(task.Visualization == 2) & (task.Ontologies == 1)]
pyo.plot([{
    'x' : graphEasy.ID,
    'y' : graphEasy.Task_Success
}])


# In[58]:


#tree hard take viz =1, ontology=2
treeHard = task[(task.Visualization == 1) & (task.Ontologies == 2)]
pyo.plot([{
    'x' : treeHard.ID,
    'y' : treeHard.Task_Success
}])


# In[59]:


#graph hard take viz=2 and ontology=2
graphHard = task[(task.Visualization == 2) & (task.Ontologies == 2)]
pyo.plot([{
    'x' : graphHard.ID,
    'y' : graphHard.Task_Success
}])


# In[17]:


#COMBINING
from plotly.subplots import make_subplots
treeEasy = task[(task.Visualization == 1) & (task.Ontologies == 1)]
TE = pyo.plot([{
    'x' : treeEasy.ID,
    'y' : treeEasy.Task_Success
}])
graphEasy = task[(task.Visualization == 2) & (task.Ontologies == 1)]
GE = pyo.plot([{
    'x' : graphEasy.ID,
    'y' : graphEasy.Task_Success
}])
treeHard = task[(task.Visualization == 1) & (task.Ontologies == 2)]
TH = pyo.plot([{
    'x' : treeHard.ID,
    'y' : treeHard.Task_Success
}])
graphHard = task[(task.Visualization == 2) & (task.Ontologies == 2)]
GH = pyo.plot([{
    'x' : graphHard.ID,
    'y' : graphHard.Task_Success
}])


# In[18]:


#from plotly.subplots import make_subplots
#import plotly.graph_objects as go

#fig = make_subplots(rows=2, cols=2,subplot_titles=("Tree - Easy", "Tree - Hard", "Graph - Easy", "Graph - Hard"))

#fig.add_trace(go.Scatter(x=treeEasy.ID,y = treeEasy.Task_Success),row=1, col=2)

#fig.add_trace(go.Scatter(x=treeHard.ID,y = treeHard.Task_Success),row=2, col=1)

#fig.add_trace(go.Scatter(x=graphEasy.ID,y = graphEasy.Task_Success),row=2, col=1)

#fig.add_trace(go.Scatter(x=graphHard.ID,y = graphHard.Task_Success),row=2, col=2)

#fig.update_layout(height=500, width=700,title_text="Multiple Subplots with Titles")

#fig.show()


# In[14]:


import plotly.graph_objects as go


# In[9]:


data1 = [go.Scatter(x= treeEasy.Visualization, y = treeEasy.Task_Success,)]


# In[10]:


layout1 = go.Layout(title = 'Tree - Easy')


# In[11]:


figure1 = go.Figure(data = data1, layout = layout1)


# In[12]:


pyo.plot(figure1)


# In[27]:


fig = make_subplots(rows=2, cols=2)

fig.add_trace(go.Scatter(x=treeEasy.ID,y=treeEasy.Task_Success),row=1, col=1)

fig.add_trace(go.Scatter(x=graphEasy.ID,y=graphEasy.Task_Success),row=2, col=1)
fig.add_trace(go.Scatter(x=treeHard.ID,y=treeHard.Task_Success),row=1, col=2)
fig.add_trace(go.Scatter(x=graphHard.ID,y=graphHard.Task_Success),row=2, col=2)

fig.update_layout(height=600, width=800, title_text="Subplots")
fig.show()

