#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gmtime, strftime
print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
#import time

# 格式化成2016-03-20 11:45:39形式
#print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
#print datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")

# 格式化成Sat Mar 28 22:24:24 2016形式
#print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
#a = "Sat Mar 28 22:24:24 2016"
#print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))