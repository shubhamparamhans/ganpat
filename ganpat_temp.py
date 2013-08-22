import time
from parser import parser
from downloader import downloader

class ganpat:
    def __init__(self,site_name,site_url):
        self._sitename=site_name;
        self._siteurl=site_url;
        self._links=[];
        self._images=[];
        self._d_links=[];
        self._d_images=[];

    def start(self) :
    	down=downloader(self._sitename,self._siteurl);
    	if down.download():
    		parse=parser(down._save_location(),down._data_is(),self._siteurl)
    			if parse.parse():
    				parse_links=parse.links_are();
    				parse_links=self.check_rel(parse_links,"http://");
    				self.remove_duplicate()
    	else:
    		print "Error in downloading %s. Now exitting"%(self._siteurl);
    		sys.exit(0);


