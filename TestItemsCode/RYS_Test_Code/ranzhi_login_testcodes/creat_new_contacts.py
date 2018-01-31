import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import ddt
import logging
from utils import capture_screen

test_data = [["星巴克",1,"Tim","123578990","3432423@ty.com","34354543",2,3,4,5,"希望下次合作"],
             ["金磨坊",0,"Jack","786543567","6756788@ty.com","567567546",7,4,5,2,"无合作的倾向"]]

@ddt.ddt
class CreateNewContacts(unittest.TestCase):

    def setUp(self):
        """开始函数打开谷歌浏览器"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        logging.info("打开谷歌浏览器")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭谷歌浏览器")
    @ddt.unpack
    @ddt.data(*test_data)
    def test_create_new_clients(self,name,public,contact,gender,email,qq,type,scale,status,level,intension):
        logging.info("test_create_new_clients start.....")
        driver = self.driver
        driver.get(self.base_url+"ranzhi/www/sys/user-login.html")
        time.sleep(3)
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        if self.assertIn("所有应用",driver.page_source) is True:
            logging.info("admin用户登陆成功...")
        else:
            logging.info("admin用户登陆失败")
        #//*[@id="s-menu-1"]/button/img 客户管理
        driver.find_element_by_xpath("//*[@id=\"s-menu-1\"]/button/img").click()
        time.sleep(2)
        #//*[@id="iframe-1"]
        #//*[@id="win-1"]
        #/html/body
        #tager = driver.find_element_by_xpath("//div[@id='deskContainer']/div[@id='win-1']/div[3]/iframe")
        driver.switch_to.frame("iframe-1")
        time.sleep(3)
        if self.assertIn("客户",driver.page_source) is True:
            logging.info("iframe层切换成功")
        else:
            logging.info("iframe层切换失败")
         #//*[@id="mainNavbar"]/div[2]/ul/li[5]/a 联系人
        tager1 = driver.find_element_by_xpath("//*[@id=\"mainNavbar\"]/div[2]/ul/li[5]/a")
        ActionChains(driver).move_to_element(tager1).click().perform()
        time.sleep(3)
        #//*[@id="menuActions"]/a 点击添加联系人按钮
        driver.find_element_by_xpath("//*[@id='menuActions']/a").click()
        time.sleep(3)
        #//*[@id="realname"] 真实姓名
        driver.find_element_by_xpath("//div[@class='col-md-9']/descendant::input[@id='realname']").send_keys(name)
        time.sleep(2)
        #//*[@id="maker"] 单选框"决策人"
        if public is 1:
            driver.find_element_by_xpath("//div[@class='col-md-9']/descendant::input[@id='maker']").click()
        else:
              logging.info("公有单选框的值为{}表示为未选中".format(public))
        time.sleep(2)
        #driver.find_element_by_xpath("//*[@id=\"public\"]").click()
        #///*[@id="customer_chosen"]/a 所属客户 新建点击
        driver.find_element_by_xpath(
            "//span[@class='input-group-addon']/label[@class='checkbox']/input[@id='newCustomer']").click()
        driver.find_element_by_xpath("//div[@class='input-group']/input[@id='name']").send_keys(contact)
        time.sleep(5)
        #性别的选择
        if gender == 1:
            driver.find_element_by_xpath("//input[@id='gender1']").click()
        else:
            driver.find_element_by_xpath("//input[@id='gender2']").click()
        #部门
        driver.find_element_by_xpath("//input[@id='dept']").send_keys()
        #职位
        driver.find_element_by_xpath("//input[@id='title']").send_keys()
        #入职时间
        driver.find_element_by_xpath("//input[@id='join']").send_keys()
        #邮箱
        driver.find_element_by_xpath("//input[@id='email']").send_keys()
        #手机
        driver.find_element_by_xpath("//input[@id='mobile']").send_keys()
        #电话
        driver.find_element_by_xpath("//input[@id='phone']").send_keys()
        #传真
        driver.find_element_by_xpath("//input[@id='fax']").send_keys()
        #QQ
        driver.find_element_by_xpath("//input[@id='qq']").send_keys()
        #类型下拉框选择1-8
        driver.find_element_by_xpath("//select[@id='type']/option['国有企业']").click()
        #规模下拉框选择1-5
        driver.find_element_by_xpath("//select[@id='status']/option[2]").click()
        #状态下拉框选择1-5
        driver.find_element_by_xpath("//select[@id='status']/option[2]").click()
        #级别下拉框选择
        driver.find_element_by_xpath("//select[@id='level']/option[2]").click()
        #简介文本框的输入
        driver.find_element_by_xpath("//textarea[@id='desc']").send_keys("yigukl")
        #点击保存按钮
        driver.find_element_by_xpath("//input[@id='submit']").click()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
