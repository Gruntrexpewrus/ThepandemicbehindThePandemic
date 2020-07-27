#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:19:15 2020

@author: marco
"""
import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

class FanpageParser:

    # DO NOT TOUCH THIS
    def __init__(self, target_domain, dataset_path, decode_format = 'UTF-8'):
        self.target_domain = target_domain
        self.http = urllib3.PoolManager()
        self.decode_format = decode_format
        self.default_header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
           'Connection': 'keep-alive'}
     
        dataset = pd.read_csv(dataset_path, sep = ';', index_col = [0])
        self.dataset = dataset[dataset['website-domain'] == target_domain]
             

    # DO NOT TOUCH THIS
    def get_updated_dataset(self):
        
        num_of_articles = len(self.dataset)
        
        for index, count in zip(self.dataset.index, range(num_of_articles)):
            
            print("[Progress at %.4f %%]" % float(count/num_of_articles*100))

            try:
                url = self.dataset['url'][index]
                
                print("\tGetting page from ", url[:50], '...')
                response = self.http.request('GET', url, headers=self.default_header)
                page_content = response.data.decode(self.decode_format)
                
                print("\tParsing page content...")
                updated_article_content = self._extract_article_body(page_content)
                
                print("\tOverwriting dataset...")
                self.dataset['content'][index] = updated_article_content
                print("\tDone")
                print("------------------------------------------------------------------")
                    
                time.sleep(random.randint(9, 11))
            except Exception as e:
                print('\n\n', e, '\n Error at URL: ', url, '\n\n')
                print("------------------------------------------------------------------")
                time.sleep(60)

        return self.dataset
    
    def write_dataset_to_file(self, save_path):
        cols = self.dataset.columns
        self.dataset.to_csv(save_path + self.target_domain + '_updated_content.csv', 
                   sep=';',
                   na_rep='NULL',
                   columns=cols,
                   escapechar="")

    def _extract_article_body(self, page_content):
        
        soup = BeautifulSoup(page_content, 'html.parser')
        '''
        ######################################################################
        ################# WRITE FROM HERE ####################################
        ######################################################################
        '''
        
        
        
        updated_content = ''
        
        body = soup.find("div", {'class':'articleContent'})
        article_paragraphs = body.findAll('p')
        
        for paragraph in article_paragraphs:
            updated_content = updated_content + paragraph.getText() + ' '
        
        #print(updated_content)
            
            
            
        '''
        ######################################################################
        ################# TO HERE ####################################
        ######################################################################
        '''
        #print(updated_content)
        return updated_content

    