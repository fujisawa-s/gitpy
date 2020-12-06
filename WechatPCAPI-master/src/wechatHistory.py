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
import sys
sys.path.append(r"E:/gitpy")
import choiceReturn

#全局变量
history_switch = False    #是否开启历史上的今天查询
history_open_key = '历史'    #开启历史上的今天查询关键字


logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()

#获取dict的消息内容，并且放到消息队列中
def on_message(message):
    queue_recved_message.put(message)

# 消息处理示例 仅供参考
def thread_handle_message(wx_inst):
    #死循环，一直运行
    global history_switch
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
                
                #如果未开启历史上的今天查询，并且收到了开启历史上的今天查询关键字，则开始查询
                if msg_content == history_open_key and history_switch == False:
                    wx_inst.send_text('filehelper', 'user:{},收到消息:{}'.format(wechar_user, msg_content))
                    wx_inst.send_text(wechar_user, '历史上的今天发生了...')
                    history_switch = True
                    if history_switch == True:
               #接下来返回查询结果且自动关闭
                        wx_inst.send_img(wechar_user, '%s' % choiceReturn.answer_book())
                        wx_inst.send_text(wechar_user, '重新输入[历史]可获取新内容')
                        history_switch = False

                # 0是收到的消息 1是发出的 对于1不要再回复了 不然会无限循环回复
                #wx_inst.send_text('filehelper', '收到消息:{}'.format(msg_content))
        
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

        
        