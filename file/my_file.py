#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 打开一个文件
fo = open("foo.txt", "wb")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
fo.close()


fo = open("foo1.txt", "rb")
data = fo.read(4)
read_utf = unicode(data,"utf-8")
print "读取的二进制字符串是 : ", data, read_utf
fo.close()

fo = open("foo.txt", "r+")
# 查找当前位置
position = fo.tell();
print "当前文件位置 : ", position

fo.write( "hello\nwww.runoob.com!\nVery good site!\n");
# 把指针再次重新定位到文件开头
position = fo.seek(0, 0);
str = fo.read(10);
print "重新读取字符串 : ", str
# 关闭打开的文件
fo.close()


# import os
# # 重命名文件test1.txt到test2.txt。
# os.rename( "test1.txt", "test2.txt" )
# # 删除一个已经存在的文件test2.txt
# os.remove("test2.txt")
# # 创建目录test
# os.mkdir("test")
# # 将当前目录改为"/home/newdir"
# os.chdir("/home/newdir")

# # 删除”/tmp/test”目录
# os.rmdir( "/tmp/test"  )