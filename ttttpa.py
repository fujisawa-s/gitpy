# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 20:36:04 2020

@author: Administrator
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

#声明谷歌、Firefox、Safari等浏览器
browser=webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")#链接
    input=browser.find_element_by_id("kw")#选定要操作的元素
    input.send_keys("Python")#对元素进行操作,这里是发送字符串到输入框
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
    time.sleep(10)
finally:
    browser.close()
    
