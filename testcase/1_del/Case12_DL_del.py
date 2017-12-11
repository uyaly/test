# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from utils.config import Config
from utils.log1 import Log
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()

@ddt.ddt
class delDL(unittest.TestCase):
    '''代理登录,删除直属会员
    总代登录,删除代理'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)
        self.A = Page_Account(self.driver)
        self.l.open(self.url)

    def test01_login(self):
        '''代理登录'''
        self.username = Config().get('DL_NAME')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginout_loc, "退出", "-------代理登录  失败-------"))
        log.info("-------代理登录              用例结束-------")

    def test02_delZSHY(self):
        '''删除代理的直属会员'''
        self.username = Config().get('DL_NAME')
        # 进入模块
        self.A.IntoModule("帐号1会员1")
        # 切换ifream
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,删除
        self.assertTrue(self.A.select_row(self.username))
        self.A.delete()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 确定按钮
        self.A.click_ok()
        # 判断是否删除成功
        time.sleep(1)
        self.assertTrue(self.l.is_text_in_element(self.A.alert_text, "删除成功", str(self.l.get_text(self.A.alert_text))))
        # 确定按钮
        self.A.click_ok()
        log.info('-------删除代理【直属会员】  用例结束-------')

    def test03_loginout(self):
        '''代理退出'''
        # 释放iframe
        self.driver.switch_to.default_content()
        self.A.LoginOut()
        log.info("-------代理退出              用例结束-------")

    def test04_login(self):
        '''总代登录'''
        self.username = Config().get('ZD_NAME')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginout_loc, "退出", "-------总代登录  失败-------"))
        log.info("-------总代登录              用例结束-------")

    def test05_delDL(self):
        '''删除代理'''
        self.username = Config().get('DL_NAME')
        # 进入模块
        self.A.IntoModule("帐号1代理1")
        # 切换ifream
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,删除
        self.assertTrue(self.A.select_row(self.username))
        self.A.delete()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 确定按钮
        self.A.click_ok()
        # 判断是否删除成功
        time.sleep(1)
        self.assertTrue(self.l.is_text_in_element(self.A.alert_text, "删除成功", str(self.l.get_text(self.A.alert_text))))
        # 确定按钮
        self.A.click_ok()
        log.info('-------删除【代理】          用例结束-------')



    # def test09_loginout(self):
    #     '''总代退出'''
    #     self.A.LoginOut()
    #     log.info("-------总代退出           用例结束-------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)