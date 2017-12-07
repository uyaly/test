# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from pageobject.account.Page_Account_HY_ADD import Page_Account_HY_ADD
from utils.config import Config
from utils.log1 import Log
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()

@ddt.ddt
class addZD(unittest.TestCase):
    '''代理登录，新增会员'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.A = Page_Account(self.driver)
        self.A_HY_ADD = Page_Account_HY_ADD(self.driver)
        self.l.open(self.url)
        # 浏览器最大化
        self.driver.maximize_window()

    def test01_login(self):
        '''代理登录'''
        self.username = Config().get('DL_NAME')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginout_loc, "退出", "-------代理登录  失败-------"))
        log.info("-------代理登录  用例结束-------")

    def test02_add(self):
        '''新增会员'''
        self.loginid = Config().get('HY_NAME')
        self.phone = Config().get('PHONE1')
        # 进入模块
        self.A.IntoModule("帐号1会员1")
        # 点击新增按钮
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        self.A.add()
        self.driver.switch_to.default_content()
        # 新增界面
        time.sleep(2)
        self.A_HY_ADD.input_loginid(self.loginid)
        time.sleep(2)
        self.A_HY_ADD.input_phone(self.phone)
        time.sleep(2)
        self.A_HY_ADD.click_save()
        time.sleep(2)
        # 判断是否新建成功
        self.l.is_text_in_element(self.A.alert_text, "新增成功", str(self.l.get_text(self.A.alert_text)))
        # 确定
        self.A_HY_ADD.click_ok()
        log.info('-------新增会员    用例结束-------')

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)