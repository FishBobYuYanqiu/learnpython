# Exploring the HyperText Transport Protocol

# You are to retrieve the following document using the HTTP protocol in a 
# way that you can examine the HTTP Response headers.

# http://data.pr4e.org/intro-short.txt

# Way 1: In python
import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org",80))
a="GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
mysocket.send(a)
while True:
 	data=mysocket.recv(512)
 	if len(data)<1:
 		break
 	print(data.decode())
 	mysocket.close()

 # Way 2: Telnet
 # Type the following command into terminal
 # telnet data.pr4e.org 80
 # GET http://data.pr4e.org/intro-short.txt HTTP/1.0
 # Then hit enter twice