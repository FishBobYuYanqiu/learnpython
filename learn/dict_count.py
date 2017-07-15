# 9.4 Write a program to read through the mbox-short.txt and figure out 
# who has the sent the greatest number of mail messages. The program 
# looks for 'From ' lines and takes the second word of those lines as the 
# person who sent the mail. The program creates a Python dictionary that 
# maps the sender's mail address to a count of the number of times they 
# appear in the file. After the dictionary is produced, the program reads 
# through the dictionary using a maximum loop to find the most prolific committer.

# Read the text as lines
fname=input("Enter the file name: ")
if len(fname)==0:
	fname="mbox-short.txt"
try:
	handle=open(fname)
except:
	print("Invaild file name")
	quit()

# generate the dictionary
counts=dict()
for line in handle:
	words=line.split()
	if line.startswith("From") and len(words)>2:
		word=words[1]
		counts[word]=counts.get(word,0)+1

# find the largest number in the dictionary
committer=None
times=None
for k,v in counts.items():
	if times is None or counts[k]>times:
		committer=k
		times=v
print(committer,times)