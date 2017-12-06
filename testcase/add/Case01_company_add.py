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
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = Log()
@ddt.ddt
class addcompany(unittest.TestCase):
    u'''管理员登录，新增公司'''

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
        u'''管理员登录'''
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue(self.l.is_text_in_element(self.A.loginout_loc, "退出", "-------管理员登录  失败-------"))
        log.info("-------管理员登录  用例结束-------")

    def test02_add(self):
        u'''新增公司'''
        self.username = Config().get('GS_NAME')
        self.psw = Config().get('PASSWORD')
        self.driver.implicitly_wait(10)
        # 进入模块
        self.A.IntoModule("公司")
        self.driver.implicitly_wait(30)
        # 点击新增按钮
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        self.A.add()
        self.driver.implicitly_wait(3)
        # 释放iframe，重新回到主页上XXXXXX,iframe一定要切回来
        self.driver.switch_to.default_content()
        # 新增界面
        self.A_GS_ADD.input_loginid(self.username)
        time.sleep(3)
        self.A_GS_ADD.input_psw(self.psw)
        time.sleep(3)
        self.A_GS_ADD.input_psw1(self.psw)
        time.sleep(3)
        self.A_GS_ADD.input_name(self.username)
        time.sleep(3)
        self.A_GS_ADD.click_save()
        time.sleep(3)
        # 判断是否新建成功
        time.sleep(1)
        self.l.is_text_in_element(self.A.alert_text, "新增成功", str(self.l.get_text(self.A.alert_text)))
        # 确定
        self.A.click_ok()
        log.info('-------新增公司    用例结束-------')

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)