# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:56:35 2020

@author: Administrator
"""

import json
import requests

def main():
    lottery_request()
    
#所有开奖结果查询列表
def lottery_request():
    #配置key
    appkey = '9cccc639b813dd68e133be6d4f0e05d3'
    
    #1.双色球开奖结果查询
    ssq_request(appkey)
    
    #2.福彩3D开奖结果查询
    fcsd_request(appkey)
    
    #3.排列5开奖结果查询
    plw_request(appkey)
    
    #4.七星彩开奖结果查询
    qxc_request(appkey)
    
    #5.超级大乐透开奖结果查询
    dlt_request(appkey)
    
#ssq开奖结果查询
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
            print('%s:' % w.get('lottery_name'),'\n',
                  '第%s期开奖结果 ' % w.get('lottery_no'),
                  '开奖日期:%s' % w.get('lottery_date'),'\n',
                  '中奖号码:  %s' % w.get('lottery_res'),'\n')
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
        
#fcsd开奖结果查询
def fcsd_request(appkey):
    url = 'http://apis.juhe.cn/lottery/query'
    params = {
        'key' : appkey,#我申请的key
        'lottery_id' : 'fcsd',#彩票id
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
            print('%s:' % w.get('lottery_name'),'\n',
                  '第%s期开奖结果 ' % w.get('lottery_no'),
                  '开奖日期:%s' % w.get('lottery_date'),'\n',
                  '中奖号码:  %s' % w.get('lottery_res'),'\n')
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
 
#plw开奖结果查询
def plw_request(appkey):
    url = 'http://apis.juhe.cn/lottery/query'
    params = {
        'key' : appkey,#我申请的key
        'lottery_id' : 'plw',#彩票id
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
            print('%s:' % w.get('lottery_name'),'\n',
                  '第%s期开奖结果 ' % w.get('lottery_no'),
                  '开奖日期:%s' % w.get('lottery_date'),'\n',
                  '中奖号码:  %s' % w.get('lottery_res'),'\n')
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error") 
 
#qxc开奖结果查询
def qxc_request(appkey):
    url = 'http://apis.juhe.cn/lottery/query'
    params = {
        'key' : appkey,#我申请的key
        'lottery_id' : 'qxc',#彩票id
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
            print('%s:' % w.get('lottery_name'),'\n',
                  '第%s期开奖结果 ' % w.get('lottery_no'),
                  '开奖日期:%s' % w.get('lottery_date'),'\n',
                  '中奖号码:  %s' % w.get('lottery_res'),'\n')
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
        
#dlt开奖结果查询
def dlt_request(appkey):
    url = 'http://apis.juhe.cn/lottery/query'
    params = {
        'key' : appkey,#我申请的key
        'lottery_id' : 'dlt',#彩票id
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
            print('%s:' % w.get('lottery_name'),'\n',
                  '第%s期开奖结果 ' % w.get('lottery_no'),
                  '开奖日期:%s' % w.get('lottery_date'),'\n',
                  '中奖号码:  %s' % w.get('lottery_res'),'\n')
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
 
if __name__ == '__main__':
    main()