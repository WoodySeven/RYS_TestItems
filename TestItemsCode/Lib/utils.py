#!/usr/bin/env python
# author: samren
import shutil #主要是对文件的相关操作
import os


shutil.copyfile("HTMLTestRunner.py", "c:\HTMLTestRunner.py")

os.system("del c:\\HTMLTestRunner.py") #调用windows下的命令行cmd