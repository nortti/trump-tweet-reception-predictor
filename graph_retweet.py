import plotly
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd

# Credential
plotly.tools.set_credentials_file(username='tringuyenminh23', api_key='Ujw0Z0wUWFUDAXiKEsZO')


# Process data
data = pd.read_json("json_data/realDonaldTrump.json")
data.sort_values('retweet_count', ascending = 0, inplace = True)

data_top10 = data.head(10)
data_low10 = data.tail(10)
frames = [data_top10, data_low10]
data_extracted = pd.concat(frames)

print(data_extracted)

# # trace0 = go.Scatter(
# #     x= ,
# #     y=[10, 11, 12, 13],
# #     text=['A<br>size: 40', 'B<br>size: 60', 'C<br>size: 80', 'D<br>size: 100'],
# #     mode='markers',
# #     marker=dict(
# #         color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
# #         size=[40, 60, 80, 100],
# #     )
# # )

# data = [trace0]
# py.iplot(data, filename='bubblechart-text')
