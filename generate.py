#!/usr/bin/env python
import os
import sys
import plotly

import twitter_client
import respond_count_line_graph
import respond_count_bubble_graph
import word_count

if len(sys.argv) is 1:
    sys.exit('Provide a twitter screen name')

screen_name = sys.argv[1]

twitter_data = twitter_client.get_tweets_json(screen_name)

plotly.tools.set_credentials_file(username='tringuyenminh23',
                                  api_key='Ujw0Z0wUWFUDAXiKEsZO')

out_dir = 'out/' + screen_name + '/'
os.makedirs(out_dir, exist_ok=True)

respond_count_line_graph.generate(twitter_data, out_dir)
respond_count_bubble_graph.generate(twitter_data, out_dir)
word_count.generate(twitter_data, out_dir)
