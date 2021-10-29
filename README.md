# trgn_assignment3bssignment 3B
##  extract_phonenum.py

### Usage
* python3 extract_phonenum.py
* mytextfile.txt #Use this file as a unit test.

### Description
* Extracts phone numbers from a text file, and prints formatted phone numbers.
* One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number].
* Create a script called extract_phonenum.py which extracts phone numbers from text file

### Known Issues
* This program will only work for phone numbers that are formatted as [+][country code] ([AreaCode]) [local phone number].
    * To format a match you can try to use print('+%s (%s) %s-%s').

##  ens2hugo.py
### Usage
* python3 ens2hugo.py [file]
* Use the following repository to convert gtf file to csv for usage of this script: https://github.com/zyxue/gtf2csv.git

### Description
* You will need to download the Homo_sapiens.GRCh37.75.gtf yourself as it is too big to keep on the github.
```
wget http://ftp.ENSEMBL.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz | gunzip
```
* The purpose of this script is to convert the ENSEMBL ID to HUGO ID in the file that is being called.
###  Unit Test
* Unit test can be found here: https://github.com/davcraig75/rna.git. 

### Known Issues
* Input file [-f] needs to be identified in the usage of the script, otherwise  -f parameter will be treated as the input file and give an error. 
* Homo_sapiens file called in above needs to be in the main directory so script will know to call it. If it is not, you will need to specify directory within script.
* Need to go in and specify the file names within the script and confirm that the file is in the main repository. If is is not, you will receive an error message and will need to specify the directory within the script. 

# histogram.py
### Usage
* python3 histogram.py [file]
* Unit test can be found here: https://github.com/davcraig75/rna.git
* File used is trgn599.clinical.csv. 
* Confirm that the file being used is in csv format.

### Description
* Creates a histogram as a png from a file using the specified column in a tab delimited file.

### Known Issues
* To see different data from a separate column plotted, change the index col to desired column.
