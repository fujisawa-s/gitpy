# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 23:43:34 2020

@author: Administrator
"""

from selenium import webdriver
import time

url = 'https://www.douban.com'
browser = webdriver.Chrome()
browser.get(url)

browser.implicitly_wait(10)

# 重点1要先切换到子框架
browser.switch_to.frame(browser.find_elements_by_tag_name('iframe')[0])

# 重点2要先点击用账号密码登录的按钮，不然会找不到输入账号和密码的地方
bottom1 = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
bottom1.click()
time.sleep(2)

input1 = browser.find_element_by_id('username')
input1.clear()
input1.send_keys('18616802280')
time.sleep(1)

input2 = browser.find_element_by_id('password')
input2.clear()
input2.send_keys('asdf123456')
time.sleep(5)

# 手动输入验证码。。这个后面再弄

bottom = browser.find_element_by_class_name('account-form-field-submit ')
bottom.click()
time.sleep(3)

input3 = browser.find_element_by_id('inp-query')
input3.clear()
input3.send_keys('霸王别姬\n')
time.sleep(3)

element = browser.find_element_by_class_name('content')
bottom2 = element.find_element_by_tag_name('a')
bottom2.click()
time.sleep(2)


handles = browser.window_handles
browser.switch_to.window(handles[-1])
element = browser.find_element_by_id('link-report')
element2 = element.find_element_by_tag_name('span')
print(element2.text)

pass

