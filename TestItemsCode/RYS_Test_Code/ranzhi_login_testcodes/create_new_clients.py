import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class CreateNewProducts(unittest.TestCase):

    def setUp(self):
        """开始函数打开谷歌浏览器"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"

    def tearDown(self):
        """关闭谷歌浏览器"""
        self.driver.quit()

    def test_create_new_clients(self):
        driver = self.driver
        driver.get(self.base_url+"ranzhi/www/sys/user-login.html")
        time.sleep(3)
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        #//*[@id="s-menu-1"]/button/img 客户管理
        driver.find_element_by_xpath("//*[@id=\"s-menu-1\"]/button/img").click()
        time.sleep(2)
        #//*[@id="iframe-1"]
        #//*[@id="win-1"]
        #/html/body
        tager = driver.find_element_by_xpath("//div[@id='deskContainer']/div[@id='win-1']/div[3]/iframe")
        driver.switch_to.frame(tager)
        time.sleep(3)
         #//*[@id="mainNavbar"]/div[2]/ul/li[4]/a 客户
        tager1 = driver.find_element_by_xpath("//*[@id=\"mainNavbar\"]/div[2]/ul/li[4]/a")
        ActionChains(driver).move_to_element(tager1).click().perform()
        time.sleep(3)
        #//*[@id="menuActions"]/a 添加客户
        driver.find_element_by_xpath("//*[@id='menuActions']/a").click()
        time.sleep(3)
        #//*[@id="name"] 名称输入框
        #//*[@id="customerForm"]
        #tager3 = driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='name']")
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='name']").send_keys("有限公司")
        time.sleep(2)
        #//*[@id="public"] 单选框"公有"
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='public']").click()
        time.sleep(2)
        #driver.find_element_by_xpath("//*[@id=\"public\"]").click()
        #//*[@id="contact"] 联系人输入框
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[2]/descendant::input[@id='contact']").send_keys("任永生")
        #driver.find_element_by_xpath("//*[@id=\"contact\"]").send_keys("任永生")
        #//*[@id="phone"] 电话输入框
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[3]/descendant::input[@id='phone']").send_keys("15139098493")
        #driver.find_element_by_xpath("//*[@id=\"phone\"]").send_keys("15139098493")
        #//*[@id="email"] 邮箱输入框
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[4]/descendant::input[@id='email']").send_keys(r"1145254583@qq.com") 
        #driver.find_element_by_xpath("//*[@id=\"email\"]").send_keys("1145254583@qq.com")
        #//*[@id="qq"] qq输入框
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[5]/descendant::input[@id='qq']").send_keys(r"1145254583@qq.com")
        #driver.find_element_by_xpath("//*[@id=\"qq\"]").send_keys("1145254583")
        #//*[@id="type"]/option[2]     类型下拉框的选择1-8
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[6]/descendant::option[2]").click()
        #driver.find_element_by_xpath("//*[@id=\"type\"]/option[2]").click()
        #//*[@id="size"]/option[2] 规模下拉框的选择1-4
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[7]/descendant::option[2]").click()
        #//*[@id="status"]/option[1] 状态下拉框的选择1-5
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[8]/descendant::option[1]").click()
        #//*[@id="level"]/option[2] 级别下拉框的选择1-6
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[9]/descendant::option[2]").click()
        #//*[@id="intension"] 购买意向文本框的输入
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[10]/descendant::textarea[@id='intension']").send_keys("很强的购买倾向")
        #//*[@id="submit"] 点击保存[1] 返回[3]两按钮
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='保存']").click()
        #driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='返回']").click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()
