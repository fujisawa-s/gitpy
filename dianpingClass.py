# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:25:26 2020

@author: Administrator
"""
# import requests
# from bs4 import BeautifulSoup


# class dianping:
    
#     def __init__(self):
#         self.URL = 'https://movie.douban.com/chart'
#         self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
        
#     def get_15(self):
#         html = requests.get(self.URL)
#         soup = BeautifulSoup(html.content, 'html.parser', from_encoding='utf-8')
#         print(soup)
        
# if __name__ =='__main__':
#     cls = dianping()
#     cls.get_15()

from selenium import webdriver

# 创建 WebDriver 实例对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome()

# WebDriver 实例对象的get方法 可以让浏览器打开指定网址
wd.get('http://www.dianping.com/shanghai/ch20/g119r3o2')

# 根据 class name 选择元素，返回的是 一个列表
element = wd.find_element_by_class_name('J-bonus-close')
element.click()

elements = wd.find_elements_by_tag_name('h4')

# 取出列表中的每个 WebElement对象，打印出其text属性的值
# text属性就是该 WebElement对象对应的元素在网页中的文本内容
for element in elements:
    print(element.text)
pass














