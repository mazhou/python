#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename http.py
#chmod +x http.py
# execute: python3 http.py

import http.client, urllib.parse

conn = http.client.HTTPSConnection("qt.gtimg.cn")
conn.request("GET", "/q=sz300104")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
conn.close()

# conn = http.client.HTTPSConnection("www.baidu.com")
# conn.request("GET", "/")
# r1 = conn.getresponse()
# print(r1.status, r1.reason)
# data1 = r1.read()
# print(data1)
# conn.close()

# params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
# headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
# conn = http.client.HTTPConnection("musi-cal.mojam.com:80")
# conn.request("POST", "/cgi-bin/query", params, headers)
# response = conn.getresponse()
# print(response.status, response.reason)
# data = response.read()
# conn.close()