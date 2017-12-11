# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from pageobject.account.Page_Account_HZ_ZSHY_original import Page_ZSHY_original
from pageobject.account.Page_Account_HZ_ZD_original import Page_ZD_original
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from utils.config import Config
from utils.log1 import Log
from utils.location import getData

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()
# @ddt.ddt
class HZoriginal(unittest.TestCase):
    '''会长登录，增修额度：直属会员、总代'''

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
        log.info("-------代理登录               用例结束-------")

    def test02_originalHY(self):
        '''对会员增修额度'''
        self.zo = Page_ZSHY_original(self.driver)
        self.username = Config().get('HY_NAME')
        original = getData(1, "DL_HY_original")
        # 进入模块
        self.A.IntoModule("帐号1会员1")
        # 切换ifream
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,增修额度
        self.assertTrue(self.A.select_row(self.username))
        self.A.original()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 修改
        self.zo.input_original(str(original))
        # 保存、确定
        self.A.click_save()
        self.A.click_ok()
        # 判断是否修改成功
        time.sleep(1)
        self.assertTrue(self.l.is_text_in_element(self.A.alert_text, "操作成功", str(self.l.get_text(self.A.alert_text))))
        # 确定按钮
        self.A.click_ok()
        log.info('-------修改【会员】初期额度    用例结束-------')

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