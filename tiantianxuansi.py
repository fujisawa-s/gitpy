# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:51:32 2020

@author: Administrator
"""

import requests

url = 'http://gwgp-rbyicnjevk7.n.bdcloudapi.com/caipiao/query?caipiaoid=97'
params = {
        'AppKey' : '360de7785d6f498ebb4e1a375cb1e509',#我申请的key
        'X-Bce-Stage' : 'release',
        'Content-Type' : 'application/json; charset=utf-8'
        }

r = requests.post(url = url, params=params)
res = r.json()

w = res["result"]
print(w)