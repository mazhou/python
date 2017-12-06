# python
<pre>
	https://stackoverflow.com/questions/1448429/how-to-install-mysqldb-python-data-access-library-to-mysql-on-mac-os-x
</pre>

<pre>
	2017-6-13
	https://github.com/pbharrin/machinelearninginaction/blob/master/Ch02/kNN.py
</pre>

<pre>
import module1[, module2[,... moduleN]
from modname import name1[, name2[, ... nameN]]
from fib import fibonacci
	只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表
from modname import * 把一个模块的所有内容全都导入到当前的命名空间也是可行的,然而这种声明不该被过多地使用。

当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。

Python中的包
test.py
package_runoob
|-- __init__.py
|-- runoob1.py
|-- runoob2.py

package_runoob/runoob1.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def runoob1():
   print "I'm in runoob1"


package_runoob/runoob2.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def runoob2():
   print "I'm in runoob2"

package_runoob/__init__.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    print '作为主程序运行'
else:
    print 'package_runoob 初始化'


test.py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# 导入 Phone 包
from package_runoob.runoob1 import runoob1
from package_runoob.runoob2 import runoob2
 
runoob1()
runoob2()

</pre>

<pre>
sys.argv 是一个 list,包含所有的命令行参数.    
sys.stdout sys.stdin sys.stderr 分别表示标准输入输出,错误输出的文件对象.    
sys.stdin.readline() 从标准输入读一行 sys.stdout.write("a") 屏幕输出a    
sys.exit(exit_code) 退出程序    
sys.modules 是一个dictionary，表示系统中所有可用的module    
sys.platform 得到运行的操作系统环境    
sys.path 是一个list,指明所有查找module，package的路径.  

os.environ 一个dictionary 包含环境变量的映射关系   
os.environ["HOME"] 可以得到环境变量HOME的值     
os.chdir(dir) 改变当前目录 os.chdir('d:\\outlook')   
注意windows下用到转义     
os.getcwd() 得到当前目录     
os.getegid() 得到有效组id os.getgid() 得到组id     
os.getuid() 得到用户id os.geteuid() 得到有效用户id     
os.setegid os.setegid() os.seteuid() os.setuid()     
os.getgruops() 得到用户组名称列表     
os.getlogin() 得到用户登录名称     
os.getenv 得到环境变量     
os.putenv 设置环境变量     
os.umask 设置umask     
os.system(cmd) 利用系统调用，运行cmd命令   

help(obj) 在线帮助, obj可是任何类型    
callable(obj) 查看一个obj是不是可以像函数一样调用    
repr(obj) 得到obj的表示字符串，可以利用这个字符串eval重建该对象的一个拷贝    
eval_r(str) 表示合法的python表达式，返回这个表达式    
dir(obj) 查看obj的name space中可见的name    
hasattr(obj,name) 查看一个obj的name space中是否有name    
getattr(obj,name) 得到一个obj的name space中的一个name    
setattr(obj,name,value) 为一个obj的name   
space中的一个name指向vale这个object    
delattr(obj,name) 从obj的name space中删除一个name    
vars(obj) 返回一个object的name space。用dictionary表示    
locals() 返回一个局部name space,用dictionary表示    
globals() 返回一个全局name space,用dictionary表示    
type(obj) 查看一个obj的类型    
isinstance(obj,cls) 查看obj是不是cls的instance    
issubclass(subcls,supcls) 查看subcls是不是supcls的子类  

##################    类型转换  ##################

chr(i) 把一个ASCII数值,变成字符    
ord(i) 把一个字符或者unicode字符,变成ASCII数值    
oct(x) 把整数x变成八进制表示的字符串    
hex(x) 把整数x变成十六进制表示的字符串    
str(obj) 得到obj的字符串描述    
list(seq) 把一个sequence转换成一个list    
tuple(seq) 把一个sequence转换成一个tuple    
dict(),dict(list) 转换成一个dictionary    
int(x) 转换成一个integer    
long(x) 转换成一个long interger    
float(x) 转换成一个浮点数    
complex(x) 转换成复数    
max(...) 求最大值    
min(...) 求最小值  
</pre>


<pre>
echo "# python" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mazhou/python.git
git push -u origin master
</pre>

<pre>
git remote add origin https://github.com/mazhou/python.git
git push -u origin master
</pre>


<pre>
vim computationalGraph.py
chmod a+x computationalGraph.py
python computationalGraph.py
</pre>

<pre>
https://github.com/bazelbuild/bazel
https://developer.nvidia.com/cuda-downloads
https://pypi.python.org/pypi
https://virtualenv.pypa.io/en/stable/
export PATH=/Developer/NVIDIA/CUDA-8.0/bin${PATH:+:${PATH}}
export DYLD_LIBRARY_PATH=/Developer/NVIDIA/CUDA-8.0/lib\
${DYLD_LIBRARY_PATH:+:${DYLD_LIBRARY_PATH}}
</pre>

<pre>
安装tensorflow
报错说库
File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 82, in __init__
    req = Requirement(req)
安装下面修复
sudo pip install awscli --upgrade --ignore-installed six
sudo -H pip3 install tensorflow
其他参考https://www.tensorflow.org/install/install_mac
sudo easy_install pip
sudo -H 这个是mac安装权限用

</pre>

<pre>
sudo pip install virtualenv
virtualenv ENV
virtualenv --version
native
virtualenv --system-site-packages targetDirectory
cd workspace/
mkdir python
cd python
virtualenv --system-site-packages targetDirectory
virtualenv --system-site-packages -p python3 targetDirectory


virtualenv --system-site-packages targetDirectory
virtualenv --system-site-packages -p python3 targetDirectory

source /Users/mazhou/workspace/python/targetDirectory/bin/activate
source /Users/mazhou/workspace/python/targetDirectory/bin/activate.csh
csh ~/targetDirectory/bin/activate.csh

sudo -H easy_install -U pip
csh ~/targetDirectory/bin/activate.csh
  </pre>
