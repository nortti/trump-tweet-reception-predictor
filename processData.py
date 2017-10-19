import pandas as pd


data = pd.read_json('json_data/realDonaldTrump.json')
print(list(data))
# print(data.head())
# data.sort_values(['retweet_count', 'favorite_count'], ascending = [0, 0], inplace = True)
# print(data.head())