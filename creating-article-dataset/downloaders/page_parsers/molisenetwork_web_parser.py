#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:30:31 2020

@author: marco
"""


import pandas as pd
from bs4 import BeautifulSoup
import os, time, datetime
from matplotlib import pyplot as plt
from urllib.parse import urlparse
import glob


def extract_date(raw_string):
    raw_string = str(raw_string)
    months = {'Gennaio':'01', 'Febbraio':'02', 'Marzo':'03', 'Aprile':'04', 'Maggio':'05'}

    date_tokens = raw_string.split(' ')
    
    day = date_tokens[0]
    month = months[date_tokens[1]]
    year = date_tokens[2]
    
    form_date = str(year +'-'+ month + '-' + day)
        #print(form_date)
    
    return form_date

######################## MAIN STARTS HERE ######################################################
    

cols = ['title', 'content', 'date', 'author', 'tags', 'url', 'website-domain', 'region']

articles_df = pd.DataFrame(data = None, columns = cols)

html_paths = glob.glob("/home/marco/workspace/git/StatLearnTeam/old/web_pages_index/new_pages/molise*.html")
for path in html_paths: # From last page to most recent
    
    webpage_path = path
    
    html_content = open(webpage_path)
    soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8') # Open file as a webpage
    
    ################# SINGLE PAGE MINING STARTS HERE #############################
    
    article_section = soup.findAll('article', attrs={"class":"blog-post-item"})
    
    for article in article_section:
        try:
            title = article.find('h2', {'class':'post-title'}).getText()
            content =  ''#
            
            date =  article.find('time', {'class':'postmeta-date'})['datetime']
            
            author = 'Molise Network'
            
            url = article.find('h2', {'class':'post-title'}).find('a')['href']
            website = 'www.molisenetwork.net'
            
            # Not all articles have tags, but should not be a problem getting the other info (always useful)
            # That's why there is a nested try except.
            tags = []
            
            
            regions = ['Molise']
            
            article_entry = pd.DataFrame(data = [[title, content, date, author, tags, url, website, regions]], columns = cols)
            articles_df = articles_df.append(article_entry, ignore_index = True)

        except Exception as e:
            pass # Not all html element retrieved are actually article so exceptions could be thrown.
            #print(e)
            #print("=" * 10)
            #print("\nNOT AN ARTICLE!\n")
            #print(article)
            #print("\n" * 3)


# Saving dataframe to file
#articles_df.drop_duplicates(subset=["content"])
'''
articles_df.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/molisenetwork.csv', 
                   sep=';',
                   na_rep='NULL',
                   columns=cols,
                   escapechar="")

'''
'''
## SIMPLE CONTENT FILTER - WILL LOOK FOR COVID RELATED KEYWORDSs       
        
contains_virus_count = {}

for i in range(0, len(articles_df)):
    row = articles_df.values[i]
    
    title = row[0]
    content = row[1]
    date = row[2]
    author = row[3]
    tags = row[4]
    
    aggregate_fields = [title, content]
    aggregate_fields.extend(tags)
    
    if date not in contains_virus_count.keys():
        contains_virus_count[date] = 0

    keywords = ['coronavirus', 'covid', 'covid-19']            
    has_keyword = False # Until proven true
    
    for field in aggregate_fields:
        
        if any(k in str.lower(field) for k in keywords):
            has_keyword = True
            
    if has_keyword:
        contains_virus_count[date] = contains_virus_count[date] + 1  # 1 More article contains coronavirus related keywords
        
        
        
'''