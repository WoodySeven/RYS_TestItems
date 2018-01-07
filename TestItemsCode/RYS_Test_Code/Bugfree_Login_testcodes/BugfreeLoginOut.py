import unittest
import time
from selenium import webdriver
import ddt

test_data = [['admin','123456','退出'],
             ['invalid','123456','用户名不存在'],
             ['','123456','不可为空白']]


@ddt.ddt
class BugfreeLogin(unittest.TestCase):
    """
    创建一个Bugfree登录的类
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.2.87"
        driver = self.driver
        """
        设置一个启动谷歌浏览器的方法
        """
    def tearDown(self):
        pass
    """
    设置一个关闭谷歌浏览器的方法
    """
    @ddt.unpack
    @ddt.data(*test_data)
    def test_Bugfreelogin(self,admmin,password,flag):
        """
        对Bugfree登录界面的用户名及密码和登录按钮的测试用例
        """
        driver = self.driver
        driver.get(self.base_url+"/bugfree/index.php/site/login")
        time.sleep(3)
        driver.find_element_by_id("LoginForm_username").send_keys(admmin)
        driver.find_element_by_id("LoginForm_password").send_keys(password)
        driver.find_element_by_id("SubmitLoginBTN").click()
        self.assertIn(flag,driver.page_source)


if __name__ == '__main__':
    unittest.main()
