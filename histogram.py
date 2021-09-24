#!/usr/bin/env python

import csv
import matplotlib as mpl
import matplotlib.pyplot as plt



column=[]
with open("covid_local_adult_detention_fac.csv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for idx, line in enumerate(tsv_file):
        if idx > 4:
            column.append(line[4])
            
fig, ax=plt.subplots(figsize=[100,45])
plt.style.use('seaborn-white')
ax.hist(column, bins=17)
plt.show()
# print (column)
plt.savefig('histo_plot.png') 
