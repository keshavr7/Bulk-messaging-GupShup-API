'''
Created on 7 Jan 2015

@author: KRaghu
'''
from iniparse import INIConfig
import requests
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
import csv

import urllib

if __name__ == '__main__':
    cfg = INIConfig(open('constants.ini'))
    userid = cfg['Details']['userId']
    password = cfg['Details']['password']
    msg = cfg['Details']['message']
    method = cfg['General']['method']
    msgType = cfg['General']['msg_type']
    fileType = cfg['General']['filetype']
    version = cfg['General']['version']
    auth = cfg['General']['auth_scheme']
    url = cfg['General']['url']
    
    values = {'method' : method, 'auth_scheme': auth , 'password' : password, 'userid' : userid, 'msg_type' : msgType, 'filetype' : fileType, 'v' : version, 'msg' : msg}
    #url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?"+data
    
        
    #files = {'file': open('C:\Users\kraghu\workspace\gupshupMessaging\src\gupshup.csv', 'rb')}
    #files = {'file': ('common.csv', open('common.csv', 'rb'))}
    #r = requests.post(url, files= files, data=values)
    #print(r.status_code)
    #print (r.text)
    postMsgUrl = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=xlsUpload&filetype=csv&msg=%s&userid=%s&password=%s&v=1.1\
    &msg_type=TEXT&auth_scheme=PLAIN" % (msg, userid, password)
    
    register_openers()
    
    message = "Yo %VAR1 \n Great job!! \n #SlowClaps"
    
    passtup = {'x' : message}
    temp =  urllib.urlencode(passtup)
    finmessage = temp[2:]
    
    
    data = [["PHONE", "%VAR1"],["9035357336","KESHAV"],["9901871696", "Mohanty"]]
  
    with open("myfile.csv","w") as f:
        writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_ALL)
        writer.writerows(data)
    f.close()
         
        

        
    datagen, headers = multipart_encode({"file": open("myfile.csv" , "rb"), "method" : method, "auth_scheme": auth , "password" : password, "userid" : userid, "msg_type" : msgType, "filetype" : fileType, "v" : version, "msg" : finmessage })

    request = urllib2.Request(url, datagen, headers)
    response =  urllib2.urlopen(request)
    print response.read()
    
    
    
    
    

