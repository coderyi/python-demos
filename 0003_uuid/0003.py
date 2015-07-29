__author__ = 'coderyi'
# -*- coding: utf-8 -*-
#07-28  uuid
#第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（
# 或者优惠券）？
#https://github.com/Show-Me-the-Code/python/tree/master/JiYouMCC/0001

import uuid

def create_code(number=200):
    result = []
    while True is True:
        temp = str(uuid.uuid1()).replace('-', '')
        if not temp in result:
            result.append(temp)
        if len(result) is number:
            break
    return result

print (create_code())

#http://www.cnblogs.com/dkblog/archive/2011/10/10/2205200.html
#Python使用UUID库生成唯一ID