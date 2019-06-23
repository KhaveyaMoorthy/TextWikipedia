# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 19:51:04 2019

@author: Pujitha
"""

import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
def soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser")
    return soupdata
soup2 = soup("https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy")
#print(soup2)
for records2 in soup2.findAll("div",{"id" : "content"}):
    #print(records2)
    for records in records2.findAll("div",{"class" : "mw-parser-output"}):
        #print(records)
        for data in records.findAll('a'):
            print(data.text)
for i in soup2.findAll("p"):
    print(i.text)
    