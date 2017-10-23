import pandas as pd
import numpy as np


data = pd.read_json('json_data/HillaryClinton.json')
# print(list(data))
print(data.iloc[1]['user']['name'])
# ['followers_count']
# print(data.favorite_count[1])
# print(data.iloc[1]['favorite_count'])


# Normalize favorite_count and retweet_count with number of follower
# favorite_count_normalized = []
# retweet_count_normalized = []
# for i in range(len(data)):
# 	follower_count = data.iloc[i]['user']['followers_count']
# 	favorite_count_normalized.append(follower_count / data.iloc[i]['favorite_count'])
# 	retweet_count_normalized.append(follower_count / data.iloc[i]['retweet_count'])


# print(retweet_count_normalized[np.argmax(retweet_count_normalized)])
# print(max(retweet_count_normalized))

# print(list(data))
# print(data.head())
# print(data.head())
# data.sort_values(['retweet_count', 'favorite_count'], ascending = [0, 0], inplace = True)
# print(data.head())