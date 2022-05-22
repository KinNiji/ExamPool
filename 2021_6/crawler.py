# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:21:21 2021

@author: Niji
"""

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}

for i in range(1, 22):

    url = 'https://s3.ananas.chaoxing.com/doc/12/3e/4f/f2eabd462bea5eb1c4a544ecbe2cd486/thumb/{page}.png'.format(page=i)
    
    img_data = requests.get(url=url, headers=headers).content
    
    with open('./qb_res/modern_history/{page}.png'.format(page=i), 'wb') as fp:
        fp.write(img_data)
        
    print('{page}.png success!'.format(page=i))