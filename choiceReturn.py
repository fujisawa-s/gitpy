# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:41:25 2020

@author: Administrator
"""
import random

def main():
    print(style_cooking())#一共有45种菜品类型,如对结果不满意,可发送【1】重新获取
    print(district_shanghai())
    print(answer_book())


def style_cooking():
    alwaysHttp = 'http://www.dianping.com/shanghai/ch10/'
    style = (random.choice(['本帮江浙菜\n%sg101'%alwaysHttp,
                          '日本菜\n%sg113'%alwaysHttp, 
                          '小吃快餐\n%sg112'%alwaysHttp,
                          '面包甜点\n%sg117'%alwaysHttp,
                          '火锅\n%sg110'%alwaysHttp,
                          '西餐\n%sg116'%alwaysHttp,
                          '自助餐\n%sg111'%alwaysHttp,
                          '粤菜\n%sg103'%alwaysHttp,
                          '韩国料理\n%sg114'%alwaysHttp,
                          '川菜\n%sg102'%alwaysHttp,
                          '其他美食\n%sg118'%alwaysHttp,
                          '咖啡厅\n%sg132'%alwaysHttp,
                          '小龙虾\n%sg219'%alwaysHttp,
                          '烧烤烤串\n%sg508'%alwaysHttp,
                          '东南亚菜\n%sg115'%alwaysHttp,
                          '饮品店\n%sg34236'%alwaysHttp,
                          '下午茶\n%sg34014'%alwaysHttp,
                          '面馆\n%sg215'%alwaysHttp,
                          '江河湖海鲜\n%sg251'%alwaysHttp,
                          '东北菜\n%sg106'%alwaysHttp,
                          '新疆菜\n%sg3243'%alwaysHttp,
                          '素食\n%sg109'%alwaysHttp,
                          '湘菜\n%sg104'%alwaysHttp,
                          '早茶\n%sg34055'%alwaysHttp,
                          '北京菜\n%sg311'%alwaysHttp,
                          '农家菜\n%sg25474'%alwaysHttp,
                          '水果生鲜\n%sg2714'%alwaysHttp,
                          '家常菜\n%sg1783'%alwaysHttp,
                          '烤肉\n%sg34303'%alwaysHttp,
                          '特色菜\n%sg34284'%alwaysHttp,
                          '私房菜\n%sg1338'%alwaysHttp,
                          '创意菜\n%sg250'%alwaysHttp,
                          '中东菜\n%sg234'%alwaysHttp,
                          '非洲菜\n%sg2797'%alwaysHttp,
                          '台湾菜\n%sg107'%alwaysHttp,
                          '福建菜\n%sg34059'%alwaysHttp,
                          '江西菜\n%sg247'%alwaysHttp,
                          '徽菜\n%sg26482'%alwaysHttp,
                          '西北民间菜\n%sg34235'%alwaysHttp,
                          '鲁菜\n%sg26483'%alwaysHttp,
                          '贵州菜|黔菜\n%sg105'%alwaysHttp,
                          '云南菜|滇菜\n%sg248'%alwaysHttp,
                          '陕菜\n%sg34234'%alwaysHttp,
                          '湖北菜\n%sg246'%alwaysHttp,
                          '山西菜\n%sg26484'%alwaysHttp,
                          '内蒙菜\n%sg1453'%alwaysHttp,]))
    return(style)

def district_shanghai():
    AH = '热门商户参考:http://www.dianping.com/shanghai/ch20/'
    district = (random.choice(['静安区\n%sg119r3o2'%AH,
                               '长宁区\n%sg119r4o2'%AH,
                               '徐汇区\n%sg119r2o2'%AH,
                               '杨浦区\n%sg119r10o2'%AH,
                               '黄浦区\n%sg119r6o2'%AH,
                               '虹口区\n%sg119r9o2'%AH,
                               '普陀区\n%sg119r7o2'%AH,
                               '闵行区\n%sg119r12o2'%AH,
                               '宝山区\n%sg119r13o2'%AH,
                               '浦东新区\n%sg119r5o2'%AH,
                               '松江区\n%sg119r5937o2'%AH,
                               '嘉定区\n%sg119r5938o2'%AH,
                               '青浦区\n%sg119r5939o2'%AH,
                               '金山区\n%sg119r8847o2'%AH,
                               '奉贤区\n%sg119r8846o2'%AH,
                               '崇明区\n%sg119o2c3580'%AH,
                               ]))
    return(district) 

def answer_book():
    number=str((random.randint(7, 324)))
    photo_number=number.zfill(3)
    photo_location=('E:\\gitpy\\answer\\answer-%s.jpg'%photo_number)
    return(photo_location)                          
                                 
                                 
                                 
    #wx_inst.send_img(to_user='filehelper', img_abspath=r'C:\Users\Leon\Pictures\1.jpg')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()