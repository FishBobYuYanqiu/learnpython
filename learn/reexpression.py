# Finding Numbers in a Haystack

# In this assignment you will read through and parse a file with text and 
# numbers. You will extract all the numbers in the file and compute the 
# sum of the numbers.
import re
sum=0
fname=input("Enter file name: ")
try:
	handle=open(fname)
except:
	print("Invalid file name")
	quit()
for line in handle:
	numbers=re.findall("[0-9]+",line)
	if numbers is None:
		continue
	for number in numbers:
		number=int(number)
		sum=sum+number
print("The sum is:",sum)

# Another more compact way to do this homework
# import re
# print(sum(int(i) for i in re.findall("[0-9]+",open("regex_sum_9514.txt").read())))im