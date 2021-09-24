# trgn_assignment3bssignment 3B
# extract_phonenum.py

### Usage
* python3 extract_phonenum.py
* mytextfile.txt #Use this file as a unit test.

### Description
* Extracts phone numbers from a text file, and prints formatted phone numbers.
* One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. 
* [+][country code] optional output if number is international. Create a script called extract_phonenum.py which extracts phone numbers from text file

### Known Issues
* This program will only work for phone numbers that are formatted as [+][country code] ([AreaCode]) [local phone number]. 
    * The local number needs to be formatted as such "'+'[any string of #, 0-9]'space'([any string of # > 2, 0-9 enclosed in parenthesis])'space'[any string of # > 3, 0-9]'-'[any string of # > 3, 0-9]". For example +1 (818) 818-8188 or (818) 818-8188 will also work.

# ens2hugo.py
### Usage
* python3 ens2hugo.py [-f][0-9] [file]
* Options
    * -f An optional flag where -f is followed by a number 0-9, such as ensg2hugo.py -f2 expression_analysis.tsv

### Description
* Key hints. You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.
* ```wget http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz.```
* ```gunzip Homo_sapiens.GRCh37.75.gtf.gz"```
* Use script ens2hugo.py to match gene_id to gene_name using ens2gene dictionary
* Use ```mini.gtf``` for testing before running script with ```Homo_sapiens.GRCh37.75.gtf```
###### Unit Test
* Start your unit test by git clone https://github.com/davcraig75/rna files
```
with open ('rna/expression_results.csv') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[0] in ens2gene:
            row[0]=ens2gene[row[0]]
            print(row)
            print(ens2gene([row[0]], end=', ')
``` 
### Known Issues
* Confirm that gene_id and gene_name are matching using regex expression. This can be tricky as thre are many opportunities for mistakes in big files. 
* The file has ensembles that are repeats thus the gene namnes found in the dictionary will be reassigned multiple times to the same. This is redundant and I could filter this out but I decided to keep this step for now.

# histogram.py
### Usage
* python3 histogram.py [-f][0-9] [file] # name of the .csv file is included in the repository ```covid_local_adult_detention_fac.csv```

### Description
* Creates a histogram as a png from a file using the specified column in a tab delimited file.
* Options
    * -f An optional flag where -f is followed by a number 0-9 indicating which column to use to create the histogram.  If no option is selected, use the 2nd column
* Should be using pandas and numpy to create histogram. 
* Data file used in this example came from .csv file COVID-19 data set from [data.ca.gov/dataset](https://data.ca.gov/dataset/covid-19-in-local-adult-detention-facilities/resource/dadeb689-08e3-4fbd-ac09-c101bcb2f2b2)
    * Needed to convert this .csv file to a .tsv file before creating the data plot
### Known Issues
* ```ImportError: No module named matplotlib.pyplot```
    * This issue has yet to be resolved on local machine. Fixes involve uninstalling and reinstalling ```matplotlib```, confirimg ```matplotlib``` in PATH, or chaning python library in your script from #!/usr/bin/python to #!/usr/bin/env python
