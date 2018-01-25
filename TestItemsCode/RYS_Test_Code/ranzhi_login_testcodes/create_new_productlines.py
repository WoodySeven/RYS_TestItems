import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import ddt
import logging
from utils import capture_screen

products_data = [["name","code",1,1],
                 ["RYS-123","123",2,2],
                 ["RYS-234","234",3,3]]

@ddt.ddt
class CreateNewProducts(unittest.TestCase):

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
    @ddt.data(*products_data)
    def test_create_new_clients(self,name,code,a,b):
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
        logging.info("成功进入客户管理界面")
        #//*[@id="iframe-1"]
        #//*[@id="win-1"]
        #/html/body
        tager = driver.find_element_by_xpath("//div[@id='deskContainer']/div[@id='win-1']/div[3]/iframe")
        driver.switch_to.frame(tager)
        time.sleep(3)
        if self.assertIn("客户",driver.page_source) is True:
            logging.info("iframe层切换成功")
        else:
            logging.info("iframe层切换失败")
         #//*[@id="mainNavbar"]/div[2]/ul/li[4]/a 设置
        tager1 = driver.find_element_by_xpath("//*[@id=\"mainNavbar\"]/div[2]/ul/li[8]/a")
        ActionChains(driver).move_to_element(tager1).click().perform()
        time.sleep(3)
        #//*[@id="menuActions"]/a 添加客户
        driver.find_element_by_xpath("//*[@id='menuActions']/a").click()
        time.sleep(3)
        #//*[@id="name"] 名称输入框
        driver.find_element_by_xpath(
            "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/form/table/tbody/descendant::input[@id='name']").send_keys(name)
        #输入产品代号
        driver.find_element_by_xpath(
            "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/form/table/tbody/descendant::input[@id='code']").send_keys(
            code)
        #选择产品线
        driver.find_element_by_xpath(
            "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/form/table/tbody/descendant::select[@id='line']").click()
        #选择产品类型
        driver.find_element_by_xpath(
            "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/form/table/tbody/descendant::select[@id='type']/option[{}]".format(a)).click()
        #产品状态的选择status
        driver.find_element_by_xpath(
            "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/form/table/tbody/descendant::select[@id='status']/option[{}]".format(b)).click()
        #点击保存按钮submit
        driver.find_element_by_xpath(
            "//div[@class='modal-dialog']/div[@class='modal-content']/div[@class='modal-body']/form/table/tbody/descendant::input[@id='submit']").click()
        logging.info("产品添加结束 end.....")
        time.sleep(5)
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.info("截图不成功")
        else:
            logging.info(pic_path)



if __name__ == '__main__':
    unittest.main()
