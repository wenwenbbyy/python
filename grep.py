import re
num=0
regular=raw_input('input your regular expression:')
fhand=open('mbox.txt')
for line in fhand:
	line=line.rstrip()
	if re.findall(regular,line):
		num=1+num
print 'mbox.txt had ' + str(num) +' lines that matched '+regular