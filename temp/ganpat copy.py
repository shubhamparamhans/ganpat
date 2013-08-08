import sys
import time
from downloader import downloader
print "*************GANPAT, THE CRAWLER**************";
if len(sys.argv)>1 :
    print "SITE: ",sys.argv[1]," started at ",time.ctime(time.time());
    down1=downloader(sys.argv[1]);
else :
	print "USAGE: python ganpat.py <sitename>";
	sys.exit(2);
