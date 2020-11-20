# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:17:20 2020

@author: Administrator
"""
import requests

def main():
    print(lottery_all())

akey = '9cccc639b813dd68e133be6d4f0e05d3'

def lottery_request(cpid):
    url = 'http://apis.juhe.cn/lottery/query'
    params = {
        'key' : akey,#我申请的key
        'lottery_id' : cpid,#彩票id
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
            ret_tuple = ('%s:' % w.get('lottery_name'),'\n',
                  '第%s期开奖结果 ' % w.get('lottery_no'),'\n',
                  '开奖日期:%s' % w.get('lottery_date'),'\n',
                  '中奖号码:  %s' % w.get('lottery_res'),'\n')
            ret_str= ''.join(ret_tuple)
            return ret_str
            
def lottery_all():
    ssq = lottery_request('ssq')
    fcsd = lottery_request('fcsd')
    plw = lottery_request('plw')
    qxc = lottery_request('qxc')
    dlt = lottery_request('dlt')
    return ssq+fcsd+plw+qxc+dlt


if __name__ == '__main__':
    main()