# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 23:00
# @Author  : Leon
# @Email   : 1446684220@qq.com
# @File    : test.py
# @Desc    : 
# @Software: PyCharm

import threading
import function_object
import json
import urllib.request
import time
import logging
from queue import Queue
from WechatPCAPI import WechatPCAPI
from enum import Enum


#全局变量
api_key = '2a22ca3cc8e54c0790e8b26bbd382820'   #图灵机器人apiKey
user_id = '672653'    #图灵机器人账户userId
api_url = "http://openapi.tuling123.com/openapi/api/v2"    #图灵机器人post调用接口

#菜单状态变量，确认用户在哪级菜单
state_list = ("main", "robot", "ip", "lottery", "express")
class state_list(Enum):
    main = 1
    robot = 2
    ip = 3
    lottery = 4
    express = 5
    
robot_list = {
    
}
    
# main_list = {
#     "main":main_list, 
#     "robot":robot_list, 
#     "ip":main_list, 
#     "lottery":main_list, 
#     "express":main_list
# }

    
g_frist_entry_flag = True #记录是不是第一条消息
g_state = state_list.main  #默认都是进入主菜单

#原有的消息队列内容
logging.basicConfig(level=logging.INFO)
queue_recved_message = Queue()

#获取dict的消息内容，并且放到消息队列中
def on_message(message):
    queue_recved_message.put(message)
#两个回调函数，作为数据参数，一个是收到消息后的处理
wx_inst = WechatPCAPI(on_message=on_message, log=logging)

#获取图灵反馈信息函数调用，message为传入的文本信息
def get_message(message):
    #图灵机器人post json消息体
    global api_key
    global user_id
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
    #按照utf8格式对req(dict)进行json格式编码
    req = json.dumps(req).encode('utf8')
    #按照request方式进行post数据通讯
    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    #用于打开一个远程的url连接,并且向这个连接发出请求,获取响应结果
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')
    #读取字符串数据转为dict
    response_dic = json.loads(response_str)
    #读取json key分别嵌套的results values text 得到回复信息
    results_text = response_dic['results'][0]['values']['text']
    print(results_text)  
    return results_text


    
def get_tbd(user, mes):
    wx_inst.send_text(user, "目前还未支持此功能，请稍后")
    return True
    
#机器人菜单回调函数集合
def entry_robot_function(user, mes):
    global g_state
    g_state = state_list.robot
    
def exit_robot_function(user, mes):
    global g_state
    g_state = state_list.main

def custom_robot_function(user, mes):
    wx_inst.send_text(user, "欣悦是小可爱!")
    
def robot_process_function(user, mes):
    res_robot = get_message(mes)
    wx_inst.send_text(user, res_robot)
    
    
#主菜单返回字符串，主菜单对象及对象集合
main_dict = {
'0':'''【主菜单】
服务内容如下，只要回复【】内数字就可以查询相关内容
【1】机器人对话
【2】查询IP地址
【3】彩票查询
【4】快递查询
''',

'1':'''【机器人对话】
服务内容如下，随意发送数据和机器人进行对话，如果想返回主菜单，请发送数字0
''',

'2':'''【查询IP地址】
服务内容如下，查询到本地IP地址或者输入具体IP地址返回IP地址所在地，如果想返回主菜单，请发送数字0
''',

'3':'''【彩票查询】
服务内容如下，进行彩票内容查询功能，如果想返回主菜单，请发送数字0
''',

'4':'''【快递查询】
服务内容如下，输入单号查询快递，如果想返回主菜单，请发送数字0
''',
}

main_wechat_robot = function_object.Function_main("1", main_dict,entry_robot_function)
main_ip_search = function_object.Function_main("2", main_dict, get_tbd)
main_lottery_query = function_object.Function_main("3", main_dict, get_tbd)
main_express_query = function_object.Function_main("4", main_dict, get_tbd)

main_dict_class = {
    "1": main_wechat_robot, 
    "2": main_ip_search, 
    "3": main_lottery_query, 
    "4": main_express_query, 
}


#机器人二级菜单返回字符串，二级菜单对象及对象集合
secondary_robot_dict = {
'0':'''【停止机器人对话，已返回主菜单】
服务内容如下，只要回复【】内数字就可以查询相关内容
【1】机器人对话
【2】查询IP地址
【3】彩票查询
【4】快递查询
''',
}

secondary_robot_chat = function_object.Function_main("0", secondary_robot_dict,exit_robot_function)
secondary_robot_custom = function_object.Function_main("欣悦", secondary_robot_dict, custom_robot_function)

robot_dict_class = {
    "0": secondary_robot_chat, 
    "欣悦": secondary_robot_custom, 
}



# 消息处理回调函数
def thread_handle_message(wx_inst):
    #死循环，一直运行
    global tuling_switch
    global g_frist_entry_flag
    global g_state
    while True:
        #堵塞等待消息，有了就读出来
        msg_temp = queue_recved_message.get()
        print(msg_temp)
        if 'msg' in msg_temp.get('type'):
            # 这里是判断收到的是消息 不是别的响应
            msg_content = msg_temp.get('data', {}).get('msg', '')  #获取消息内容
            send_or_recv = msg_temp.get('data', {}).get('send_or_recv', '') #收还是发
            wechar_user = msg_temp.get('data', {}).get('from_wxid','') #消息是谁发的
            if send_or_recv[0] == '0':
                #如果收到消息则走以下处理
                if g_frist_entry_flag == True:  #如果是第一次进入，则发送介绍信息
                    g_frist_entry_flag = False  
                    wx_inst.send_text(wechar_user, main_dict['0']) #发送介绍信息
                else:  #如果不是第一次进入，则根据具体菜单内容进行回复
                
                    if g_state == state_list.main: #如果是在主菜单，则根据关键字遍历主菜单服务
                        temp = function_object.find_value_from_dict(msg_content, main_dict_class) #得到对象
                        if temp != None:  #如果关键字能找到结构体，代表是设置的指令
                            if temp.print_message != None: #如果对象中有要反馈的微信消息则返回
                                wx_inst.send_text(wechar_user, temp.print_message)
                                
                            temp.wx_message = msg_content
                            temp.wx_user = wechar_user
                            temp.process_call_back()
                        else:
                            wx_inst.send_text(wechar_user, main_dict['0'])
                            
                    elif g_state == state_list.robot: #如果是机器人菜单，则遍历机器人菜单
                        temp = function_object.find_value_from_dict(msg_content, robot_dict_class) #得到对象
                        if temp != None:  #如果关键字能找到结构体，代表是设置的指令
                            temp.wx_message = msg_content
                            temp.wx_user = wechar_user
                            if temp.print_message != None: #如果对象中有要反馈的微信消息则返回
                                wx_inst.send_text(wechar_user, temp.print_message)
                    
                            temp.process_call_back()   
                        else:
                            robot_process_function(wechar_user, msg_content) #如果无关键字则到图灵机器人交互

                            
                # 0是收到的消息 1是发出的 对于1不要再回复了 不然会无限循环回复
                #wx_inst.send_text('filehelper', '收到消息:{}'.format(msg_content))



# wx_inst = WechatPCAPI(on_message=do_nothing, log=logging)
def main():
    #创建一个wechatpcapi对象，传递的参数为函数对象，类似回调函数。
    wx_inst.start_wechat(block=True)
    
    while not wx_inst.get_myself():
        time.sleep(5)

    print('登陆成功')
    
    #得到自己的信息
    print(wx_inst.get_myself())
    print(type(wx_inst.get_myself()))

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

