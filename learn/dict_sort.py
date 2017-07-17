# 10.2 Write a program to read through the mbox-short.txt and figure out 
# he distribution by hour of the day for each of the messages. You can 
# pull the hour out from the 'From ' line by finding the time and then 
# splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the 
# counts, sorted by hour as shown below.

# Open and read the file
fname=input("Enter file name: ")
if len(fname)==0:
	fname="mbox-short.txt"
try:
	handle=open(fname)
except:
	print("Invalid file name")
	quit()
counts=dict()

# Extract lines and hours, construct dictionaries
for line in handle:
	line=line.strip()
	line1=line.split()
	if line.startswith("From") and len(line1)>2:
		word=line1[5]
		time=word.split(":")
		hour=time[0]
		counts[hour]=counts.get(hour,0)+1

# sort the dictionary by hour and print
count=sorted(counts.items())
for i,j in count:
	print(i,j)