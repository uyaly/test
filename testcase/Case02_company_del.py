# coding:utf-8
import time
import unittest

import ddt
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from pageobject.account.Page_Account import Page_Account
# from pageobject.account.Page_Account_GS_DEL import Page_Account_GS_DEL
from utils.config import Config
from utils.log1 import Log

log = Log()


@ddt.ddt
class delcompany(unittest.TestCase):
    u'''登录'''


    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.A = Page_Account(self.driver)

        # self.driver.get(self.url)
        self.l.open(self.url)
        # 浏览器最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test01_login(self):
        '''管理员登录'''
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 测试结果,判断是否登录成功
        # links = self.l.is_text_in_element(("id", "loginOut"), u"退出")
        # self.assertTrue(self.l.is_text_in_value(self.A.loginout_loc, "退出"), "没有找到退出按钮")
        # 期望结果
        # expect_result = expect
        # self.assertEqual(result, expect_result)
        # links = self.driver.find_elements(*self.locator_result)
        # for link in links:
        print("-------管理员登录  成功-------")
        log.info("-------管理员登录  用例结束-------")

    def test02_delcompany(self):
        '''删除公司'''
        self.driver.implicitly_wait(10)
        self.username = Config().get('GS_NAME')
        # 进入模块
        self.A.IntoModule("公司")
        self.driver.implicitly_wait(30)
        # 点击新增按钮
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行
        time.sleep(3)
        self.A.select_row(self.username)
        # 感谢QQ：326186713 流年斑驳XXXXXX,input标签中的按钮要用send_keys(Keys.ENTER)来点击
        time.sleep(3)
        self.A.delete()
        self.driver.implicitly_wait(3)
        # 释放iframe，重新回到主页上XXXXXX,iframe一定要切回来
        self.driver.switch_to.default_content()
        # 确定按钮
        self.A.click_ok()
        log.info('-------删除公司    用例结束-------')

    def test03_loginout(self):
        '''退出'''
        self.A.LoginOut()
        log.info("-------管理员退出  用例结束-------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)