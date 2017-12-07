# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from pageobject.account.Page_Account_GS_ADD import Page_Account_GS_ADD
from utils.config import Config
from utils.log1 import Log
from selenium.common.exceptions import NoSuchElementException

log = Log()

@ddt.ddt
class loginout(unittest.TestCase):
    u'''登出'''
    def test03_loginout(self):
        '''退出'''
        # self.A.LoginOut()
        self.driver = webdriver.Firefox()
        self.driver.find_element_by_id("loginOut").click()
        self.assertTrue(self.driver.current_url == "http://47.52.77.154:8015/Default/Login", "-------管理员退出失败-------")
        # log.info("-------管理员退出  用例结束-------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)