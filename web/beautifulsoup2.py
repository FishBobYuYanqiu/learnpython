# In this assignment you will write a Python program that expands on 
# http://www.py4e.com/code3/urllinks.py. The program will use urllib to 
# read the HTML from the data files below, extract the href= vaues from 
# the anchor tags, scan for a tag that is in a particular position 
# relative to the first name in the list, follow that link and repeat the 
# process a number of times and report the last name you find.
from urllib import request,error,parse
from bs4 import BeautifulSoup
myurl=input("Enter url: ")
names=list()
if len(myurl)==0:
	myurl="http://py4e-data.dr-chuck.net/known_by_Lang.html"
for i in range(7):
	print("Retrieving:",myurl)
	handle=request.urlopen(myurl).read()
	soup=BeautifulSoup(handle,'html.parser')
	tag=soup.find_all("a")[17]
	print(tag)
	name=tag.contents
	myurl=tag.get("href",None)
	names.append(name)
print("Sequence of name",names)