#!/usr/bin/python3

import sys
import re
import csv

ens2gene= {}

with open ("mini.gtf", 'r') as file: #use mini.gtf for testing first
    for line in file:
        matches=re.findall('.*gene_id "(.*?)".*gene_name "(.*?)";', line)
        if matches:
            ens2gene[matches[0][0]]=matches[0][1]
            print (ens2gene[matches[0][0]])
