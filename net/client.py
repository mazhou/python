#!/usr/bin/python
# -*- coding: UTF-8 -*-
# filename server.py

import socket

s = socket.socket()
host = socket.gethostbyname('localhost')	#socket.gethostname()
port = 12345

s.connect((host,port))
print s.recv(1024)
s.close()


