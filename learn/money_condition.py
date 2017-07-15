hour=input("Enter hours:")
rate=input("Enter rate")
hour=float(hour)
rate=float(rate)
if hour<40:
    money=hour*rate
else:
    money=40*rate+(hour-40)*rate*1.5
print(money)