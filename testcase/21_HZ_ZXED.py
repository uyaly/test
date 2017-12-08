# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from pageobject.account.Page_Account_ALL_original import Page_Account_ALL_original
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from utils.config import Config
from utils.config import Data
from utils.log1 import Log
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()

@ddt.ddt
class HZoriginal(unittest.TestCase):
    '''会长登录，增修额度：直属会员、总代'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)
        self.A = Page_Account(self.driver)
        self.l.open(self.url)
        self.o = Page_Account_ALL_original(self.driver)

    def test01_login(self):
        '''会长登录'''
        self.username = Config().get('HZ_LOGINNAME')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginout_loc, "退出", "-------会长登录  失败-------"))
        log.info("-------会长登录              用例结束-------")

    def test02_originalZSHY(self):
        '''对直属会员增修额度'''
        self.username = Config().get('HZ_LOGINNAME')
        self.original = Data().get('HZ_ZSHY_original')
        # 进入模块
        self.A.IntoModule("帐号2直属会员4")
        # 切换ifream
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,增修额度
        self.assertTrue(self.A.select_row(self.username))
        self.A.original()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 修改
        self.o.input_original(self.original)
        # 保存、确定
        self.A.click_ok()
        self.A.click_ok()
        # 判断是否修改成功
        time.sleep(1)
        self.assertTrue(self.l.is_text_in_element(self.A.alert_text, "操作成功", str(self.l.get_text(self.A.alert_text))))
        # 确定按钮
        self.A.click_ok()
        log.info('-------修改会长【直属会员】初期额度  用例结束-------')

    # def test03_originalZD(self):
    #     '''对总代理增修额度'''
    #     self.username = Config().get('ZD_NAME')
    #     self.original = Config().get('ZD_original')
    #     # 进入模块
    #     self.A.IntoModule("帐号2总代1")
    #     # 切换iframe
    #     i = self.driver.find_element_by_id("mainIframe")
    #     self.driver.switch_to.frame(i)
    #     # 选中一行,增修额度
    #     self.assertTrue(self.A.select_row(self.username))
    #     self.A.original()
    #     # 释放iframe
    #     self.driver.switch_to.default_content()
    #     # 修改
    #     self.o.input_original(self.original)
    #     # 保存、确定
    #     self.A.click_ok()
    #     self.A.click_ok()
    #     # 判断是否修改成功
    #     time.sleep(1)
    #     self.assertTrue(self.l.is_text_in_element(self.A.alert_text, "操作成功", str(self.l.get_text(self.A.alert_text))))
    #     # 确定按钮
    #     self.A.click_ok()
    #     log.info('-------修改【总代理】初期额度       用例结束-------')

    # def test09_loginout(self):
    #     '''会长退出'''
    #     self.A.LoginOut()
    #     log.info("-------会长退出           用例结束-------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)