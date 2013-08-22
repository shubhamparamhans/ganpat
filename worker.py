import socket
import time

_socket=socket.socket();
_host=socket.gethostname();
_port=7777;
_socket.connect((_host,_port));
while True:
	_recv=_socket.recv(1024);
	print _recv;
	if _recv=="STOP":
		break;

_socket.close();