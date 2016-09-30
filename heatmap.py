# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import seaborn as sns
import pandas as pd
#sns.set()

df = pd.read_csv('teste.csv')
# Load the example flights dataset and conver to long-form
#flights_long = sns.load_dataset("flights")

#print(type(flights_long))

flights = df.pivot("mês", "ano", "valor")

d = {'Janeiro': 0,
     'Fevereiro': 1,
     'Março': 2,
     'Abril': 3,
     'Maio': 4,
     'Junho': 5,
     'Julho': 6,
     'Agosto': 7,
     'Setembro': 8,
     'Outubro': 9,
     'Novembro': 10,
     'Dezembro': 11}

index = sorted(df['mês'], key=lambda x: d[x])

# Draw a heatmap with the numeric values in each cell
sns.heatmap(flights.reindex(index), annot=True, fmt="d", linewidths=.5)
