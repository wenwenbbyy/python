fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
words=list()
for line in fh:
    print line
    line = line.rstrip()
    words=line.split()
    for word in words:
    	if word not in lst:lst.append(word)
lst.sort()
print lst