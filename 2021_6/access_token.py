# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:53:52 2021

@author: Niji
"""

import requests 
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=your_client_id&client_secret=your_client_secret'

response = requests.get(host).json()

if response:
    with open('./access_token.txt', 'wb') as fp:
        fp.write(json.dumps(response).encode('utf-8'))
    
    print('success!')