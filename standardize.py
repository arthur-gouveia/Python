# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 08:16:18 2016

@author: arthu
"""
import random

def standardize(data,noise_level=0.05,center_value=0):
    
    minimum = center_value - noise_level
    maximum = center_value + noise_level
    
    max_data = max(data)
    min_data = min(data)
    
    for i in range(0,len(data)):
        data[i] = (data[i] - min_data) / (max_data - min_data) \
                  * (maximum - minimum) + minimum
    
    return data

data = [1, 2, 3, 4, 5]
noise = list(range(5))


for i in noise:
    noise[i] = random.random()



noise = standardize(noise, center_value=1)
print(data)

print([a*b for a,b in zip(data,noise)])