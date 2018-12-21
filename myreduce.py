#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 10:11:17 2018

@author: Nagendra
"""
def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)
  return result

def sum(x,y):
    return x+y

m= myreduce(sum,[1,2,3])
print(m)