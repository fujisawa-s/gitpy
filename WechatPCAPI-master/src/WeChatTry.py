# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 00:35:57 2020

@author: Administrator
"""

from WechatPCAPI import WechatPCAPI
import time
import logging
from queue import Queue
import threading

#全局变量
lottery_switch = False    #是否开启彩票查询
lottery_open_key = '彩票'    #开启彩票查询关键字

logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()

#获取dict的消息内容，并且放到消息队列中
def on_message(message):
    queue_recved_message.put(message)

# 消息处理示例 仅供参考
def thread_handle_message(wx_inst):
    #死循环，一直运行
    global lottery_switch
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
                #如果未开启彩票查询，并且收到了开启彩票查询关键字，则开始查询
                if msg_content == lottery_open_key and lottery_switch == False:
                    wx_inst.send_text('filehelper', 'user:{},触发机器人:{}'.format(wechar_user, msg_content))
                    wx_inst.send_text(wechar_user, '你已触发机器人进行消息反馈')
                    tuling_switch = True
                    
                #如果已经开启机器人，并且收到了关闭机器人命令，则关闭机器人    
                elif msg_content == tuling_close_key and tuling_switch == True:
                    wx_inst.send_text('filehelper', 'user:{},关闭机器人:{}'.format(wechar_user, msg_content))
                    wx_inst.send_text(wechar_user, '你已停止机器人进行消息反馈')
                    tuling_switch = False
                    
               #如果已经开启机器人，并且收到了不是控制机器人的关键字则触发图灵回复
                elif msg_content != tuling_open_key and tuling_switch == True:
                     msg_response = get_message(msg_content)
                     wx_inst.send_text(wechar_user, '机器人:{}'.format(msg_response))
                
                # 0是收到的消息 1是发出的 对于1不要再回复了 不然会无限循环回复
                #wx_inst.send_text('filehelper', '收到消息:{}'.format(msg_content))
        
        