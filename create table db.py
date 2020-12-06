# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:16:07 2020

@author: Administrator
"""

import mysql.connector 

mysql_connection = mysql.connector.connect(user='root', password='sylviaZXY_710412', host='localhost', database="multi_customer_locationDB")
cursor = mysql_connection.cursor()

cursor.execute("CREATE TABLE Customer (CustomerID int PRIMARY KEY, location VARCHAR(255),")