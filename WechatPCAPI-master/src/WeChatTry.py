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
import lotteryReturn

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
                    wx_inst.send_text('filehelper', 'user:{},收到消息:{}'.format(wechar_user, msg_content))
                    wx_inst.send_text(wechar_user, '你已开启彩票查询')
                    lottery_switch = True
                    if lottery_switch == True:
               #接下来返回查询结果且自动关闭
                        wx_inst.send_text(wechar_user, '%s' % lotteryReturn.lottery_all())
                        lottery_switch = False

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
    #发送给文件助手消息 "777888999"
    # wx_inst.send_text(to_user='filehelper', msg='777888999') 
    # time.sleep(1)
    # wx_inst.send_link_card(
    #     to_user='filehelper',
    #     title='博客',
    #     desc='我的博客，红领巾技术分享网站',
    #     target_url='http://www.honglingjin.online/',
    #     img_url='http://honglingjin.online/wp-content/uploads/2019/07/0-1562117907.jpeg'
    # )
    # time.sleep(1)
    #
    # wx_inst.send_img(to_user='filehelper', img_abspath=r'C:\Users\Leon\Pictures\1.jpg')
    # time.sleep(1)
    #
    # wx_inst.send_file(to_user='filehelper', file_abspath=r'C:\Users\Leon\Desktop\1.txt')
    # time.sleep(1)
    #
    # wx_inst.send_gif(to_user='filehelper', gif_abspath=r'C:\Users\Leon\Desktop\08.gif')
    # time.sleep(1)
    #
    # wx_inst.send_card(to_user='filehelper', wx_id='gh_6ced1cafca19')

    # 这个是获取群具体成员信息的，成员结果信息也从上面的回调返回
    # wx_inst.get_member_of_chatroom('22941059407@chatroom')

    # 新增@群里的某人的功能
    # wx_inst.send_text(to_user='filehelper', msg='这是PYTHON脚本发送的信息')
    # time.sleep(3)
    
    # wx_inst.send_link_card(to_user="filehelper", title="baidu url", desc="123456",
    #                        target_url="www.baidu.com", img_url="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png")
    # time.sleep(10)
    
    # wx_inst.send_img(to_user="filehelper", img_abspath="C:\\Users\\Administrator\\Desktop\\111.png")
    # time.sleep(10)
    
    # wx_inst.send_card(to_user="filehelper", wx_id="xinshe65321")
    # time.sleep(10)
    
    # wx_inst.send_file(to_user="filehelper",file_abspath="C:\\Users\\Administrator\\Desktop\\Quotes_DDT-Q20092808.pdf")
    # time.sleep(10)
    
    # get_message(message = "你是谁？")
    # time.sleep(10)
    
    # 这个是更新所有好友、群、公众号信息的，结果信息也从上面的回调返回
    # wx_inst.update_frinds()A


if __name__ == '__main__':
    main()

        
        