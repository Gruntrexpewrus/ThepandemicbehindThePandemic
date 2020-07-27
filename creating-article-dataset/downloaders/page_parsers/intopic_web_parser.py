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

def extract_date(filename, raw_string):
    raw_string = str(raw_string)
    months = {'Gennaio':'01', 'Febbraio':'02', 'Marzo':'03', 'Aprile':'04', 'Maggio':'05', 'Giugno':'05'}

    if "2020" in raw_string:
        creation_date = raw_string.split(' ')
        form_date = str(creation_date[3]) +'-'+ str(months[creation_date[2]]) + '-' + str(creation_date[1])
        #print(form_date)
    else:
        #print(raw_string)
        creation_date = time.ctime(os.path.getctime(filename))
        form_date = str(datetime.datetime.strptime(creation_date, "%a %b %d %H:%M:%S %Y"))
        form_date = form_date.split(' ')[0]
        #print(form_date)
    
    return form_date

######################## MAIN STARTS HERE ######################################################
    
html_root = "/home/marco/workspace/git/StatLearnTeam/web_pages_index/" # Where the html pages are

cols = ['title', 'content', 'date', 'author', 'tags', 'url', 'website-domain', 'region']

articles_df = pd.DataFrame(data = None, columns = cols)

quotidiani = pd.read_csv('/home/marco/workspace/git/StatLearnTeam/dataset/quotidiani.csv', sep = ',')


for i in (list(range(1, 3455))[::-1]): # From last page to most recent
    
    webpage_path = html_root + str(i) + ".html"
    html_content = open(webpage_path)
    soup = BeautifulSoup(html_content, 'html.parser') # Open file as a webpage
    
    ################# SINGLE PAGE MINING STARTS HERE #############################
    
    article_section = soup.findAll('div', attrs={"class":"bp-entry"})
    
    print('Page ', i, ' out of 3455')
    
    for article in article_section:
        try:
            title = article.find("h2").find("a").getText()
            content = article.find("div", attrs = {"class":"bp-details"}).getText()
            publication_info = article.find("span", attrs = {"class":"author vcard"}) # Date, author...
            
            date = extract_date(webpage_path, str(publication_info.getText()))
            
            author = publication_info.find("span", attrs={"class":"fn"}).getText()
            
            url = article.find("div", attrs = {"class":"bp-details"}).find("a")['href']
            website = urlparse(url).netloc
            
            # Not all articles have tags, but should not be a problem getting the other info (always useful)
            # That's why there is a nested try except.
            tags = list()
            try:
                tags_raw = article.find("div", {"class":"tagcloud"}).findAll("a",{'class':'tag-link-10'})
                tags.extend([tag.getText() for tag in tags_raw])
            except:
                pass # Not an article, OR the article does not have any tags
            
            
            regions = quotidiani['Region'][quotidiani.Domain == website].unique()
            
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
articles_df.drop_duplicates(subset=["content"])

articles_df.to_csv('/home/marco/workspace/git/StatLearnTeam/dataset/intopic_it_articles.csv', 
                   sep=';',
                   na_rep='NULL',
                   columns=cols,
                   escapechar="")


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