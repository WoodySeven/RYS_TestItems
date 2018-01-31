#!/usr/bin/env python
from TestItemsCode.lib1.common_logic import *
from TestItemsCode.lib1.utils import *

class CrmAddContact():
    """将添加客户信息界面封装成一个类"""
    def __init__(self,driver):
        """
        可以直接调用lib1中的common_logic中封装的方法
        1.打开浏览器并并打开然之的admin登陆界面
        2.点击客户管理
        3.点击客户
        4.将界面切换到“iframe-1”
        5.点击添加客户按钮
        6.进入客户信息的输入界面，填写相关的信息并保存
        """
        self.driver = driver
        driver.get(ADMIN_PAGE) #在浏览器的链接框中输入然之的链接
        login_by_admin(driver) #admin用户登陆
        click_crm_btn(driver) #点击客户管理按钮

    def input_contact_info(self):
        """添加联系人的信息"""
        realname = get_random_customer_name()
        maker = get_random_public()
        name = get_random_string()
        gender = get_random_public()
        mobile = get_random_phone()
        phone = get_random_phone()
        list = get_random_qq_email()
        type = get_random_type()
        scale = get_random_scale_and_status()
        status = get_random_scale_and_status()
        level = get_random_level()
        intension = get_random_intension()
        fax = get_random_fax()
        rav_l = get_random_department_and_position()
        driver = self.driver
        switch_to_frame(driver)#切换iframe
        # //*[@id="mainNavbar"]/div[2]/ul/li[5]/a 联系人
        tager1 = driver.find_element_by_xpath("//*[@id=\"mainNavbar\"]/div[2]/ul/li[5]/a")
        ActionChains(driver).move_to_element(tager1).click().perform()
        time.sleep(3)
        # //*[@id="menuActions"]/a 点击添加联系人按钮
        driver.find_element_by_xpath("//*[@id='menuActions']/a").click()
        time.sleep(3)
        # //*[@id="realname"] 真实姓名
        driver.find_element_by_xpath("//div[@class='col-md-9']/descendant::input[@id='realname']").send_keys(realname)
        time.sleep(2)
        # //*[@id="maker"] 单选框"决策人"
        if maker is 1:
            driver.find_element_by_xpath("//div[@class='col-md-9']/descendant::input[@id='maker']").click()
        time.sleep(2)
        # driver.find_element_by_xpath("//*[@id=\"public\"]").click()
        # ///*[@id="customer_chosen"]/a 所属客户 新建点击
        driver.find_element_by_xpath(
            "//span[@class='input-group-addon']/label[@class='checkbox']/input[@id='newCustomer']").click()
        #所属客户
        driver.find_element_by_xpath("//div[@class='input-group']/input[@id='name']").send_keys(name)
        time.sleep(3)
        # 性别的选择
        if gender == 1:
            driver.find_element_by_xpath("//input[@id='gender1']").click()
        else:
            driver.find_element_by_xpath("//input[@id='gender2']").click()
        # 部门
        driver.find_element_by_xpath("//input[@id='dept']").send_keys(rav_l['departments'])
        # 职位
        driver.find_element_by_xpath("//input[@id='title']").send_keys(rav_l['positions'])
        # 入职时间
        driver.find_element_by_xpath("//input[@id='join']").send_keys(time.strftime("%Y-%m-%d %H-%M-%S"))
        # 邮箱
        driver.find_element_by_xpath("//input[@id='email']").send_keys(list[1])
        # 手机
        driver.find_element_by_xpath("//input[@id='mobile']").send_keys(mobile)
        # 电话
        driver.find_element_by_xpath("//input[@id='phone']").send_keys(phone)
        # 传真
        driver.find_element_by_xpath("//input[@id='fax']").send_keys(fax)
        # QQ
        driver.find_element_by_xpath("//input[@id='qq']").send_keys(list[0])
        # 类型下拉框选择1-8
        driver.find_element_by_xpath("//select[@id='type']/option[{}]".format(type)).click()
        # 规模下拉框选择1-5
        driver.find_element_by_xpath("//select[@id='status']/option[{}]".format(scale)).click()
        # 状态下拉框选择1-5
        driver.find_element_by_xpath("//select[@id='status']/option[{}]".format(status)).click()
        # 级别下拉框选择
        driver.find_element_by_xpath("//select[@id='level']/option[{}]".format(level)).click()
        # 简介文本框的输入
        driver.find_element_by_xpath("//textarea[@id='desc']").send_keys(intension)
        # 点击保存按钮
        driver.find_element_by_xpath("//input[@id='submit']").click()
        time.sleep(3)
        return {"name": name, "email": list[1]}

#def accser_customers()