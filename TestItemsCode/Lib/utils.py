#!/usr/bin/env python
# author: samren
import shutil #主要是对文件的相关操作
import os
import time
from selenium import webdriver

def copy_file(src,dest):
    #shutil.copyfile("HTMLTestRunner.py", "c:\HTMLTestRunner.py")#把当前的目录下的HTMLTestRunner.py拷贝到C盘下
    """拷贝文件到指定的目录下，src拷贝到dest"""
    if not os.path.exists(src):
        raise OSError  #首先判断src路径是否存在，如果不存在抛出OSError的错误。
    shutil.copy(src,dest)
    #os.system("del c:\\HTMLTestRunner.py") #调用windows下的命令行cmd

def capture_screen(driver,file_name=None):
    pic_path = "./screenshots/mypic_%s.png" % time.strftime("%Y-%m-%d %H-%M-%S") #主要注意时间戳的字符串表示方法
    if file_name is None:
        driver.get_screenshot_as_file(pic_path)
    else:
        driver.get_screenshot_as_file(file_name)
        pic_path = file_name
    if os.path.exists(pic_path):
        return pic_path

def capture_full_screen():
    """对全屏截图，朴有天python3以上版本有待查阅资料"""

    pass