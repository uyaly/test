# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from pageobject.account.Page_Account_HZ_ZSHY_distribution import Page_ZSHY_distribution
from pageobject.account.Page_Account_HZ_ZD_distribution import Page_ZD_distribution
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
class HZdistribution(unittest.TestCase):
    '''会长登录，发放回收：直属会员、总代'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)
        self.A = Page_Account(self.driver)
        self.l.open(self.url)

    def test01_login(self):
        '''会长登录'''
        self.username = Config().get('HZ_LOGINNAME')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginout_loc, "退出", "-------会长登录  失败-------"))
        log.info("-------会长登录              用例结束-------")

    def test02_distributionZSHY(self):
        '''对直属会员发放'''
        self.zo = Page_ZSHY_distribution(self.driver)      # 修改了这里lllllllllll+++++++++++++++++++++++++++++++++++++++++++++
        self.username = Config().get('HZ_NAME')
        distribution = getData(2, "HZ_ZSHY")     # 修改了这里lllllllllll+++++++++++++++++++++++++++++++++++++++++++++
        # 进入模块
        self.A.IntoModule("帐号2直属会员4")
        # 切换ifream
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,增修额度
        self.assertTrue(self.A.select_row(self.username))
        self.A.distribution()     # 修改了这里lllllllllll+++++++++++++++++++++++++++++++++++++++++++++
        # 释放iframe
        self.driver.switch_to.default_content()
        # 修改
        self.zo.input_distribution(str(distribution))     # 修改了这里lllllllllll+++++++++++++++++++++++++++++++++++++++++++++
        # 保存、确定
        self.A.click_save()
        self.A.click_ok()
        # 判断是否修改成功
        time.sleep(1)
        self.assertTrue(self.l.is_text_in_element(self.A.alert_text, "操作成功", str(self.l.get_text(self.A.alert_text))))
        # 确定按钮
        self.A.click_ok()
        log.info('-------会长发放【直属会员】        用例结束-------')

    def test03_distributionZD(self):
        '''对总代理发放'''
        self.username = Config().get('ZD_NAME')
        self.zd = Page_ZD_distribution(self.driver)
        distribution = getData(2, "HZ_ZD")
        # 进入模块
        self.A.IntoModule("总代1")
        # 切换iframe
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,增修额度
        self.assertTrue(self.A.select_row(self.username))
        self.A.distribution()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 修改
        self.zd.input_distribution(str(distribution))
        # 保存、确定
        self.A.click_save()
        self.A.click_ok()
        # 判断是否修改成功
        time.sleep(1)
        self.assertTrue(self.l.is_text_in_element(self.A.alert_text, "操作成功", str(self.l.get_text(self.A.alert_text))))
        # 确定按钮
        self.A.click_ok()
        log.info('-------会长发放【总代理】             用例结束-------')

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