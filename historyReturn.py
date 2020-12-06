# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:22:43 2020

@author: Administrator
"""

import requests
import datetime
import random

appkey = "a7584d259fc577693bdae3e99fc9511c"
month = ('%s' % datetime.datetime.now().month)
day = ('%s' % datetime.datetime.now().day)


def main():
    print(set_history_date())
    

def set_history_date():
    url = "http://api.juheapi.com/japi/toh"
    params = {
        "month": month,  #月份
        "day": day,  #日期
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
            
            def get_each(x): #x为决定输出第几条历史
                one_news = w[x]
                ret_tuple =('[%s]' % one_news.get('year'),
                            '%s' % one_news.get('title'),'\n'
                           )
                ret_str= ''.join(ret_tuple)
                return ret_str
            
            
            number1 = (random.randint(0,9))
            number2 = (random.randint(10,19))
            renumber1 = (random.randint(-10,-1))
            renumber2 = (random.randint(-20,-11))
            n1 = get_each(renumber1)
            n2 = get_each(renumber2)
            n3 = get_each(number2)
            n4 = get_each(number1)
            return n1+n2+n3+n4
        
        
if __name__ == '__main__':
    main()