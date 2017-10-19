import plotly as py
import plotly.graph_objs as go 
import pandas as pd

from datetime import datetime


data = pd.read_json("json_data/realDonaldTrump.json")
trace = go.Scatter(
    x = data.created_at, 
    y = data.favorite_count,
    text = data.text,)

fig_data = [trace]
layout = dict(
    title="Tweets' favorite count with slider",
    hovermode= 'closest',
    xaxis=dict(
        title = "Time",
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    ),
    yaxis=dict(
        title = "Favorite Count",
    )
)

fig = dict(data=fig_data, layout=layout)
py.offline.plot(fig, filename = 'favorite_graph')