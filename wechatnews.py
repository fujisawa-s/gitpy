# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 19:44:33 2020

@author: Administrator
"""

from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
import threading
import sys
sys.path.append(r"E:/gitpy")
import newsReturn

news_switch = False    #是否开启新闻
news_open_key = '打开新闻'  #开启新闻关键字
news_close_key = '关闭新闻'    #关闭新闻关键字

logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()

#获取dict的消息内容，并且放到消息队列中
def on_message(message):
    queue_recved_message.put(message)

# 消息处理示例 仅供参考
def thread_handle_message(wx_inst):
    #死循环，一直运行
    global news_switch
    while True:
        #堵塞等待消息，有了就读出来
        msg_temp = queue_recved_message.get()
        print(msg_temp)
        if 'msg' in msg_temp.get('type'):
            # 这里是判断收到的是消息 不是别的响应
            msg_content = msg_temp.get('data', {}).get('msg', '')
            send_or_recv = msg_temp.get('data', {}).get('send_or_recv', '')
            wechar_user = msg_temp.get('data', {}).get('from_wxid','')
            if send_or_recv[0] == '0':
                                        
                #如果未开启新闻，并且收到了开启新闻关键字，则开始回复
                if msg_content == news_open_key and news_switch == False:
                    wx_inst.send_text('filehelper', 'user:{},打开新闻:{}'.format(wechar_user, msg_content))
                    wx_inst.send_text(wechar_user, '你已打开新闻阅览,请选择新闻类型(输入数字):[1]热点,[2]社会,[3]国内,[4]国际,[5]娱乐,[6]体育,[7]军事,[8]科技,[9]财经,[10]时尚')
                    news_switch = True
                #如果已经开启新闻，并且收到了关闭新闻命令，则关闭新闻   
                elif msg_content == news_close_key and news_switch == True:
                    wx_inst.send_text('filehelper', 'user:{},关闭新闻:{}'.format(wechar_user, msg_content))
                    wx_inst.send_text(wechar_user, '你已关闭新闻阅览')
                    news_switch = False
                    
               #如果已经开启新闻，那么开始选择类别
                elif msg_content == 1 and news_switch == True:
                     wx_inst.send_text(wechar_user,'%s' % newsReturn.get_type('热点'))
                     
#两个回调函数，作为数据参数，一个是收到消息后的处理
wx_inst = WechatPCAPI(on_message=on_message, log=logging)
# wx_inst = WechatPCAPI(on_message=do_nothing, log=logging)
def main():
    #创建一个wechatpcapi对象，传递的参数为函数对象，类似回调函数。
    wx_inst.start_wechat(block=True)
    
    while not wx_inst.get_myself():
        time.sleep(5)

    print('登陆成功')
    
    #得到自己的信息
    print(wx_inst.get_myself())

    #创建一个现线程来一直运行，读取消息
    threading.Thread(target=thread_handle_message, args=(wx_inst,)).start()

    time.sleep(10)
    
if __name__ == '__main__':
    main()
