import threading
import sys
import time
import os
import socket

class ClusterConnect(threading.Thread):
	def __init__(self):
		super(ClusterConnect,self).__init__();
		self.stop_request=threading.Event();
		self._workers=[];
		self._socket=socket.socket();
		self._host=socket.gethostname();
		self._port=7777;
		self._socket.bind((self._host,self._port));
		
	def set_stop(self):
		self.stop_request.set();

	def join(self,timeout=None):
		self.stop_request.set();
		super(ClusterConnect,self).join(timeout);

	def close(self):
			self._socket.close();

	def workers(self):
		return self._workers;

	def send(self,msg):
		for node in self._workers:
			node.send(msg);

	def run(self):
		self._socket.listen(22);
		print "%s : Server started on %s:%s" %(time.ctime(time.time()),self._host,self._port);
		while (not self.stop_request.is_set()):
			c,addr=self._socket.accept();
			print "Got connection from ",addr;
			c.send("Connected");
			self._workers.append(c);