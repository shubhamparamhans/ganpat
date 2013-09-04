import socket
import time
import sys

sock=socket.socket();
host="127.0.0.1";
port=7777;
sock.connect((host,port));
while True:
	recv=sock.recv(10000);
	print recv;
	time.sleep(2);