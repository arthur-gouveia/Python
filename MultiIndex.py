# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

dic_teste = {'ID': ['AM1', 'AM2', 'AM3', 'AM4', 'AM1', 'AM2', 'AM3', 'AM4'],
             'ELEMENTO': ['Ca', 'Ca', 'Ca', 'Ca', 'Mg', 'Mg', 'Mg', 'Mg'],
             'CONC.': [10, 5, 10, 8, 3, 2, 1, 5]}

# using set just to remove duplicates
iterables = [set(dic_teste['ELEMENTO']), set(dic_teste['ID'])]
# creates the MultiIndex
index = pd.MultiIndex.from_product(iterables, names=['ELEMENTO', 'ID'])
# Since it's just one data column it is a Series. If there were 2+ it's a DF
s = pd.Series(dic_teste['CONC.'], index=index, name='CONC.')

print(s)
