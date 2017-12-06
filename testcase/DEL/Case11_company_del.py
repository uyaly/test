# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from utils.config import Config
from utils.log1 import Log
from pageobject.account.Page_Account_GS_ADD import Page_Account_GS_ADD
from selenium.webdriver.support.wait import WebDriverWait
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()

@ddt.ddt
class delcompany(unittest.TestCase):
    u'''管理员登录,删除公司'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)
        self.A = Page_Account(self.driver)
        self.A_GS_ADD = Page_Account_GS_ADD(self.driver)
        self.l.open(self.url)
        # 浏览器最大化
        self.driver.maximize_window()

    def test01_login(self):
        '''管理员登录'''
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginout_loc, "退出", "-------管理员登录  失败-------"))
        log.info("-------管理员登录          用例结束-------")

    def test02_delcompany(self):
        '''删除公司'''
        self.username = Config().get('GS_NAME')
        self.psw = Config().get('PASSWORD')
        # 进入模块
        self.A.IntoModule("公司")
        # 切换ifream
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,删除
        self.A.select_row(self.username)
        self.A.delete()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 确定按钮
        self.A.click_ok()
        # 判断是否新建成功
        time.sleep(1)
        self.l.is_text_in_element(self.A.alert_text, "删除成功", str(self.l.get_text(self.A.alert_text)))
        # 确定按钮
        self.A.click_ok()
        log.info('-------删除【公司】           用例结束-------')

    # def test09_loginout(self):
    #     u'''管理员退出'''
    #     self.A.LoginOut()
    #     log.info("-------管理员退出           用例结束-------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)