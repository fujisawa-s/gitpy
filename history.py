# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:16:38 2020

@author: Administrator
"""

import requests
import datetime

def main():
    # 配置APPKey
    appkey = "a7584d259fc577693bdae3e99fc9511c"
 

    print(request1(appkey))
 
     
 

def request1(appkey):
    url = "http://api.juheapi.com/japi/toh"
    params = {
        "month": "11",  
        "day": "20",
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json
    }
 
    f = requests.get(url=url, params=params)
    res = f.json()
 
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            w = res["result"]
            
            def get_each(x): #x为决定输出第几条新闻
                one_news = w[x]
                ret_tuple =('%s' % one_news.get('title'),'\n',
                        '%s' % one_news.get('year'),'\n')
                ret_str= ''.join(ret_tuple)
                return ret_str
            
            n1 = get_each(-1)
            n2 = get_each(-2)
            n3 = get_each(-3)
            n4 = get_each(-4)
            n5 = get_each(-5)
            return n1+n2+n3+n4+n5
            
           
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
 
 
if __name__ == '__main__':
    main()