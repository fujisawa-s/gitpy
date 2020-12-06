# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:52:11 2020

@author: Administrator
"""
import requests

appkey = "b8118458ce9fb15e78c09a5b6edbd183"

def main():
    print(get_fortune_star('水瓶座'))
    

def get_fortune_star(cn): #cn为星座名称
    url = "http://web.juhe.cn:8080/constellation/getAll"
    params = {
        "consName": cn ,  #星座名称
        "type" : 'today' ,#运势类型：today,tomorrow,week,month,year
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json
    }
 
    f = requests.get(url=url, params=params)
    res = f.json()
 
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            w = res
            ret_tuple =('<%s>今日运势(ﾉﾟ∀ﾟ)ﾉ ' % w.get('name'),'\n',
                        '*幸运色*   %s' % w.get('color'),'\n',
                        '*幸运数字* %s' % w.get('number'),'\n',
                        '*速配星座* %s' % w.get('QFriend'),'\n','\n'
                        '年轻人!把握今天,耗子尾汁:','\n',
                        '%s' % w.get('summary'),'\n','\n',
                        '*综合指数: %s*' % w.get('all'),'\n',
                        '健康:%s ' % w.get('health'),
                        '爱情:%s ' % w.get('love'),
                        '财运:%s ' % w.get('money'),
                        '工作:%s ' % w.get('work'),
                        '财运:%s' % w.get('love'))
            ret_str= ''.join(ret_tuple)
            return ret_str
        
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
 
 
        
if __name__ == '__main__':
    main()