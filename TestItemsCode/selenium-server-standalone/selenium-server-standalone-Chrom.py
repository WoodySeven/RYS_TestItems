#!usr/bin/env python

import time
import unittest
import TestItemsCode.太阳
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestChrome(unittest.TestCase):
    def setUp(self):
        self.capabilities = {}
        self.cammand_executor = "http://192.168.1.100:5555/wd/hub"
        self.capabilities['browserName'] = 'chrome'
        self.capabilities['platform'] = 'WINDOWS'
        self.capabilities['version'] = '10'

        self.base_url = "https://www.baidu.com"
        self.driver = Remote(self.cammand_executor,desired_capabilities=self.capabilities)
        self.driver.implicitly_wait(30)
    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_open_and_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("test chrome")
        driver.find_element_by_id("su").click()
        time.sleep(5)

if __name__=="__main__":
    unittest.main()