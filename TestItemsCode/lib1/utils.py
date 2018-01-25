#!/usr/bin/env python
# author: samren
import shutil #主要是对文件的相关操作
import os
import time
import random
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

"""
下列函数主要是为创建客户的相关参数，自动化
"""
def get_random_customer_name():
    """生成随机的客户名称，并返回"""
    name = "customer_{}".format(random.randint(1000,9999))
    #print(name)
    return name

def get_random_public():
    """生产一个随机数只有0或者1的随机数，用于单选框是否勾选"""
    #print(random.randint(0,1))
    return random.randint(0,1)

def get_random_string(i=8):
    """生产随机的字符串，并返回"""
    population = 'ABCDEFGHIJKLMNPOQRSTUVWXYZabcdefghjklqwertyuiomnbvcxz0123456789'
    rand_list = random.choices(population,k=i) #从population字符串中随机取i个字符，组成一个列表
    #print(rand_list)
    #str1 = ''.join(rand_list)
    #print(str1)
    return ''.join(rand_list) #将rand_list列表中的所有字符组成一个字符串，并返回

def get_random_phone():
    """生产随机的手机号码，并返回 手机号格式13 15 17 18开头的号码"""
    phone_prefix = random.choice([13, 15, 17, 18])
    population = '0123456789'
    phone_suffix = ''.join(random.choices(population,k=9))
    #print("{}{}".format(phone_prefix,phone_suffix))
    return "{}{}".format(phone_prefix,phone_suffix)

def get_random_qq_email():
    """用于生产一个随机的qq号，qq号有5，6，7，8，9，10，11位"""
    list1 = []
    qq_digits = random.randint(5,11)
    #print(qq_digits)
    qq_profix = random.choice([1,2,3,4,5,6,7,8,9])
    population = '0123456789'
    qq_suffix = ''.join(random.choices(population,k=qq_digits-1))
    #print("{}{}".format(qq_profix,qq_suffix))
    email_suffix = '@qq.com'
    qq = "{}{}".format(qq_profix,qq_suffix)
    list1.append(qq)
    email = "{}{}{}".format(qq_profix,qq_suffix,email_suffix)
    list1.append(email)
    #print(list1)
    return list1

#def get_random_email():
    #"""生产一个随机的邮箱，格式位 QQ号@qq.com"""
    #email_profix = get_random_qq()
    #email_suffix = '@qq.com'
    #print("{}{}".format(email_profix,email_suffix))
    #return "{}{}".format(email_profix,email_profix)

def get_random_type():
    """随机生成类型的下拉框选择随机数1-8"""
    return random.randint(1,8)

def get_random_scale_and_status():
    """随机生产规模与状态的下拉框选择随机数1-5"""
    return random.randint(1,5)

def get_random_level():
    """随机生产级别下拉框的随机数1-6"""
    return random.randint(1,6)
def get_random_intension():
    """随机生成一个简单的购买意向表达，购买意向强烈 购买意向一般  希望再次进一步详细了解 无购买意向"""
    population = ["购买意向强烈","购买意向一般","希望再次进一步详细了解","无购买意向"]
    #print(random.choice(population))
    return random.choice(population)

if __name__=="__main__":
    get_random_customer_name()
    get_random_public()
    get_random_string()
    get_random_phone()
    get_random_qq_email()
    get_random_type()
    get_random_scale_and_status()
    get_random_level()
    get_random_intension()