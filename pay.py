def computepay(hours,rate):
	if hours>=40:
		pay=hours*rate+(hours-40)*1.5
	else :
		pay=hours*rate
	print "Pay:"+str(pay)

hours= float(raw_input("Hours:"))
rate= float(raw_input("Rate:"))
computepay(hours,rate)