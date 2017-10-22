#!/usr/bin/env python
import pandas as pd
import json
import string
import plotly as py
import plotly.graph_objs as go
from nltk.stem.porter import *
from collections import Counter
import operator

# from apyori import apriori

# Parameters
num_top_words = 25
json_file = "json_data/realDonaldTrump.json"
#json_file = "json_data/BarackObama.json"
#json_file = "json_data/HillaryClinton.json"
stopWord_file = "stop-word-list.csv"

# Data IN
df = pd.read_json(json_file)[['text', 'retweet_count', 'favorite_count']]

# Stopwords
with open(stopWord_file) as f:
    stopwords = set(f.read().split(", "))

more_stopwords = {'amp','httpstco1rzmeenqib', 'httpstcowyunhjjujg','httpstcov3aoj9ruh4','httpstco9pfqnrsh1z','httpstcohfujerzbod',
				'httpstcobh7srnegz1','httpstcoohshqsfrfl','httpstcolz2dhrxzo4','httpstcowpk7qwpk8z','httpstcoosxa3bamh',
				'httpstcory9mggjrxm','httpstcoe0bup1k83z','httpstco4jfhyydeho','httpstcojjora0kfyr','httpstcoik3yqjhzsa',
				'httpstcohhge51dtsn','httpstcowazigoqqmq','httpstco9qg8sjf4t8'}
stopwords = stopwords.union(more_stopwords)

df['text'] = df['text'].apply(lambda row: ''.join(l for l in row.lower() if l not in string.punctuation))
df['text'] = df['text'].apply(lambda row: ' '.join([word for word in row.split() if word not in stopwords]))
ps = PorterStemmer()
df['text'] = df['text'].apply(lambda row: ' '.join([ps.stem(word) for word in row.split()]))

# Wordcount

wordfreq = []
words = Counter();

# Simple word count
	
for row in df['text']:
	wordlist = row.split()
	words.update(word for word in wordlist)

topW = words.most_common(num_top_words)

trace1 = go.Bar(
            x=[val[0] for val in topW],
            y=[val[1] for val in topW],
    )
data1 = go.Data([trace1])

