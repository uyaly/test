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
class login(unittest.TestCase):
    u'''登录'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.A = Page_Account(self.driver)
        self.A_GS_ADD = Page_Account_GS_ADD(self.driver)
        self.l.open(self.url)
        # 浏览器最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test01_login(self):
        '''管理员登录'''
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        time.sleep(10)
        # print self.driver.current_url
        self.assertTrue(self.driver.current_url == "http://47.52.77.154:8015/Default/Index", "-------管理员登录失败-------")
        # log.info('-------管理员登录    用例结束-------')

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)