import unittest
import time
from selenium import webdriver
import ddt #可以将将相同流程的代码通过数据驱动ddt进行参数化
import logging
import traceback
from utils import capture_screen


test_data = [['admin','123456','退出'],
             ['','','登录失败']]
@ddt.ddt
class RanzhiLogin(unittest.TestCase):
    """
    设置谷歌浏览器的打开函数
    """
    def setUp(self):
        self.driver = webdriver.Chrome()  #调用selenium中的webdriver打开谷歌浏览器
        self.driver.implicitly_wait(30)   #打开谷歌浏览器给其30s的自由等待时间，过时五任何操作关闭浏览器
        self.base_url = "http://localhost/" #将要打开的链接的头部当作为固定的参数
        logging.info("已经成功打开谷歌浏览器")
    def tearDown(self):
        """声明函数推出谷歌浏览器"""
        self.driver.quit() #调用webdriver中的quit（）函数退出谷歌浏览器
        logging.info("已将调用的谷歌浏览器关闭")
    @ddt.unpack
    @ddt.data(*test_data)
    def test_ranzhi_login_username(self,admin,password,flags):
        """对用户名的测试"""
        logging.info("test_ranzhi_login_username_test start.....")
        driver = self.driver
        driver.get(self.base_url+"ranzhi/www/sys/user-login.html") #调用webdriver中的get()函数再浏览器的地址栏输入链接
        time.sleep(3) #等待3s主要是防止加载的速率慢影响后续的操作
        driver.find_element_by_id("account").send_keys(admin) #使用webdriver中的find_element_by_id()函数定位元素，并在Input输入框内通过send_keys()函数输入admin
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("submit").click() #定位到元素点击按钮
        time.sleep(3) #如果此处不等待有可能下面的断点判读就会失败
        self.assertIn(flags,driver.page_source)#加入断言的判断
        logging.info("test datas is:{},{},{}".format(admin,password,flags))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_admin_login_test end....")

if __name__ == '__main__':
    unittest.main()
