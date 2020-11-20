# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 12:59:15 2020

@author: Administrator
"""
import requests

def main():
    lottery_request()

def lottery_request():
    #配置key
    appkey = '9cccc639b813dd68e133be6d4f0e05d3'
    
    #1.双色球开奖结果查询
    ssq_request(appkey)



def ssq_request(appkey):
    url = 'http://apis.juhe.cn/lottery/query'
    params = {
        'key' : appkey,#我申请的key
        'lottery_id' : 'ssq',#彩票id
        'lottery_no' : '',#指定彩票期号,默认最近
        'dtype' : 'json',#数据格式,xml或json,默认json
        }
    f = requests.get(url=url, params=params)
    res = f.json()
 
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            w = res["result"]
            ret = print('%s:' % w.get('lottery_name'),'\n',
                  '第%s期开奖结果 ' % w.get('lottery_no'),
                  '开奖日期:%s' % w.get('lottery_date'),'\n',
                  '中奖号码:  %s' % w.get('lottery_res'),'\n')
            print (type(ret))
            return ret
            
        else:
            error_ret = ("%s:%s" % (res["error_code"], res["reason"]))
            print (error_ret)
            return error_ret
          
    else:
        print("request api error")
        
if __name__ == '__main__':
    main()