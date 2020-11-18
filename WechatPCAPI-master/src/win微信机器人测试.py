# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 23:00
# @Author  : Leon
# @Email   : 1446684220@qq.com
# @File    : test.py
# @Desc    : 
# @Software: PyCharm

import threading
import json
import urllib.request
import time
import logging
from queue import Queue
from WechatPCAPI import WechatPCAPI


#全局变量
api_key = '2a22ca3cc8e54c0790e8b26bbd382820'   #图灵机器人apiKey
user_id = '672653'    #图灵机器人账户userId
api_url = "http://openapi.tuling123.com/openapi/api/v2"    #图灵机器人post调用接口
tuling_switch = False    #是否开启图灵机器人回复
tuling_open_key = '呼叫机器人'    #开启机器人口令
tuling_close_key = '关闭机器人'    #开启机器人口令

logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()

#获取图灵反馈信息函数调用，message为传入的文本信息
def get_message(message):
    #图灵机器人post json消息体
    req = {
    "reqType":0,
    "perception":
        {
            "inputText":
            {
                "text": message
            },
        },
    "userInfo": 
        {
            "apiKey": api_key,
            "userId": user_id
        }
    }
    #按照utf8格式对req进行json格式编码
    req = json.dumps(req).encode('utf8')
    #按照request方式进行post数据通讯
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    #用于打开一个远程的url连接,并且向这个连接发出请求,获取响应结果
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    #读取数据转为dict
    response_dic = json.loads(response_str)
    #读取json key分别嵌套的results values text 得到回复信息
    results_text = response_dic['results'][0]['values']['text']
    print(results_text)  
    return results_text


#获取dict的消息内容，并且放到消息队列中
def on_message(message):
    queue_recved_message.put(message)

# 消息处理回调函数
def thread_handle_message(wx_inst):
    #死循环，一直运行
    global tuling_switch
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
                #如果未开启机器人，并且收到了开启机器人命令，则开启机器人
                if msg_content == tuling_open_key and tuling_switch == False:
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
    wx_inst.send_text(to_user='filehelper', msg='这是PYTHON脚本发送的信息')
    time.sleep(3)
    
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
