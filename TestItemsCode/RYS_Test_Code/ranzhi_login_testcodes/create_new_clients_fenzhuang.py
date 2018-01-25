import unittest
import logging
import TestItemsCode.config
from TestItemsCode.lib1.common_logic import *

#@ddt.ddt
class CreateNewClient(unittest.TestCase):

    def setUp(self):
        """开始函数打开谷歌浏览器"""
        self.driver = get_driver()
        logging.info("打开谷歌浏览器")

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()
        logging.info("关闭谷歌浏览器")
    #@ddt.unpack
    #@ddt.data(*test_data)
    def test_create_new_clients(self):
        """新建客户的测试用例
        执行步骤：
        1.访问admin管理员页面，并登录
        2.点击客户管理应用
        3.添加客户信息（此处的自动添加）
        4.判断结果
        """
        logging.info("test_create_new_clients start.....")
        driver = self.driver
        driver.get(ADMIN_PAGE)
        login_by_admin(driver)
        click_crm_btn(driver)
        ret_val = add_customer(driver)
        self.assertIn(ret_val['name'],driver.page_source)
        self.assertIn('www/crm/customer-browse.html',driver.current_url)
if __name__ == '__main__':
    unittest.main()
