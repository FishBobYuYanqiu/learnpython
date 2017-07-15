def computepay(hours,rate):
	if hours<40:
	    pay=hours*rate
	else:
		pay=40*rate+(hours-40)*rate*1.5
	return pay
hours=input("Enter hours")
rate=input("Enter rate")
hours=float(hours)
rate=float(rate)
money=computepay(hours,rate)
print(money)