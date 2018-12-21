#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:35:30 2018

@author: Nagendra
"""

wordlist = ["Nagendra", "is", "pursuing", "DataScience", "from","Acadgild"]

def wordlength(wordlist):
 return list(map(lambda x: len(x), wordlist))

print ("word lengths in array => " + str(wordlength(wordlist)))

