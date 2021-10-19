#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:33:10 2021

@author: jacobsosine
"""

import numpy as np 
import pandas as pd 
import json 
import string
import re
raw = pd.read_csv('../data/01_raw/aba_twitter_scrape.csv') 
df = raw.copy()

# df[:100].to_csv('../data/01_raw/aba_twitter_scrape_100_rows.csv')

# df = pd.read_csv('../data/01_raw/aba_twitter_scrape_100_rows.csv') 





# get the user column
user = pd.DataFrame()
user['users'] = df[['user', 'id']]


# from the description - Lower case the description 

def get_value(value):
    finding = value.find('descriptionUrls')
    value = value[:finding]
    
    return value

def get_bcba(value):
    value = str.lower(value)
    if ('bcba' in value): #or ('behavioral' in value) or ('bcaba' in value):
        print('bcba_found')
        return 'behavior analyst'
        
    else:
        print('bcba_not_found')
        return 'not behavior analyst'
    
    
def remove_punctuation_with_period(text):
  punct = set(string.punctuation)
  text = text.lower()
  text = "".join([c for c in text if c not in punct])
  text = re.sub(r"""[()\’°"#/@;¢€:£<“>{}«®`©”+=~‘|.!?,]""", "", text)         id  780371
  text = re.sub(r'/[^a-zA-Z]',"",text)
  text = " ".join(text.split())
  return text


user['bcba_or_no_bcba'] = user['users'].apply(lambda x: get_bcba(str(x)))
user['only_descrip'] = user['users'].apply(lambda x: get_value(str(x)))
user['only_descrip'] = user['only_descrip'].apply(lambda x: remove_punctuation_with_period(x))
user['only_descrip'] = user['only_descrip'].str.lower()
user['only_descrip'] = user['only_descrip'].str.split()


list_of_vals = user['only_descrip'].tolist()

dict_ = {}
for i in list_of_vals:
    for j in i:
        if j not in dict_:
            dict_[j] = 1
        else:
            dict_[j] += 1
    
dict_df = pd.DataFrame.from_dict(dict_,orient='index').reset_index(drop=False)    
dict_df = dict_df.sort_values(by=0,ascending=False)
# user['only_descrip'] = user['only_descrip'].apply(lambda x: remove_punctuation_with_period(x))
#%%
top_500 = dict_df[:500]

def barplot(data,figsize,xlabel,title,ylabel,fpath):
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import seaborn as sns

    fig, ax = plt.subplots(figsize=figsize)
    ax = sns.barplot(x=0, y='index', data=data,color='black')
    
    plt.xlabel(xlabel,fontsize=32,labelpad=(16))
    plt.yticks(fontsize=24)
    plt.xticks(fontsize=24,rotation=0)
    plt.ylabel(ylabel,fontsize=50,labelpad=(16))

    plt.title(title,fontsize=48,pad=60)
    right_side=ax.spines['right']
    right_side.set_visible(False)
    top = ax.spines['top']
    top.set_visible(False)
    plt.tight_layout()
    plt.savefig(fpath)
    plt.show()




barplot(data=top_500,figsize=(200,100),xlabel='Word Count',title="",ylabel='Bigrams',fpath='../figures/word_count.png')




# loop through the description and look for bcba 
# create a colum called "bcba_notbcba"
# add a label of bcba



# print(df['user'][])