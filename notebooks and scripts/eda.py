#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FUNCTION: Basic EDA and visualizations of data

LAST UPDATED: 07/31/2021

OWNER: david J. Cox, PhD, MSB, BCBA-D
'''

# Packages and modules
import os
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

!pip install sweetviz # In case the individual does not have it installed
import sweetviz as sv

pd.set_option("display.max_columns", None)

#% Read in the data
raw_data = pd.read_csv('/Users/davidjcox/Dropbox (Personal)/Projects/Manuscripts In Progress/Empirical/Endicott Data/twitter-aba-sentiment/data/03_primary/aba_twitter_scrape_sentiment.csv').drop(['Unnamed: 0', 'Unnamed: 0.1'], axis=1)
data = raw_data.copy()
data.head()

#%% get current datatype of cols
for i in list(data):
    print(data[i].dtype, i)

#%% Convert string cols to appropriate datatype
str_cols = ['_type', 'url', 'content', 'renderedContent',  'user', 'lang',
            'source', 'sourceUrl', 'sourceLabel', 'outlinks', 'tcooutlinks',
            'media', 'quotedTweet', 'inReplyToTweetId', 'inReplyToUser',
            'mentionedUsers', 'coordinates', 'place', 'hashtags', 'cashtags',
            'focus']

for i in str_cols:
    data[i] = data[i].astype(str)

#%% Convert datetime cols to appropriate datatype
date_vals = []

for i in range(len(data)):
    val = data['date'][i]
    try:
        new_val = str(val)
        new_val = pd.to_datetime(new_val)
        date_vals.append(new_val)
    except:
        print("Need to fix: ", val)
        new_val = input()
        date_vals.append(new_val)

data['date'] = date_vals

#%% Convert float cols to appropriate datatype
float_cols = ['id', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount',
              'conversationId', 'retweetedTweet', 'neg', 'neu', 'pos',
              'compound', 'neg_e', 'neu_e', 'pos_e', 'compound_e']

for i in float_cols:
    data[i] = data[i].astype(float)

#%% Quick EDA html output using sweetviz
first_report = sv.analyze(data)

#display the report
first_report.show_html('Advertising.html')

#%% 