#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
from bs4 import BeautifulSoup
import os, time, datetime
from matplotlib import pyplot as plt
from urllib.parse import urlparse
import glob


def extract_date(raw_string):
    raw_string = str(raw_string)
    months = {'Gennaio':'01', 'Febbraio':'02', 'Marzo':'03', 'Aprile':'04', 'Maggio':'05'}

    date_tokens = raw_string.strip().split(' ')
    
    
    day = date_tokens[0]
    month = months[date_tokens[1]]
    year = date_tokens[2]
    
    form_date = str(year +'-'+ month + '-' + day)
        #print(form_date)
    
    return form_date

######################## MAIN STARTS HERE ######################################################
    

cols = ['title', 'content', 'date', 'author', 'tags', 'url', 'website-domain', 'region']

articles_df = pd.DataFrame(data = None, columns = cols)

html_paths = glob.glob("/home/marco/workspace/git/StatLearnTeam/web_pages_index/new_pages/ilfriuli*.html")
for path in html_paths: # From last page to most recent
    
    webpage_path = path
    
    html_content = open(webpage_path)
    soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8') # Open file as a webpage
    
    ################# SINGLE PAGE MINING STARTS HERE #############################
    
    article_section = soup.findAll('article', {'class':'media'})
    
    for article in article_section:
        try:
            title = article.find('h3', {'class':'media__title'}).getText()
            content =  ''#  
            date = ''
            
            author = 'Il Friuli'
            
            url = 'https://www.ilfriuli.it' + article.find('a')['href']
            
            website = 'www.ilfriuli.it'
            
            tags = []
   
            regions = ['Friuli']
            
            article_entry = pd.DataFrame(data = [[title, content, date, author, tags, url, website, regions]], columns = cols)
            articles_df = articles_df.append(article_entry, ignore_index = True)

        except Exception as e:
            print(e) # Not all html element retrieved are actually article so exceptions could be thrown.
            #print(e)
            #print("=" * 10)
            #print("\nNOT AN ARTICLE!\n")
            #print(article)
            #print("\n" * 3)


# Saving dataframe to file
articles_df.drop_duplicates(subset=["content"])


articles_df.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/ilfriuli.csv', 
                   sep=';',
                   na_rep='NULL',
                   columns=cols,
                   escapechar="")
