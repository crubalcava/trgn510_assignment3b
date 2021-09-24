import re

file = "mytextfile.txt"

phonenum=[]
with open(file) as f:
	for line in f:
		text=line
		phoneNumRegex = re.compile(r'((?:\+[0-9]+\s*)?[(]?(?:\d{2,})?[)](?:\s|-|\.)?(?:\d{3,})(?:\s|-|\.)(?:\d{3,}))',re.VERBOSE)
for match in phoneNumRegex.findall(text):
			phonenum.append(match)

print(phonenum)
