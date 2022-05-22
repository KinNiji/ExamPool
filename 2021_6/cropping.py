# -*- coding: utf-8 -*-
"""
Created on Wed May 26 22:58:55 2021

@author: Niji
"""

from PIL import Image

for i in range(1, 22):
    srcPath = './question_bank/modern_history/png/{page}.png'.format(page=i)
    dstPath = './question_bank/modern_history/cut/{page}.png'.format(page=i)
    
    # 读取图片
    img_1 = Image.open(srcPath)
    # 设置裁剪的位置
    crop_box = (139,115,883,1331)
    # 裁剪图片
    img_2 = img_1.crop(crop_box)
    # print("format---before:",img_1.format,",after:",img_2.format)
    # print("mode---before:",img_1.mode,",after:",img_2.mode)
    # print("size---before:",img_1.size,",after:",img_2.size)
    # print("width---before:",img_1.size[0],",after:",img_2.size[0])
    # print("height---before:",img_1.size[1],",after:",img_2.size[1])
    img_2.save(dstPath)
    
    print('{page}.png success!'.format(page=i))
