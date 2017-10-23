import plotly as py
import plotly.graph_objs as go 
import pandas as pd
import numpy as np
import random

from datetime import datetime

data = pd.read_json("../json_data/realDonaldTrump.json")

# Normalize favorite_count and retweet_count with number of follower
favorite_count_normalized = []
retweet_count_normalized = []
for i in range(len(data)):
	follower_count = data.iloc[i]['user']['followers_count']
	favorite_count_normalized.append(follower_count / data.iloc[i]['favorite_count'])
	retweet_count_normalized.append(follower_count / data.iloc[i]['retweet_count'])

# Graph data
trace_favorite = go.Scatter(
    x = data.created_at, 
    y = favorite_count_normalized,
    name = 'Favorite Count',
    text = data.text,
    line = dict(color='#33CFA5'))
trace_favorite_average = go.Scatter(
	x = data.created_at, 
	y = [sum(favorite_count_normalized) / float(len(favorite_count_normalized))] * len(data.created_at),
	name = "Favorite Count Average",
	visible = False, 
	line = dict(color='#33CFA5', dash = 'dash'))


trace_retweet = go.Scatter(
    x = data.created_at, 
    y = retweet_count_normalized,
    name = 'Retweet Count',
    text = data.text,
    line=dict(color='#F06A6A'))
trace_retweet_average = go.Scatter(
	x = data.created_at, 
	y = [sum(retweet_count_normalized) / float(len(retweet_count_normalized))] * len(data.created_at),
	name = "Retweet Count Average",
	visible = False, 
	line = dict(color='#F06A6A', dash = 'dash'))


fig_data = [trace_favorite, trace_favorite_average, trace_retweet, trace_retweet_average]


# Annotations
random_index = random.randrange(len(data))
retweet_annotations=[dict(x=data.created_at[random_index],
                    y=sum(retweet_count_normalized) / float(len(retweet_count_normalized)),
                    xref='x', yref='y',
                    text='Retweet Count Average:<br>'+str(sum(retweet_count_normalized) / float(len(retweet_count_normalized))),
                    ax=20, ay=-40),

                  	dict(x=data.created_at[np.argmax(retweet_count_normalized)],
                  	y=max(retweet_count_normalized),
                    xref='x', yref='y',
                    text='Retweet Count Max:<br>'+ str(max(retweet_count_normalized)),
                    ax=-20, ay=-40)]
random_index = random.randrange(len(data))
favorite_annotations=[dict(x=data.created_at[random_index],
						y=sum(favorite_count_normalized) / float(len(favorite_count_normalized)),
                      	xref='x', yref='y',
                      	text='Favorite Count Average:<br>'+str(sum(favorite_count_normalized) / float(len(favorite_count_normalized))),
                      	ax=20, ay=-40),
                 dict(x=data.created_at[np.argmax(favorite_count_normalized)],
                      y=max(favorite_count_normalized),
                      xref='x', yref='y',
                      text='Favorite Count Max:<br>'+str(max(favorite_count_normalized)),
                      ax=-20, ay=-40)]

# Drop down menu
updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'Retweet Count',
                 method = 'update',
                 args = [{'visible': [False, False, True, True]},
                 		{'title': 'Retweet Count',
                        'annotations': retweet_annotations}]),
            dict(label = 'Favorite Count',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': 'Favorite Count',
                          'annotations': favorite_annotations}]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True, True, True, True]},
                         {'title': 'Both',
                          'annotations': retweet_annotations+favorite_annotations}]),
            dict(label = 'Reset',
                 method = 'update',
                 args = [{'visible': [True, False, True, False]},
                         {'title': 'Both reset',
                          'annotations': []}])
        ]),
    )
])


# Layout
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
        title = "Count",
    ),
    updatemenus = updatemenus
)


fig = dict(data=fig_data, layout=layout)
py.offline.plot(fig, filename = 'responds_count_line_graph.html')