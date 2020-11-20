# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 11:26:33 2020

@author: hema
"""


def find_value_from_dict(key, table):
    '''通过关键字key返回dict中的value字符串数据

    如果创建了一个dict的字典，你需要从dict字典中，通过key返回value字符串，则可以用此函数
    进行查找，如果查找到，则返回字符串信息，如果没查到，则返回 None

    :param key(str): 关键字key
    :param table(dict): 要遍历哪个dict返回相应的字符串
    :returns(str): 关键字对应的字符串数据
    '''
    for x in table:
        if x == key:
            #print(table[x])
            return (table[x])
    return None

    

class Function_main(object):
    '''通过创建类对象来映射每个实际的功能，其中包含了要输入的参数以及关键字还有要运行的回调函数

    详细描述

    Attributes:
    :param key(str): 关键字key
    :param table(dict): 要遍历哪个dict返回相应的字符串
    :param func(def): 回调函数
    :returns(str): 关键字对应的字符串数据
    '''
    def __init__(self, key, table, func = None):
        
        self.key_words = key  #回调函数和输出字符的关键字
        self.print_message = find_value_from_dict(key, table)  #返回要微信返回的信息内容
        self.wx_message = None
        self.wx_user = None
        self.func = func
    
#回调函数方法，如果此对象有回调函数则进行运行
    def process_call_back(self):
        if self.func != None:
            return self.func(self.wx_user, self.wx_message)



def main():
    pass
# =============================================================================
#     a = Function_main("1", main_dict, find_value_from_dict)
#     b = Function_main("2", main_dict, find_value_from_dict)
#     c = Function_main("3", main_dict, find_value_from_dict)
#     d = Function_main("4", main_dict, find_value_from_dict)
#     print(a.message_call_back())
#     print(b.message_call_back())
#     print(c.message_call_back())
#     print(d.message_call_back())
# =============================================================================

if __name__ == '__main__':
    main()
