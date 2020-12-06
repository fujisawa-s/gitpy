#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

def main():
    # 配置APPKey
    appkey = "54735190aa66a24335b98a38ca1c6062"
 
    # 根据城市查询天气
    request1(appkey)
 
 
# 根据城市查询天气
def request1(appkey):
    url = "http://apis.juhe.cn/simpleWeather/query"
    params = {
        "city": "上海",  # 要查询的城市，如：温州、上海、北京
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": "json",  # 返回数据的格式,xml或json，默认json
        "format": 1
    }
 
    f = requests.get(url=url, params=params)
    res = f.json()
 
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            w = res["result"]
            print('上海当前天气状况:')
            now = w.get('realtime')
            print ("气温:%s℃" %  now.get('temperature'),','
                   "气象:%s" %  now.get('info'),','
                   "湿度:%s" %  now.get('humidity'),','
                   "风速:%s"%  now.get('direct'),"%s" % now.get('power'),'\n')
            print('上海未来天气预报:')
            future = w.get('future')
            today = future[0]
            print("今天 %s" % today.get('date'),'\n'
                  "气温区间:%s" % today.get('temperature'),','
                  "气象预测:%s" % today.get('weather'),','
                  "风向:%s" % today.get('direct'))
            tomo = future[1]
            print("明天 %s" % tomo.get('date'),'\n'
                  "气温区间:%s" % tomo.get('temperature'),','
                  "气象预测:%s" % tomo.get('weather'),','
                  "风向:%s" % tomo.get('direct'))
            after = future[2]
            print("后天 %s" % after.get('date'),'\n'
                  "气温区间:%s" % after.get('temperature'),','
                  "气象预测:%s" % after.get('weather'),','
                  "风向:%s" % after.get('direct'))
            four = future[3]
            print("%s" % four.get('date'),'\n'
                  "气温区间:%s" % four.get('temperature'),','
                  "气象预测:%s" % four.get('weather'),','
                  "风向:%s" % four.get('direct'))
            five = future[4]
            print("%s" % five.get('date'),'\n'
                  "气温区间:%s" % five.get('temperature'),','
                  "气象预测:%s" % five.get('weather'),','
                  "风向:%s" % five.get('direct'))
        else:
            print("%s:%s" % (res["error_code"], res["reason"]))
    else:
        print("request api error")
 
 
if __name__ == '__main__':
    main()

