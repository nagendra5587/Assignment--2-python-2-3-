#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:27:28 2018

@author: Nagendra
"""

def myfilter(anyfunc, sequence):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in sequence:
  if anyfunc(item):
   result.append(item)
# return funal output
 return result
