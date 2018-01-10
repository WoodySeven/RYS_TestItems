import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # //*[@id="menuActions"]/a 创建订单
        #driver.find_element_by_xpath("//*[@id=\"menuActions\"]/a").click()
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
