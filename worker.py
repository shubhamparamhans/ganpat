import socket
import time
import sys
from ganpat_temp import ganpat
import thread

_socket=socket.socket();
_host=socket.gethostname();
_port=7777;

_sitename="";
_siteurl="";

_links=[];
_imgs=[];

_r_links=[];
_r_imgs=[];

_d_links=[];
_d_imgs=[];

try:
	_socket.connect((_host,_port));
except Exception:
	print "There was some problem in connecting the worker. Please check connections";
	print Exception;
	sys.exit(1);

while not(_data=_socket.recv(4048)):
	continue;

_data=_data.split(",");
a_ganpat=ganpat(_data[0],_data[1]);


while True:
	if _socket.recv(4048)==None:

	else:
		_recv=_socket.recv(4048);
		print _recv;
	print _recv;
	if _recv=="STOP":
		break;
	else:
		

_socket.close();