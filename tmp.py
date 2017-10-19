import plotly
import plotly.graph_objs as go 
import pandas as pd
import math 
import numpy as np


data = pd.read_json("json_data/realDonaldTrump.json")
accumulate_responds = []
for i in range(len(data)):
    accumulate_responds.append(data.iloc[i]['retweet_count'] + data.iloc[i]['favorite_count'])

accumulate_responds_normalized = [float(i)/max(accumulate_responds) for i in accumulate_responds]    
sizeref = 2*max(accumulate_responds_normalized)/(80**2)


l= []
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
l.append(trace0);

layout= go.Layout(
    title= "Donald Trump's most recent tweets and respond count",
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
fig = go.Figure(data=l, layout=layout)
plotly.offline.plot(fig, filename = 'overall_graph')
