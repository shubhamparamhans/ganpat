import sys
import time
from downloader import downloader
from parser import parser

print "*************GANPAT, THE CRAWLER**************";
_links=[];
_images=[];
_d_links=[];
_d_images=[];

def rem_dup(check_var,temp_data):
    temp_data_len=len(temp_data);
    add_counter=0;
    if check_var==1:
        for zxc in range(0,temp_data_len):
            if not(_links.__contains__(temp_data[zxc])):
                _links.append(temp_data[zxc]);
                _d_links.append(temp_data[zxc]);
                add_counter+=1;
        print "%s : %s new links added" %(time.ctime(time.time()),add_counter);

    elif check_var==2:
        for zxc in range(0,temp_data_len):
            if not(_images.__contains__(temp_data[zxc])):
                _images.append(temp_data[zxc]);
                _d_images.append(temp_data[zxc]);
                add_counter+=1;
        print "%s : %s new images added" %(time.ctime(time.time()),add_counter);

def check_rel(temp_data,check_data,add_data) :
    temp_data_len=len(temp_data);
    for zxc in range(0,temp_data_len):
        if not(temp_data[zxc].__contains__(check_data)):
            temp_data[zxc]=add_data+temp_data[zxc];

    return temp_data;


if len(sys.argv)>2 :
    print "SITE: ",sys.argv[1]," started at ",time.ctime(time.time());
    down1=downloader(sys.argv[1],sys.argv[2]);
    if down1.download():
        parse1=parser(down1._save_location(),down1._data_is(),sys.argv[2]);
        if parse1.parse():
            temp_links=parse1.links_are();
            temp_links=check_rel(temp_links,"http://",sys.argv[2]);
            rem_dup(1,temp_links);
            temp_img=parse1.images_are();
            rem_dup(2,temp_img);
        while len(_d_links)!=0 :
            temp_down=downloader(sys.argv[1],_d_links.pop());
            if temp_down.download():
                temp_parser=parser(temp_down._save_location(),temp_down._data_is(),_d_links.pop());
                if temp_parser.parse():
                    temp_links=temp_parser.links_are();
                    temp_links=check_rel(temp_links,"http://",sys.argv[2]);
                    rem_dup(1,temp_links);
                    temp_img=temp_parser.images_are();
                    rem_dup(2,temp_img);


else :
	print "USAGE: python ganpat.py <sitename> <siteurl>";
	sys.exit(2);

def cross_check(a_temp,check_var):
    return_data=[];
    _data_len=len(a_temp);
    if check_var==1:
        for z_x_c in range(0,_data_len):
            if  not(_links.__contains__(a_temp[z_x_c])) :
                return_data.append(a_temp[z_x_c]);
    elif check_var==2:
        for z_x_c in range(0,_data_len):
            if not(_links.__contains__(a_temp[z_x_c])) :
                return_data.append(a_temp[z_x_c]);
    return return_data;

def write_log(log_info):
        try:
            log=open("logs/ganpat.log","a");
            log.write(log_info);
            print log_info;
            log.close();
        except Exception:
            print "Something went wrong. Cannot write log";
            sys.exit(2);


