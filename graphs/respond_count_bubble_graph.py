import plotly
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd

# Credential
plotly.tools.set_credentials_file(username='tringuyenminh23', api_key='Ujw0Z0wUWFUDAXiKEsZO')


# Process data
data = pd.read_json("json_data/realDonaldTrump.json")

# Calculate accumulate respond 
accumulate_responds = []
for i in range(len(data)):
    accumulate_responds.append(data.iloc[i]['retweet_count'] + data.iloc[i]['favorite_count'])

# Normalize accumulate_responds to use as size of bubble
accumulate_responds_normalized = [float(i)/max(accumulate_responds) for i in accumulate_responds]    
sizeref = 2*max(accumulate_responds_normalized)/(80**2)


fig_data = []
trace0= go.Scatter(
    x= data['favorite_count'],
    y= data['retweet_count'],
    mode= 'markers',
    marker= dict(
        symbol = 'circle',
        sizemode = 'area',
        sizeref = sizeref,
        size = accumulate_responds_normalized,
        line= dict(width=1),
        color= 'rgb(93, 164, 214)',
        opacity= 0.8),
    text= data['text'])
fig_data.append(trace0);

layout= go.Layout(
    title= str(data.iloc[0]['user']['name']) + "'s most recent tweets and respond count",
    hovermode= 'closest',
    xaxis= dict(
        title= 'Retweet Count',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Favorite Count',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)
fig = go.Figure(data = fig_data, layout=layout)
plotly.offline.plot(fig, filename = 'responds_count_bubble_graph.html')