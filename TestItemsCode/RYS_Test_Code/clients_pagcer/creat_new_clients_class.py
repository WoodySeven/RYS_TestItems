#1/usr/bin/env python
from TestItemsCode.lib1.common_logic import *
from TestItemsCode.lib1.utils import *

class CrmAddCustomer():
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

    def input_customer_info(self):
        """添加客户的信息"""
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
        driver = self.driver
        switch_to_frame(driver)#切换iframe
        # //*[@id="mainNavbar"]/div[2]/ul/li[4]/a 客户
        tager1 = driver.find_element_by_xpath("//*[@id='mainNavbar']/div[2]/ul/li[4]/a")
        ActionChains(driver).move_to_element(tager1).click().perform()
        time.sleep(3)
        # //*[@id="menuActions"]/a 添加客户
        driver.find_element_by_xpath("//*[@id='menuActions']/a").click()
        time.sleep(3)
        # //*[@id="name"] 名称输入框
        # //*[@id="customerForm"]
        # tager3 = driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='name']")
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='name']").send_keys(name)
        time.sleep(2)
        # //*[@id="public"] 单选框"公有"
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='public']").click()
        time.sleep(2)
        # driver.find_element_by_xpath("//*[@id=\"public\"]").click()
        # //*[@id="contact"] 联系人输入框
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[2]/descendant::input[@id='contact']").send_keys(contact)
        # driver.find_element_by_xpath("//*[@id=\"contact\"]").send_keys("任永生")
        # //*[@id="phone"] 电话输入框
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[3]/descendant::input[@id='phone']").send_keys(phone)
        # driver.find_element_by_xpath("//*[@id=\"phone\"]").send_keys("15139098493")
        # //*[@id="email"] 邮箱输入框
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[4]/descendant::input[@id='email']").send_keys(list[1])
        # driver.find_element_by_xpath("//*[@id=\"email\"]").send_keys("1145254583@qq.com")
        # //*[@id="qq"] qq输入框
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[5]/descendant::input[@id='qq']").send_keys(list[0])
        # driver.find_element_by_xpath("//*[@id=\"qq\"]").send_keys("1145254583")
        # //*[@id="type"]/option[2]     类型下拉框的选择1-8
        if type > 0 and type < 9:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[6]/descendant::option[{}]".format(type)).click()
        else:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[6]/descendant::option[1]").click()
        # driver.find_element_by_xpath("//*[@id=\"type\"]/option[2]").click()
        # //*[@id="size"]/option[2] 规模下拉框的选择1-5
        if scale > 0 and scale < 6:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[7]/descendant::option[{}]".format(scale)).click()
        else:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[7]/descendant::option[1]").click()
        # //*[@id="status"]/option[1] 状态下拉框的选择1-5
        if status > 0 and status < 6:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[8]/descendant::option[{}]".format(status)).click()
        else:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[8]/descendant::option[1]").click()
        # //*[@id="level"]/option[2] 级别下拉框的选择1-6
        if level > 0 and level < 7:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[9]/descendant::option[{}]".format(level)).click()
        else:
            driver.find_element_by_xpath(
                "//div[@class='panel']/div[2]/form/table/tbody/tr[9]/descendant::option[1]").click()
        # //*[@id="intension"] 购买意向文本框的输入
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[10]/descendant::textarea[@id='intension']").send_keys(
            intension)
        time.sleep(3)
        # //*[@id="submit"] 点击保存[1] 返回[3]两按钮
        driver.find_element_by_xpath(
            "//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='保存']").click()
        # driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='返回']").click()
        time.sleep(5)
        return {"name": name, "email": list[1]}

#def accser_customers()