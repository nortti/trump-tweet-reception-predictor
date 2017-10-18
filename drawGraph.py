import plotly
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd
plotly.tools.set_credentials_file(username='tringuyenminh23', api_key='Ujw0Z0wUWFUDAXiKEsZO')
l= []
y= []
data= pd.read_json("json_data/realDonaldTrump.json")
print(list(data))
# Setting colors for plot.
N= 53
c= ['hsl('+str(h)+',50%'+',50%)' for h in np.linspace(0, 360, N)]

for i in range(int(N)):
    y.append((2000+i))
    trace0= go.Scatter(
        x= data['favorite_count'],
        y= data['retweet_count']+(i*1000000),
        mode= 'markers',
        marker= dict(size= 14,
                    line= dict(width=1),
                    color= c[i],
                    opacity= 0.3
                   ),name= y[i],
        text= data['text']) # The hover text goes here... 
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