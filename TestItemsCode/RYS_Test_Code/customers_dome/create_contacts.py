import unittest
import logging
from selenium import webdriver
from TestItemsCode.RYS_Test_Code.clients_pagcer.create_new_contacts_class import CrmAddContact
from TestItemsCode.lib1.common_logic import *


class MyContactTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = get_driver()
        logging.info("打开浏览器...")

    def tearDown(self):
        self.driver.quit()
        logging.info("关闭浏览器...")
    def test_something(self):
        driver = self.driver
        page = CrmAddContact(driver)
        rav_l = page.input_contact_info()
        logging.info("客户信息添加完成")
        self.assertIn(rav_l['name'], driver.page_source)
        self.assertIn('www/crm/contact', driver.current_url)