#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 19:33:10 2021

@author: jacobsosine
"""

import numpy as np 
import pandas as pd 
import json 

df = pd.read_csv('../data/01_raw/aba_twitter_scrape.csv') 

# df[:100].to_csv('../data/01_raw/aba_twitter_scrape_100_rows.csv')

# df = pd.read_csv('../data/01_raw/aba_twitter_scrape_100_rows.csv') 





# get the user column
user = pd.DataFrame()
user['users'] = df['user']


# from the description - Lower case the description 



def get_bcba(value):
    value = str.lower(value)
    if ('bcba' in value): #or ('behavioral' in value) or ('bcaba' in value):
        print('bcba_found')
        return 'behavior analyst'
        
    else:
        print('bcba_not_found')
        return 'not behavior analyst'
    


user['bcba_or_no_bcba'] = user['users'].apply(lambda x: get_bcba(str(x)))



# loop through the description and look for bcba 
# create a colum called "bcba_notbcba"
# add a label of bcba



# print(df['user'][])