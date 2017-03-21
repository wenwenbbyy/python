import re
filename=raw_input('Enter file:')
fhand=open(filename)
fl=list()
for line in fhand:
	line=line.rstrip()
	stuff=re.findall('^New Revision: ([0-9]+)',line)
	if len(stuff)>0:
		fl.append(float(stuff[0]))
print sum(fl)/len(fl)