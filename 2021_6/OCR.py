# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:51:48 2021

@author: Niji
"""

import requests
import base64

'''
通用文字识别
'''

access_token = '24.fe1d3296dfe5a26c4f74e53606afc5a6.2592000.1624615951.282335-24032237'

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + access_token

headers = {'content-type': 'application/x-www-form-urlencoded'}

for i in range(1, 22):
    # 二进制方式打开图片文件
    f = open('./qb_res/modern_history/cut/{page}.png'.format(page=i), 'rb')
    img = base64.b64encode(f.read())
    
    params = {"image":img}
    
    response = requests.post(request_url, data=params, headers=headers).json()
    
    if response:
        result = response['words_result']
        words_list = []
        for words in result:
            words_list.append(words['words'])
        
        with open('./qb_res/modern_history/all.txt', 'ab') as fp:
            for words in words_list:
                fp.write('{words}\n'.format(words=words).encode('utf-8'))
        
    print('{page}.png success!'.format(page=i))