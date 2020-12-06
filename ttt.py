# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 23:51:38 2020

@author: Administrator
"""
#调用我写的函数(在指定文件夹内) (使用记得回缩进)
    # import sys
    # sys.path.append(r"E:/gitpy")
    # import lottery
    # lottery.lottery_request()


#时间日期
    # import datetime
    # month = ('%s' % datetime.datetime.now().month)
    
    # print(type(datetime.datetime.now().year))
    # print(type(month))
    
    # import datetime

    # a = datetime.date.today()
    # dat = ('%s' % a.__format__('%Y-%m-%d'))



#utf8和中文的解码
# org_utf8_str = "\u767d\u7f8a\u5ea7"
# dst_gbk_str = ""
# org_gbk_str = '双鱼座'
# dst_utf8_str = ""
# dst_gbk_str = org_utf8_str.split('\\u')
# for item in org_gbk_str:
#     dst_utf8_str += item.encode('unicode_escape').decode('utf-8')

# print(dst_gbk_str[0])
# print(dst_utf8_str)


# #时间格式化
# import time
 
# localtime = time.localtime(time.time())
# print (type(localtime))

# import time
# ## dd/mm/yyyy格式
# print (time.strftime("%x"))

# import  datetime
# cur=datetime.datetime.now()
# cur.hour
# cur.minute
# cur.year
# cur.day
# cur.month

# #!/usr/bin/python
# import datetime
# i = datetime.datetime.now()
# print ("当前的日期和时间是 %s" % i)
# print ("ISO格式的日期和时间是 %s" % i.isoformat() )
# print ("当前的年份是 %s" %i.year)
# print ("当前的月份是 %s" %i.month)
# print ("当前的日期是  %s" %i.day)
# print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
# print ("当前小时是 %s" %i.hour)
# print ("当前分钟是 %s" %i.minute)
# print ("当前秒是  %s" %i.second)

string = "  * it is blank space test *  "
str_new = string.replace(" ", "")
print (str_new)


























