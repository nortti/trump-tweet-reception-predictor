## Word Analysis

Data from Twitter API is pre-processed: Tweets are transfered to list of words, letters are converted to lower caps, stop-words are removed and then words are stemmed.

### Word Count

The simpliest analysis is to found which words the tweeter prefers and we plot the most frequently used words in a bar chart; **Word Count**. In case of Donald J. Trump (*realDonaldTrump*) these words are pretty much the same that he has been using during his presidency campaign: great, america, make, fake, news, etc.

### Accumulative Response Count

 For the second text analysis we computed the total retweets and likes for words summing every retweet and like for every tweet where the word appear. In the bubble plot x-axis represent number of total retweets and y-axis represent total number of favorites while the size of the bubble correspond to the Word Count. The plot for *realDonaldTrump* show quite linear correlation between favorites (likes) and retweets. There are two bubbles that have less likes respect to retweets than the linearity suggests: these are **hillari** and **clinton**.

### Average Count

Since some words appear often the Accumulative Response Count don't give good view of the impact of seldom used words, so we divided it by the Word Count and got the Average Count. While the Accumulative Response Count give showed the effect of repeating a word the Average Count shows the average effect of single word. Axes and bubble size are same as in Accumulative Response Count. There are two bubbles that dominate Average Count for *realDonaldTrump* these are tags fraudnewscnn and fnn, that he used to send a video of himself wrestling a man with a cnn logo as ahead. So the response don't only depend on the words but also other content of the tweet.