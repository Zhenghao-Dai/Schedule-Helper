#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
url = "http://wxpusher.zjiecode.com/api/send/message"
data = {"appToken": "AT_6oRXaKOQV9HJoAIPMbIRTgZ0af13hOxF",
        "content": "wdnmd",
        "contentType": 1, 
        "topicIds": [ 
                     123
                     ],
        "uids": [
                'UID_suhLU94hlXsi8wkPjPb2LNy1TK9d'
                #"UID_pjpXX6SP5d3TSJ22h4uuqjMjaI1K"
        ]
        
}
payload = {
    "appToken": "AT_6oRXaKOQV9HJoAIPMbIRTgZ0af13hOxF",
    "content": "wdnmd",
    "uid":'UID_suhLU94hlXsi8wkPjPb2LNy1TK9d'
}
          
r = requests.get(url=url, params=payload)

body={
    "appToken": "AT_6oRXaKOQV9HJoAIPMbIRTgZ0af13hOxF",
    "extra": "312",     
    }
#r1 = requests.post(url=url, data=data).json()
print(r.json())    

