#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


''' ---- GENERAL INFO ---- '''
This parser will automatically overwrite the content of an article
in a portion of the dataset that is loaded from the filesystem and then stored in memory. 
IT WILL NOT OVERWRITE THE LOCAL intopic_it_articles.csv FILE.
Please do not overwrite your local copy of intopic_it_articles.csv.



''' ---- FOR YOU ---- '''
- Use this template to write a specific parser. 
- Copy everything that follows INCLUDING the imports.

- Write the logic in the _extract_article_body method, 
the specific section is highlighted.

- Change the name of the class from ParserTemplate to something else that
  tells us which news outlet it's specific for.




''' --- (IMPORTANT) ---'''

The method get_updated_dataset() will return only a portion of the dataset
which will contain only the info about one domain name. 


"""

import urllib3
from bs4 import BeautifulSoup
import pandas as pd
import random
import time

class ParserTemplate:
    LOW_LIMIT_TIMEOUT = 9
    HIGH_LIMIT_TIMEOUT = 11
    
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
                
                time.sleep(random.randint(self.LOW_LIMIT_TIMEOUT, self.HIGH_LIMIT_TIMEOUT))
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
        updated_content = ""
        '''
        ######################################################################
        ################# WRITE FROM HERE ####################################
        ######################################################################
        '''
        
        
        
        
        
        
        
        
        
            
            
            
        '''
        ######################################################################
        ################# TO HERE ############################################
        ######################################################################
        '''
        #print(updated_content)
        return updated_content
    