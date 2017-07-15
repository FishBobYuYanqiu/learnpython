# 5.2 Write a program that repeatedly prompts a user 
# for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and 
# smallest of the numbers. If the user enters anything 
# other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.
largest_sofar=None
smallest_sofar=None
while True:
	number=input("Please enter integer:")
	if number=="done":
		largest=largest_sofar
		smallest=smallest_sofar
		break
	try:
		number=int(number)
	except:
		print("Invalid input")
		continue
	if largest_sofar is None:
		largest_sofar=number
		smallest_sofar=number
	if largest_sofar<number:
		largest_sofar=number
	if smallest_sofar>number:
		smallest_sofar=number
print("Maximum is",largest)
print("Minimum is",smallest)