layout1 = go.Layout(
    title= "Donald Trump's most recent tweets: Word Count",
	font=dict(size=18),
    xaxis= dict(
        title= 'The Most Used Words',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Word Count',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)

fig = go.Figure(data=data1, layout=layout1)
py.offline.plot(fig, filename = 'Top_words.html')

#barplot = [go.Bar(
#            x=[val[0] for val in topW],
#            y=[val[1] for val in topW],
#    )]
#py.offline.plot(barplot, filename='Top_words.html')

# word_count times retweet_count / favorite_count

retweets = {}
likes = {}
combi = {}

for i in range(0, len(df['text'])):
	wordlist = df['text'][i].split()
#	print(wordlist)
	for w in wordlist:
#		print(wordlist.count(w))
#		print(type(retweets.keys()))
		if not w in retweets:
			retweets[w] = df['retweet_count'][i]
			likes[w]=df['favorite_count'][i]
			combi[w]=(df['retweet_count'][i],df['favorite_count'][i])
		else:
			retweets[w] = retweets[w] + df['retweet_count'][i]
			likes[w] = likes[w] + df['favorite_count'][i]
			combi[w] = (retweets[w] + df['retweet_count'][i], likes[w] + df['favorite_count'][i])
		wordfreq.append(wordlist.count(w))

# arrenge words by retweets / likes for every tweet the word appear
ret_sort = sorted(retweets.items(), key=operator.itemgetter(1), reverse=True)
topW_re = ret_sort[:num_top_words]
lik_sort = sorted(likes.items(), key=operator.itemgetter(1), reverse=True)
topW_li = lik_sort[:num_top_words]

# Retweets

trace2 = go.Bar(
            x=[val[0] for val in topW_re],
            y=[val[1] for val in topW_re]
    )
data2 = go.Data([trace2])

layout2 = go.Layout(
    title= "Donald Trump's most recent tweets: Most Retweeted Words",
	font=dict(size=18),
    xaxis= dict(
        title= 'The Most Retweeted Words',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Retweets from every tweet',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)

fig2 = go.Figure(data=data2, layout=layout2)
py.offline.plot(fig2, filename = 'most_retweeted_words.html')

# Likes

trace3 = go.Bar(
            x=[val[0] for val in topW_li],
            y=[val[1] for val in topW_li]
    )

data3 = go.Data([trace3])

layout3 = go.Layout(
    title= "Donald Trump's most recent tweets: Most Liked Words",
	font=dict(size=18),
    xaxis= dict(
        title= 'The Most Liked Words',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Likes form every tweet',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)

# Average retweets / likes for words

fig3 = go.Figure(data=data3, layout=layout3)
py.offline.plot(fig3, filename = 'most_liked_words.html')

# Retweets

retro = {}
for i in range(0, len(ret_sort)):
	retro[ret_sort[i][0]] = (float(ret_sort[i][1])/words.get(ret_sort[i][0]))
retro_sort = sorted(retro.items(), key=operator.itemgetter(1), reverse=True)

trace4 = go.Bar(
            x=[val[0] for val in retro_sort[:25]],
            y=[val[1] for val in retro_sort[:25]]
    )
data4 = go.Data([trace4])

layout4 = go.Layout(
    title= "Donald Trump's most recent tweets: Top Average Retweeted Words",
	font=dict(size=18),
    xaxis= dict(
        title= 'The Top Retweeted Words',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Retweets per Word Count',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)

fig4 = go.Figure(data=data4, layout=layout4)
py.offline.plot(fig4, filename = 'Top_retweeted_words.html')

# Likes

litro = {}
for i in range(0, len(lik_sort)):
	litro[lik_sort[i][0]] = (float(lik_sort[i][1])/words.get(lik_sort[i][0]))
litro_sort = sorted(litro.items(), key=operator.itemgetter(1), reverse=True)

trace5 = go.Bar(
            x=[val[0] for val in litro_sort[:25]],
            y=[val[1] for val in litro_sort[:25]]
    )

data5 = go.Data([trace5])

layout5 = go.Layout(
    title= "Donald Trump's most recent tweets: Top Average Liked Words",
	font=dict(size=18),
    xaxis= dict(
        title= 'The Top Liked Words',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),
    yaxis=dict(
        title= 'Likes per Word Count',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)

fig5 = go.Figure(data=data5, layout=layout5)
py.offline.plot(fig5, filename = 'Top_liked_words.html')

# Overall plots

# Calculate accumulate respond 
accumulate_responds = []
for w in combi.keys():
    accumulate_responds.append(words[w])

# Normalize accumulate_responds to use as size of bubble
accumulate_responds_normalized = [float(i)/max(accumulate_responds) for i in accumulate_responds]    
sizeref = 2*max(accumulate_responds_normalized)/(80**2)

# cumulative likes / retweets for words

fig_data1 = []
trace_f1= go.Scatter(
	x = [combi[key][0] for key in combi.keys()],
	y = [combi[key][1] for key in combi.keys()],
#    x=combi[combi.keys()][0],
#    y=combi[kombi.keys()][1],
    mode= 'markers',
    marker= dict(
        symbol = 'circle',
        sizemode = 'area',
        sizeref = sizeref,
        size = accumulate_responds_normalized,
        line= dict(width=1),
        color= 'rgb(93, 164, 214)',
        opacity= 0.8),
	textfont = dict(
		size = 20),
    text= [key+': '+str(words[key]) for key in combi.keys()])
fig_data1.append(trace_f1);

layout_f1= go.Layout(
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
fig_f1 = go.Figure(data = fig_data1, layout=layout_f1)
py.offline.plot(fig_f1, filename = 'overall_word.html')

# Average likes / retweets for word 

fig_data2 = []
trace_f2= go.Scatter(
	x = [float(combi[key][0])/words.get(key) for key in combi.keys()],
	y = [float(combi[key][1])/words.get(key) for key in combi.keys()],
#    x=combi[combi.keys()][0],
#    y=combi[kombi.keys()][1],
    mode= 'markers',
    marker= dict(
        symbol = 'circle',
        sizemode = 'area',
        sizeref = sizeref,
        size = accumulate_responds_normalized,
        line= dict(width=1),
        color= 'rgb(93, 164, 214)',
        opacity= 0.8),
	textfont = dict(
		size = 20),
    text= [key+': '+str(words[key]) for key in combi.keys()])
fig_data2.append(trace_f2);

layout_f2= go.Layout(
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
fig_f2 = go.Figure(data = fig_data2, layout=layout_f2)
py.offline.plot(fig_f2, filename = 'overall_ave_word.html')

# Apriori

#print('Apriori')
#transactions = []
#for i in range(0, len(df['text'])):
#	wordlist = df['text'][i].split()
#	print(wordlist)
#	transactions.append(wordlist)

# print(transactions)


#results = list(apriori(transactions, min_support = 0.03, min_confidence = 0.03))
#print(results)

#transactions = [
#    ['beer', 'nuts'],
#    ['beer', 'cheese'],
#]
#results = list(apriori(transactions))
