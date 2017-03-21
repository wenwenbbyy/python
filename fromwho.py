name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
counts=dict()
handle = open(name)
for line in handle:
	words=line.rstrip().split()
	if len(words)>0 and words[0]=='From':
		counts[words[1]]=counts.get(words[1],0)+1
print counts
maxnum=0
for who in counts:
	if counts[who]>maxnum : maxnum=counts[who]
print counts[maxnum]