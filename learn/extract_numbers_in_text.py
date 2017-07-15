# 7.2 Write a program that prompts for a file name, then opens that 
# file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each 
# of the lines and compute the average of those values and produce an 
# output as shown below. Do not use the sum() function or a variable 
# named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
#  you are testing below enter mbox-short.txt as the file name.
confidence=0
n=0
fname=input("Enter file name")
try:
    handle=open(fname)
except:
	print("Invalid file name")
	quit()
for line in handle:
	if 'X-DSPAM-Confidence:' in line:
		index=line.find(":")
		number=line[index+1:]
		number=float(number)
		n=n+1
		confidence=confidence+number
confidence=confidence/n
print("Average spam confidence:",confidence)