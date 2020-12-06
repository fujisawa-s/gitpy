# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:16:38 2020

@author: Administrator
"""

import requests
import datetime

#设定key
appkey = "f77da896d7893815c1694347edc340ef"
#设定时间,按照y-m-d格式


def main():

    print(set_almanac_date())
 
     
 

def set_almanac_date():
    #设定时间,按照y-m-d格式
    i = datetime.datetime.now()
    dat_ori = str("%s-%s-%s" % (i.year,i.month,i.day) )
    dat = dat_ori.replace(" ", "")
    
    url = "http://v.juhe.cn/calendar/day"
    params = {
        "date": dat,  
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
            a = w.get('data')
            ret_tuple = ('%s ' % a.get('date'),
                         '%s' % a.get('weekday'),'\n',
                         '农历: %s ' % a.get('lunar'),
                         '%s' % a.get('lunarYear'),'\n',
                         '今日宜: %s' % a.get('suit'),'\n',
                         '今日忌: %s' % a.get('avoid'))
            ret_str= ''.join(ret_tuple)
            return ret_str
            
           
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
 
 
if __name__ == '__main__':
    main()