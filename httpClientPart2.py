import requests
SERVER = 'http://34.255.116.38:11337/bab12bscfgeg2d2d2bd2b'
response = requests.get(SERVER)
if response.status_code == requests.codes.ok:
    #print (response.status_code)
    #print (response.json)
    print (response.text)
    #server_response = requests.post(SERVER, data='bab12bscfgeg2d2d2bd2b')
    #print (server_response.status_code)
    #print (server_response.json)
    #print (server_response.text)
# r = requests.post(url, data=json.dumps(payload), headers=headers)
#"http://52.211.128.190:11337"
#Level 1 Token: bab12bscfgeg2d2d2bd2b
#Level 2 Token: bsadg2342bfeds235sge2
