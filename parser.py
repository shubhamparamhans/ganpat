import sys
import time;


class parser:
    def __init__(self,uri,the_data,h_link):
        self._uri=uri;
        self._data=the_data;
        self._home_url=h_link;
        
        self.links=[];
        self.images=[];
        self.links_counter=0;
        self.image_counter=0;
        
        try:
            self.data_loaded=open(uri,"r");
        except Exception:
            log_write="%s : Error in opening %s\n" %(time.ctime(time.time()),self._uri);
            self.write_log(log_write);
            sys.exit(2);
        log_write="%s : %s Successfully open\n" %(time.ctime(time.time()),self._uri);
        self.write_log(log_write);
        
    
    def parse(self):
        log_write="%s : Parsing %s begin.\n" %(time.ctime(time.time()),self._uri);
        self.write_log(log_write);
        
        the_data=self.data_loaded.read();
        
        index=0;
        the_data_len=len(the_data);
        while index<the_data_len:
            if the_data[index]=="<" :
                index=index+1;
                while the_data[index]==" ":
                    index=index+1;
                if the_data[index]=="a" and the_data[index+1]==" ":
                    while the_data[index]!="f" and the_data[index-1]!="e" and the_data[index-2]!="r" and the_data[index-3]!="h":
                        index=index+1;
                        if the_data[index]==">":
                            break;
                    if the_data[index]=="f" and the_data[index-1]=="e" and the_data[index-2]=="r" and the_data[index-3]=="h":
                        self.links_counter+=1;
                        index=index+2;
                        _quote=the_data[index];
                        index+=1;
                        a_link="";
                        while the_data[index]!=_quote:
                            a_link+=the_data[index];
                            index+=1;
                            
                        #self.links.append(self.check_rel_url(a_link));
                        self.links.append(a_link);

                
                
            #    if the_data[index]=="i" and the_data[index+1]=="m" and the_data[index+2]=="g" and the_data[index+3]==" " :
             #       print "IMG FOUND";

              #      while the_data[index-1]!=" " and the_data[index]!="s" and  the_data[index+1]!="r" and the_data[index+2]!="c":
               #         index+=1;
                #        if the_data[index]==">":
                 #           break;
                    
                  #  if the_data[index-1]==" " and (the_data[index]=="s" or the_data[index]=="S") and  (the_data[index+1]=="r" or the_data[index+1]=="R") and (the_data[index+2]=="c" or the_data[index+2]=="C"):
                   #     self.image_counter+=1;
                    #    index+=4;
                     #   _i_quote=the_data[index];
                      #  index+=1;
                       # img_link="";
                        #while the_data[index]!=_i_quote:
                        #    img_link+=the_data[index];
                         #   index+=1;
                        #self.images.append(img_link);
                    
                
                index=index+1;
            
            index=index+1;


        index=the_data_len-1;
        
        while index>0 :
            is_an_image=self.check_for_image(index,the_data);
            if is_an_image :
                self.image_counter+=1;
                magic_quote=the_data[index+1];
                img_link="";
                while the_data[index]!=magic_quote :
                    img_link=the_data[index]+img_link;
                    index-=1;
                self.images.append(img_link);

            index-=1;

        self.data_loaded.close();
        print "LINKS ARE: ",self.links_counter;
        print "IMAGES ARE: ",self.image_counter;
        
        log_write="%s : Parsing %s complete. %s links and %s images found.\n" %(time.ctime(time.time()),self._uri,self.links_counter,self.image_counter);
        self.write_log(log_write);
        
        return True;
        
    
    def links_are(self):
        
        return self.links;
        
    def images_are(self):
        
        return self.images;
        
    def write_log(self,log_info):
        try:
            log=open("logs/parser.log","a");
            log.write(log_info);
            print log_info;
            log.close();
        except Exception:
            print "Something went wrong. Cannot write log";
            sys.exit(2);
            
    def check_rel_url(self, a_url):
        if a_url.__contains__("http"):
            return a_url;
        else:
            ret_url=self._home_url+a_url;
            return ret_url;

    def check_for_image(self,index,data_is):
        if data_is[index]=="g" and data_is[index-1]=="p" and data_is[index-2]=="j" and data_is[index-3]=="." and (data_is[index+1]=="'" or data_is[index+1]=='"') :
            return True;
        elif data_is[index]=="g" and data_is[index-1]=="n" and data_is[index-2]=="p" and data_is[index-3]=="." and (data_is[index+1]=="'" or data_is[index+1]=='"'):
            return False;
        elif data_is[index]=="g" and data_is[index-1]=="e" and data_is[index-2]=="p" and data_is[index-3]=="j" and data_is[index-4]=="." and (data_is[index+1]=="'" or data_is[index+1]=='"'):
            return True;
        else :
            return False;

