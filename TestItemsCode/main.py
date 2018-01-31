#!/usr/bin/env python
#author:RYS
import logging
import time
import traceback
import unittest
import HTMLTestRunner
#from RYS_Test_Code.Bugfree_Login_testcodes.BugfreeLoginOut import BugfreeLogin
#from RYS_Test_Code.ranzhi_login_testcodes.ranzhi_login_test import RanzhiLogin
#from RYS_Test_Code.ranzhi_login_testcodes.create_new_clients import CreateNewClients
#from RYS_Test_Code.ranzhi_login_testcodes.create_new_products import CreateNewProducts
from TestItemsCode.RYS_Test_Code.ranzhi_login_testcodes.create_new_clients_fenzhuang import CreateNewClient
from TestItemsCode.RYS_Test_Code.customers_dome.create_contacts import MyContactTestCase
from TestItemsCode.RYS_Test_Code.customers_dome.crate_customers import MyTestCase
#调用自写的测试用例的类
from TestItemsCode.lib1.Logger import Logger


if __name__ == "__main__":
    logger = Logger('./log/logger.log',logging.INFO) #logging 必须导入logging的类
    logging.info("本次测试开始执行，以下是详细的流程日志")
    #list1 = [CrmAddCustomer]
    #for list2 in list1:
    try:
        suite = unittest.TestSuite() #创建一个新的suite测试套件
        loader = unittest.TestLoader() #新建一个加载器，自定义的方式把测试用例加载到suite里
        #suite.addTest(loader.loadTestsFromTestCase(MyTestCase)) #把RanzhiLogin测试类里的所有的方法加载到suite里
        suite.addTest(loader.loadTestsFromTestCase(MyContactTestCase))
        fp = open('reports/RYS_report_bugfree_{0}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")),'wb') #再reports文件夹里创建并打开所创建.html文件
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = fp,
            title = 'Bugfree的测试报告',
            description = 'Bugfree的所有测试用例执行细节'
        )
        runner.run(suite)
        logging.info("测试顺利完成^_^")
    except Exception: #Exception表示只要有错误就执行以下语句
        #print_exc()函数把相关的异常输出到屏幕上，而format_exc()是将异常返回为字符串
        traceback.print_exc() #将异常以command的形式再windows的命令行显示出来；traceback必须导入tracebackde类
        logging.error(traceback.format_exc()) #将相关的程序异常以字符串的形式打印到日志文档中
        logging.error("测试出现异常并且终止程序")
    finally:
        if fp is not None: #判断fp是否以打开，如果不为空 就是fp已经被赋值 相对应的文档已经被打开，执行下列语句
            fp.close()


