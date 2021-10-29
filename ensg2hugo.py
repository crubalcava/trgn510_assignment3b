#!/usr/bin/python3

##Build a Dictionary using smaller file expres.anal.csv
import sys 
import re
import csv
import pandas as pd

ens2gene={}
with open ("expres.anal.csv", 'r') as file:
    for line in file:
        matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";',line)
        if matches:
            ens2gene[matches[0][0]]=matches[0][1] 
            
with open('expres.anal.csv','r') as csvin, open('expres.anal.txt', 'w') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')
    for row in csvin:
        tsvout.writerow(row)
        #print(row) # undo note to see dictionary
##Using dictionary to convert ENSEMID to HUGOId
import pandas as pd
list=[]
with open("expres.anal.csv",'r') as csv_file: 
    csv_reader=csv.reader(csv_file, delimiter=',')
    reader = csv.DictReader(csv_file)
    header = reader.fieldnames
    for row in csv_reader:
        ENSID=row[1].split('.')[0]
        row[1]=ENSID
        if row[1] in ens2gene:
            row[1]=ens2gene[row[1]]
            list.append(row)
            print(row)
df = pd.DataFrame(list,columns=fieldnames)
df.to_csv('ens2hugo.csv',index=False)
df
##Convert gtf file to csv script above to work for "Homo_sapiens.GRCh37.75.gtf"
#see README.md for git repository
