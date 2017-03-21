def chop(t):
	del t[0]
	del t[-1]
def midell(t):
	return t[1:len(t)]
ls=[1,2,3,4,5]
#print chop(ls)
print midell(ls)
print ls
