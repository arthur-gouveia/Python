# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:47:43 2016

@author: arthu
"""

data_base = [["f1", 2000, .24], ["f2", 150000, .32], ["f3", 345000, .32]]
invoice = input("Enter invoice: ")

found = False

for data in data_base:
    if invoice == data[0]:
        found = True
        break

result = "Invoice is valid" if found \
    else "Invoice does not exist, enter a valid document: "

print(result)
