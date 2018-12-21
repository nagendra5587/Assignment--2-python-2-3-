#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 08:19:28 2018

@author: Nagendra
"""
# Longest word
wordlist = ["Nagendra", "is", "pursuing", "DataScience", "from","Acadgild","ContagiousDisease"]

from functools import reduce
def maxword(wordlist):
    return reduce( (lambda x,y:y if len(y)> len(x) else x) ,wordlist)

print(maxword(wordlist))
