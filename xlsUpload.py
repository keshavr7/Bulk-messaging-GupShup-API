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

    # Fetching user details and API usage mode from config file
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

    values = {'method': method, 'auth_scheme': auth,
              'password': password, 'userid':
              userid, 'msg_type': msgType, 'filetype': fileType,
              'v': version, 'msg': msg}

    postMsgUrl = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=xlsUpload&filetype=csv&msg=%s&userid=%s&password=%s&v=1.1\
    &msg_type=TEXT&auth_scheme=PLAIN" % (msg, userid, password)

    register_openers()

    # This bit is optional
    # Here we are constructing the .csv file with some data.
    # Ignore this bit if you already have a fully populated .csv file
    data = [["PHONE", "%VAR1", "%VAR2"], ["9*********6", "K****V", "500"],
            ["9*******6", "M*****y", "300"]]

    with open("sampleFile.csv", "w") as f:
        writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerows(data)
    f.close()

    # API mandates to encode the message
    passtup = {'x': msg}
    temp = urllib.urlencode(passtup)
    finmessage = temp[2:]

    datagen, headers = multipart_encode({"file": open("sampleFile.csv", "rb"), "method": method,
                                         "auth_scheme": auth, "password": password, "userid": userid,
                                         "msg_type": msgType, "filetype": fileType, "v": version, "msg": finmessage})

    # Makeing the HTTP POST request
    request = urllib2.Request(url, datagen, headers)
    response = urllib2.urlopen(request)
    print response.read()
