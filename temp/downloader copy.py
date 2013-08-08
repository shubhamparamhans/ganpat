import time
import urllib2
import sys
import os

class downloader:
    
    _site_name="";
    _site_url="";
    _start_time;
    
    def __init__(self,site_name,site_url):
        self._site_name=site_name;
        self._site_url=site_url
    
    def download(self):
        try:
            log_write="%s : Started downloading %s \n" %(time.ctime(time.time()), self._site_name);
            self._write_log(log_write);
           
            conn=urllib2.urlopen(self._site_url);
            response=conn.getcode();
            data=conn.read();
            
            meta=conn.info();
            
            log_write="%s : Downloading %s complete\n" %(time.ctime(time.time()), self._site_name);
            self._write_log(log_write);
            
            
            if int(response) is 200:
                log_write="%s : %s response code 200" %(self._site_name);
                self._write_log(log_write);
                self._data=str(data);
                self._name_to_save=self._site_url.rfind("/")
                if self._is_image() :
                    location_folder="data/%s/%s/image/" %(self._site_name,time.ctime(time.time()));
                    if not os.path.exists(location_folder):
                        os.mkdir(location_folder);
                    location_to_save="data/%s/%s/image/%s" %(self._site_name,time.ctime(time.time()),self._name_to_save);
                    data_to_save=open(location_to_save,"w");
                    data_to_save.write();
                else :
                    location_folder="data/%s/%s/data/" %(self._site_name,time.ctime(time.time()));
                    if not os.path.exists(location_folder):
                        os.mkdir(location_folder);
                    location_to_save="data/%s/%s/data/%s" %(self._site_name,time.ctime(time.time()),self._name_to_save);
                    data_to_save=open(location_to_save,"w");
                    data_to_save.write();    
                    
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
        if self._site_url.find(".png") is > 0:
            return True;
        elif self._site_url.find(".jpg") is > 0:
            return True;
        elif self._site_url.find(".jpeg") is > 0: 
            return True;
        else:
            return False;
        

