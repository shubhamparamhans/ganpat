import time
from parser import parser
from downloader import downloader
from ClusterConnect import ClusterConnect

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
    				self.remove_duplicate(1,parse_links);
    				parse_img=parse.images_are();
    				self.remove_duplicate(2,parse_img);
    	else:
    		print "Error in downloading %s. Now exitting"%(self._siteurl);
    		sys.exit(0);

    def run(self):
        while True:
            if len(_links)!=0:
                _down=downloader(self,self._sitename,_links.pop(0));
                if _down.download():
                    _parse=parser(_down._save_location(),_down._data_is(),self._siteurl);
                    if _parse.parse():
                        _parse_links=_parse.links_are();
            elif len(_images)!=0:

            else:
                continue;

    def check_rel(self,links,_rel):
        ret_data=[];
    	for alink in links:
    		if not(alink.__contains__(rel)):
    			alink=self._siteurl+alink;
            ret_data.append(ret_data);
    	return ret_data;

    def remove_duplicate(self,flag,t_data):
        data_len=len(t_data);
        add_counter=0;
        if flag==1:
            for s_link in t_data:
                if not(_links.__contains__(t_data)):
                    _links.append(t_data);
                    _d_links.append(t_da
        elif flag==2:
            for s_img in t_data:
                if not(_images.__contains__(t_data)):
                    _images.append(t_data);
                    _d_images.append(t_data);

    def add_data(self,flag,t_data):
        if flag==0:
            _links.append(t_data);
            _d_links.append(t_data);
        elif flag==1:
            _images.append(t_data);
            _d_images.append(t_data);


