#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FUNCTION: At the top, include a short description of the function of the script.
		  That is, in one sentence answer the question, 'What does this script do?'.
		  Also provide quick note on any bugs or issues as well as last time that tests were conducted.

TESTING:
    Number conducted = 0
    Number passed = 0
    Pass percentageon last 10 = 0

LAST UPDATED: DD/MM/YYYY

OWNER: Your Name
'''

# In case it needs to be installed
!pip install git+https://github.com/JustAnotherArchivist/snscrape.git

import snscrape.modules.twitter as sntwitter
import pandas

# Personal preference
pd.set_option('display.max_columns', None)


#%% Scrape Twitter for #behaviortwitter
!snscrape --jsonl --progress --max-results 100000 --since 2018-01-01 twitter-search "#behaviortwitter until:2021-07-25" > text-query-tweets.json

# Read in the jscon file
bx_tweets = pd.read_json('text-query-tweets.json', lines=True)

# Creating a dataframe from the tweets list above 
bx_tweets = pd.DataFrame(bx_tweets)

# Add col for hashtag focus
bx_tweets['focus'] = 'behaviortwitter'

#%% Scrape Twitter for #ABATherapy
!snscrape --jsonl --progress --max-results 100000 --since 2018-01-01 twitter-search "#ABATherapy until:2021-07-25" > text-query-tweets.json

# Read in the jscon file
abtx_tweets = pd.read_json('text-query-tweets.json', lines=True)

# Creating a dataframe from the tweets list above 
abtx_tweets = pd.DataFrame(abtx_tweets)

# Add col for hashtag focus
abtx_tweets['focus'] = 'abatherapy'

#%% #ABA
!snscrape --jsonl --progress --max-results 100000 --since 2018-01-01 twitter-search "#ABA until:2021-07-25" > text-query-tweets.json

# Read in the jscon file
aba_tweets = pd.read_json('text-query-tweets.json', lines=True)

# Creating a dataframe from the tweets list above 
aba_tweets = pd.DataFrame(aba_tweets)

# Add col for hashtag focus
aba_tweets['focus'] = 'aba'

#%% #appliedbehavioranalysis
!snscrape --jsonl --progress --max-results 100000 --since 2018-01-01 twitter-search "#appliedbehavioranalysis until:2021-07-25" > text-query-tweets.json

# Read in the jscon file
appliedbehavioranalysis_tweets = pd.read_json('text-query-tweets.json', lines=True)

# Creating a dataframe from the tweets list above 
appliedbehavioranalysis_tweets = pd.DataFrame(appliedbehavioranalysis_tweets)

# Add col for hashtag focus
appliedbehavioranalysis_tweets['focus'] = 'appliedbehavioranalysis'

#%% Scrape Twitter for #medtwitter
!snscrape --jsonl --progress --max-results 10000000 --since 2018-01-01 twitter-search "#medtwitter until:2021-07-25" > text-query-tweets.json

# Read in the jscon file
med_tweets = pd.read_json('text-query-tweets.json', lines=True)

# Creating a dataframe from the tweets list above
med_tweets = pd.DataFrame(med_tweets)

# Add col for hashtag focus
med_tweets['focus'] = 'medtwitter'

#%% Concatenate all the dfs to each other
print("Expected length: ", len(bx_tweets) + len(abtx_tweets) + len(aba_tweets) + len(appliedbehavioranalysis_tweets) + len(med_tweets))
all_tweets = bx_tweets.append(abtx_tweets)
all_tweets = all_tweets.append(aba_tweets)
all_tweets = all_tweets.append(appliedbehavioranalysis_tweets)
all_tweets = all_tweets.append(med_tweets)
print("Observed length: ", len(all_tweets))

#%% Save it
all_tweets.to_csv('aba_twitter_scrape.csv')