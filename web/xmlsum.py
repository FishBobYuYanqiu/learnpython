# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to 
# http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, 
# read the XML data from that URL using urllib and then parse and extract 
# the comment counts from the XML data, compute the sum of the numbers in 
# the file.
import xml.etree.ElementTree as ET
from urllib import request,error,parse
sum=0
myurl=input("Enter url: ")
if len(myurl)<1:
	myurl="http://py4e-data.dr-chuck.net/comments_9518.xml"
data=request.urlopen(myurl).read()
tree=ET.fromstring(data)
tags=tree.findall("comments/comment")
for tag in tags:
	number=tag.find("count").text
	number=int(number)
	sum=sum+number
print("Sum is:",sum)