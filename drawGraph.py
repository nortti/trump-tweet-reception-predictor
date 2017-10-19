import plotly
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd

# Credential
plotly.tools.set_credentials_file(username='tringuyenminh23', api_key='Ujw0Z0wUWFUDAXiKEsZO')


# Process data
data = pd.read_json("json_data/realDonaldTrump.json")

l= []
y= []
for i in range(int(N)):
    y.append((2000+i))
    trace0= go.Scatter(
        x= data['favorite_count'],
        y= data['retweet_count'],
        mode= 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= 'rgba(255, 182, 193, .9)',
                    opacity= 0.3
                   ),
        name= y[i],
        text= data['text'])
    l.append(trace0);

layout= go.Layout(
    title= 'The Real Donald Trump',
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
fig= go.Figure(data=l, layout=layout)
plotly.offline.plot(fig)