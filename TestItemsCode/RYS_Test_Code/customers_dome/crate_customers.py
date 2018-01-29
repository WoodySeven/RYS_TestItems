import unittest
import logging
from selenium import webdriver
from TestItemsCode.RYS_Test_Code.clients_pagcer.creat_new_clients_class import CrmAddCustomer
from TestItemsCode.lib1.common_logic import *


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        logging.info("打开浏览器...")

    def tearDown(self):
        self.driver.quit()
        logging.info("关闭浏览器...")
    def test_something(self):
        driver = self.driver
        page = CrmAddCustomer(driver)
        rav_l = page.input_customer_info()
        logging.info("客户信息添加完成")
        self.assertIn(rav_l['name'], driver.page_source)
        self.assertIn('www/crm/customer-browse.html', driver.current_url)


if __name__ == '__main__':
    unittest.main()
