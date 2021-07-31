#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FUNCTION: Script to run sentiment analysis on text. This script also handles 
          text that contains emojis converting the emojis first to text 
          descriptions using emot and then running sentiment analysis using 
          those descriptions embedded back in the text at the right spot. 

LAST UPDATED: 07/31/2021

OWNER: David J. Cox, PhD, MSB, BCBA-D
'''

# Packages and modules
import pandas as pd
import nltk
nltk.download('vader_lexicon') # Check to make sure it's up-to-date
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import emot as e

pd.set_option("display.max_columns", None)

#%% Read in the data
raw_data = pd.read_csv('/Users/davidjcox/Dropbox (Personal)/Projects/Manuscripts In Progress/Empirical/Endicott Data/Comparing Twitter Sentiment Between ABA Practitioners & Med Practitioners/aba_twitter_scrape.csv')
data = raw_data.copy()
data.head()

#%% Get sentiment for all tweets without handling emojis
sid = SentimentIntensityAnalyzer() # specify model for asneitment analysis

neg = []
neu = []
pos = []
compound = []

for i in range(len(data)):
    text = str(data['content'][i]) # Isolate tweet for analysis
    text_s = sid.polarity_scores(text) # Get the sentiment scores

    # Append sentiment to lists for later adding to df
    neg.append(text_s.get('neg'))
    neu.append(text_s.get('neu'))
    pos.append(text_s.get('pos'))
    compound.append(text_s.get('compound'))

# Add sentiment to df
data['neg'] = neg
data['neu'] = neu
data['pos'] = pos
data['compound'] = compound

#%% Get sentiment for all tweets including emojis
neg = []
neu = []
pos = []
compound = []

for i in range(len(data)):
    text = str(data['content'][i]) # Isolate tweet for analysis

    # Get emoji information
    emoji_info = e.emoji(text)
    emoji_info = pd.DataFrame(emoji_info)
    if len(emoji_info)==0:
        # Get the sentiment scores
        text_s = sid.polarity_scores(text)
    
        # Append sentiment to lists for later adding to df
        neg.append(text_s.get('neg'))
        neu.append(text_s.get('neu'))
        pos.append(text_s.get('pos'))
        compound.append(text_s.get('compound'))
    else:
        add_str = str(' ')
        for j in range(len(emoji_info)):
            add_str = add_str + emoji_info['mean'][j] + ' '
        first_emoji = emoji_info['location'][0][0]
        text = text[:first_emoji] + add_str + text[first_emoji:]

        # Get the sentiment scores
        text_s = sid.polarity_scores(text)
    
        # Append sentiment to lists for later adding to df
        neg.append(text_s.get('neg'))
        neu.append(text_s.get('neu'))
        pos.append(text_s.get('pos'))
        compound.append(text_s.get('compound'))

    # Give update
    if (i+1)%100==0:
        print(f'{i+1} tweets complete')

# Add sentiment to df
data['neg_e'] = neg
data['neu_e'] = neu
data['pos_e'] = pos
data['compound_e'] = compound

#%% Save it
data.to_csv('/Users/davidjcox/Dropbox (Personal)/Projects/Manuscripts In Progress/Empirical/Endicott Data/Comparing Twitter Sentiment Between ABA Practitioners & Med Practitioners/aba_twitter_scrape_sentiment.csv')