import socket
import sys
import time

sock=socket.socket();
host="127.0.0.1";
port=7777;
sock.bind((host,port));
sock.listen(5);
a=["hello","world","Mr.","Shubham","Rocks"];
c,addr=sock.accept();
file=open("gif.svg","r");
data=file.read();
while True:
	
	send=",".join(a)
	c.send(data);
	print "GOING TO SLEEP";
	time.sleep(5);
	print "OUT FROM SLEEP";
