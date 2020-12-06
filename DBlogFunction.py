# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:29:28 2020

@author: Administrator
"""

import mysql.connector 

class LoggingDT:
    def __init__(self, user, password, host, database):
        self.mysql_connection = mysql.connector.connect(user=user, password=password, host=host, database=database)
        self.cursor = self.mysql_connection.cursor()
        
        
        
        
        
        
        
        
        
        
        
        
        
Logging_DT = LoggingDT('root', 'sylviaZXY_710412', 'localhost', 'multi_customer_locationDB')