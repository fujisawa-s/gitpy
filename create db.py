# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:09:31 2020

@author: Administrator
"""

import mysql.connector 

mysql_connection = mysql.connector.connect(user='root', password='sylviaZXY_710412', host='localhost')
cursor = mysql_connection.cursor()

cursor.execute("CREATE DATABASE multi_customer_locationDB")