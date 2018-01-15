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
    @ddt.data(*test_data)
    def test_create_new_clients(self,name,public,contact,phone,email,qq,type,scale,status,level,intension):
        logging.info("test_create_new_clients start.....")
        driver = self.driver
        driver.get(self.base_url+"ranzhi/www/sys/user-login.html")
        time.sleep(3)
        driver.find_element_by_id("account").send_keys("admin")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("submit").click()
        time.sleep(3)
        a = "退出"
        if a in driver.page_source:
            logging("然之协调登陆成功...")
        else:
            logging("然之协调登陆失败...")
       #//*[@id="s-menu-1"]/button/img 客户管理
        driver.find_element_by_xpath("//*[@id=\"s-menu-1\"]/button/img").click()
        time.sleep(2)
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
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='name']").send_keys(name)
        time.sleep(2)
        #//*[@id="public"] 单选框"公有"
        if public is 1:
            driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[1]/descendant::input[@id='public']").click()
        else:
              logging.info("公有单选框的值为{}表示为未选中".format(public))
        time.sleep(2)
        #driver.find_element_by_xpath("//*[@id=\"public\"]").click()
        #//*[@id="contact"] 联系人输入框
        if contact is not None:
            driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[2]/descendant::input[@id='contact']").send_keys(contact)
        else:
            contact = input("联系人为必选项不能为空，请输入{}的联系人".format(name))
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
        if type>0 and type<9:
            driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[6]/descendant::option[{}]".format(type)).click()
        else:
             driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[6]/descendant::option[1]").click()
        #driver.find_element_by_xpath("//*[@id=\"type\"]/option[2]").click()
        #//*[@id="size"]/option[2] 规模下拉框的选择1-5
        if  scale>0 and scale<6:
            driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[7]/descendant::option[{}]".format(scale)).click()
        else:
              driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[7]/descendant::option[1]").click()
        #//*[@id="status"]/option[1] 状态下拉框的选择1-5
        if status>0 and status<6:
            driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[8]/descendant::option[{}]".format(status)).click()
        else:
            driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[8]/descendant::option[1]").click()
        #//*[@id="level"]/option[2] 级别下拉框的选择1-6
        if level>0 and level<7:
            driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[9]/descendant::option[{}]".format(level)).click()
        else:
             driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[9]/descendant::option[1]").click()
        #//*[@id="intension"] 购买意向文本框的输入
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[10]/descendant::textarea[@id='intension']").send_keys("很强的购买倾向")
        time.sleep(3)
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.info("截图不成功")
        else:
            logging.info(pic_path)
        #//*[@id="submit"] 点击保存[1] 返回[3]两按钮
        driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='保存']").click()
        #driver.find_element_by_xpath("//div[@class='panel']/div[2]/form/table/tbody/tr[11]/descendant::input[@value='返回']").click()
        logging.info("客户添加结束 end.....")
        time.sleep(5)
        #self.assertIn(name,driver.page_source)

if __name__ == '__main__':
    unittest.main()
