import socket
import time
import sys
from ClusterConnect import ClusterConnect

_workers=[];
_links=[];
_imgs=[];
_d_links=[];
_d_imgs=[];

_c_connect=ClusterConnect();
_c_connect.start();

print "********************GANPAT********************\n";
print "1.Start CRAWLER";
print "2.Show CLUSTER";
print "3.Exit";
_inp==raw_input("Enter: ")
while True:
	_inp=raw_input("Enter command: ");
	if _inp=="HELP":
		print "Enter STOP to stop cluster server.";
		print "Enter EXIT to stop program and exit";
		print "Enter CRAWL to start crawling."
		print "Enter CLUSTER to see status of cluster.";
	elif _inp=="EXIT" :
		_c_connect.join(0);
		_c_connect.close();
		sys.exit(2)
	elif _inp=="STOP" :
		break;
	elif _inp=="CRAWL":
		_site_name=raw_input("Enter site name: ");
		_site_url=raw_input("Enter site url: ");
	elif _inp=="CLUSTER":
		_workers=_c_connect.workers();
		print "%s workers connected."%(len(_workers));
		for node in _workers:
			print node.getsockname();
			node.send("Hello workers");
	else:
		print "Enter HELP for help";

print "Stopping cluster server thread"; 
_c_connect.join(0);
_c_connect.close();
_c_connect.send("STOP");
#for client in _workers:
#	print "Connection from: ",client;
#	client.close();


print "EXITING MAIN THREAD, bYe";
sys.exit(0);

def _connect(stop_event):
	_socket.listen(22);
	print "%s : Server started on %s:%s" %(time.ctime(time.time()),_host,_port);
	while (not stop_event.is_set()):
		c,addr=_socket.accept();
		print "Got connection from ",addr;
		c.send("Connected");
		_workers.append(c);

#_c_stop=threading.Event();
#_c=threading.Thread(target=_connect,args=(_c_stop));