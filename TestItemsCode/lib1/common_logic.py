#!/usr/bin/env python
from selenium.webdriver import ActionChains
from TestItemsCode.config import *
from TestItemsCode.lib1.utils import *
import time
from selenium import webdriver

def get_driver():
    """获取driver对象，也就是打开浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    return driver

def login_by_admin(driver):
    """管理员登陆"""
    driver.find_element_by_id("account").clear()
    driver.find_element_by_id("account").send_keys(ADMIN_ACCOUNT['account'])
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(ADMIN_ACCOUNT['password'])
    driver.find_element_by_id("submit").click()
    time.sleep(3)

def click_crm_btn(driver):
    """点击客户管理按钮"""
    #//*[@id="s-menu-1"]/button/img 客户管理
    driver.find_element_by_xpath("//*[@id=\"s-menu-1\"]/button/img").click()
    time.sleep(2)

def switch_to_frame(driver):
    #//*[@id="iframe-1"]
    #//*[@id="win-1"]
    #/html/body
    tager = driver.find_element_by_xpath("//div[@id='deskContainer']/div[@id='win-1']/div[3]/iframe")
    driver.switch_to.frame(tager)
    time.sleep(3)

def add_customer(driver):
    name = get_random_customer_name()
    public = get_random_public()
    contact = get_random_string()
    phone = get_random_phone()
    list = get_random_qq_email()
    type = get_random_type()
    scale = get_random_scale_and_status()
    status = get_random_scale_and_status()
    level = get_random_level()
    intension = get_random_intension()
    switch_to_frame(driver)
         #//*[@id="mainNavbar"]/div[2]/ul/li[4]/a 客户
    tager1 = driver.find_element_by_xpath("//*[@id='mainNavbar']/div[2]/ul/li[4]/a")
    ActionChains(driver).move_to_element(tager1).click().perform()
    time.sleep(3)
    #//*[@id="menuActions"]/a 添加客户
    driver.find_element_by_xpath("//*[@id='menuActions']/a").click()
    time.sleep(3)
    #//*[@id="name"] 名称输入框
    #//*[@id="customerForm"]
    #tager3 = driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='name']")
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='name']").send_keys(name)
    time.sleep(2)
    #//*[@id="public"] 单选框"公有"
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='public']").click()
    time.sleep(2)
    #driver.find_element_by_xpath("//*[@id=\"public\"]").click()
    #//*[@id="contact"] 联系人输入框
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[2]/descendant::input[@id='contact']").send_keys(contact)
    #driver.find_element_by_xpath("//*[@id=\"contact\"]").send_keys("任永生")
    #//*[@id="phone"] 电话输入框
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[3]/descendant::input[@id='phone']").send_keys(phone)
    #driver.find_element_by_xpath("//*[@id=\"phone\"]").send_keys("15139098493")
    #//*[@id="email"] 邮箱输入框
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[4]/descendant::input[@id='email']").send_keys(list[1])
    #driver.find_element_by_xpath("//*[@id=\"email\"]").send_keys("1145254583@qq.com")
    #//*[@id="qq"] qq输入框
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[5]/descendant::input[@id='qq']").send_keys(list[0])
    #driver.find_element_by_xpath("//*[@id=\"qq\"]").send_keys("1145254583")
    #//*[@id="type"]/option[2]     类型下拉框的选择1-8
    if type>0 and type<9:
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[6]/descendant::option[{}]".format(type)).click()
    else:
         driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[6]/descendant::option[1]").click()
    #driver.find_element_by_xpath("//*[@id=\"type\"]/option[2]").click()
    #//*[@id="size"]/option[2] 规模下拉框的选择1-5
    if  scale>0 and scale<6:
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[7]/descendant::option[{}]".format(scale)).click()
    else:
          driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[7]/descendant::option[1]").click()
    #//*[@id="status"]/option[1] 状态下拉框的选择1-5
    if status>0 and status<6:
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[8]/descendant::option[{}]".format(status)).click()
    else:
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[8]/descendant::option[1]").click()
    #//*[@id="level"]/option[2] 级别下拉框的选择1-6
    if level>0 and level<7:
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[9]/descendant::option[{}]".format(level)).click()
    else:
         driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[9]/descendant::option[1]").click()
    #//*[@id="intension"] 购买意向文本框的输入
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[10]/descendant::textarea[@id='intension']").send_keys(intension)
    time.sleep(3)
    #//*[@id="submit"] 点击保存[1] 返回[3]两按钮
    driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='保存']").click()
    #driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='返回']").click()
    time.sleep(5)
    return {"name": name,"email": list[1]}