num=0
while True:
	try:
		x=raw_input ('> ')
		y[num]=float(x)
		if x=='done':
			print len(y)
			print sum(y)
			print max(y)
			break
	except:
		continue;