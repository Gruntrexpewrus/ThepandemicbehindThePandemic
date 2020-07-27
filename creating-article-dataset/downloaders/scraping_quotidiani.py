# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:51:33 2020

@author: Nino
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import time
import re
website_url = "https://quotidiani.net/giornali_"

regions = ['abruzzo', 'basilicata', 'calabria', 'campania' ,'emilia_romagna', 'friuli' , 
          'lazio', 'liguria' , 'lombardia', 'marche', 'molise', 'piemonte' , 'puglia', 
          'toscana' ,  'trentino', 'sicilia', 'sardegna' , 'umbria',
          'valle_d_aosta', 'veneto']
for i in regions :
    url = website_url + i + '.htm'
    try:
       page = urlopen(url)
    except:
       print("Error opening the URL",i)

    soup = BeautifulSoup(page, 'html.parser')
    content = soup.find('div', {"class": "fluid quotidiani"})
    a_tags = content.find_all('a')

    links = list()
    for url in a_tags :
        links.append(url['href'])
    #print(links)
    
    with open('quotidiani' + i + '.txt', 'w') as file:
        for ele in links :
            file.write('%s\n' % ele)
        

