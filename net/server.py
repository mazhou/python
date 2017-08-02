#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename server.py

import socket

s = socket.socket()
host = socket.gethostbyname('localhost') #socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)
while True:
		c, addr = s.accept()
		print 'connect url', addr
		c.send('welcome')
		c.close()