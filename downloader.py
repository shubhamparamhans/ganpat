import time
import urllib2
import sys
import os

class downloader:
    
    _site_name="";
    _site_url="";
    _start_time="";
    
    def __init__(self,site_name,site_url):
        self._site_name=site_name;
        self._site_url=site_url
    
    def download(self):
            log_write="%s : Started downloading %s \n" %(time.ctime(time.time()), self._site_url);
            self._write_log(log_write);
           
            conn=urllib2.urlopen(self._site_url);
            response=conn.getcode();
            data=conn.read();
            self._data=data;
            meta=conn.info();
            
            log_write="%s : Downloading %s complete\n" %(time.ctime(time.time()), self._site_url);
            self._write_log(log_write);
            
            if int(response) is 200:
                log_write="%s : %s response code 200\n" %(time.ctime(time.time()),self._site_url);
                self._write_log(log_write);
                self._data=str(data);
                if self._site_url[len(self._site_url)-1]=="/":
                    self._site_url=self._site_url[0:len(self._site_url)-2];
    
                self._name_to_save=self._site_url[self._site_url.rfind("/")+1:len(self._site_url)];
                print self._name_to_save;
                
                if self._is_image() :
                    location_folder="../crawl data/%s/image/" %(self._site_name);
                    if not os.path.exists(location_folder):
                        os.makedirs(location_folder);
                    self._location_to_save="../crawl data/%s/image/%s" %(self._site_name,self._name_to_save);
                    data_to_save=open(self._location_to_save,"w");
                    data_to_save.write(data);
                
                    data_to_save.close();
                else :
                    self._location_folder="../crawl data/%s/data/" %(self._site_name);
                    if not os.path.exists(self._location_folder):
                        os.makedirs(self._location_folder);
                    self._location_to_save="../crawl data/%s/data/%s" %(self._site_name,self._name_to_save);
                    data_to_save=open(self._location_to_save,"w");
                    data_to_save.write(data);    
                    data_to_save.close();
            else :
                log_write="%s : Some error happend while downloading %s(code %s)" %(time.ctime(time.time()),self._site_url,response);
                self._write_log(log_write);
                return False;
                
            return True;
        
    def _write_log(self,data):
        print data;
        try:
            logfile=open("logs/download.log","a");
            logfile.write(data);
            logfile.close();
        except Exception:
            print "%s: There was some problem with writing log" %(time.ctime(time.time()));
            return False;
            
        return True;
        
    def _is_image(self):
        if self._site_url.find(".png") > 0:
            return True;
        elif self._site_url.find(".jpg") > 0:
            return True;
        elif self._site_url.find(".jpeg") > 0: 
            return True;
        else:
            return False;
    
    def _save_location(self):
        return self._location_to_save;
        
    def _data_is(self):
        return self._data;


