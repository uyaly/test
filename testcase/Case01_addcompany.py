# coding:utf-8
import time
from selenium.webdriver.common.keys import Keys
import unittest
import ddt
from selenium import webdriver
from utils.config import Config, DRIVER_PATH
from utils.log1 import Log
from pageobject.Page_Login import Page_Login
from pageobject.Page_Account import Page_Account
from pageobject.Page_Account_GS import Page_Account_GS
from pageobject.Page_Account_GS_ADD import Page_Account_GS_ADD

log = Log()


@ddt.ddt
class addcompany(unittest.TestCase):
    u'''登录'''

    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        # 浏览器最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.A = Page_Account(self.driver)
        self.A_GS = Page_Account_GS(self.driver)
        self.A_GS_ADD = Page_Account_GS_ADD(self.driver)

    def test01_login(self):
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 测试结果,判断是否登录成功
        # links = self.l.is_text_in_element(("id", "loginOut"), u"退出")
        # 期望结果
        # expect_result = expect
        # self.assertEqual(result, expect_result)
        # links = self.driver.find_elements(*self.locator_result)
        # for link in links:
        print("-------管理员登录 用例结束--------")
        # log.info("-------管理员登录 用例结束--------")

    def test02_addcompany(self):
        self.driver.implicitly_wait(10)
        # 进入模块
        self.A.IntoModule("公司")
        self.driver.implicitly_wait(30)
        # 点击新增按钮
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 感谢QQ：326186713 流年斑驳XXXXXX,input标签中的按钮要用send_keys(Keys.ENTER)来点击
        # self.driver.find_element_by_id('add_Link').send_keys(Keys.ENTER)
        self.A_GS.ADD()
        self.driver.implicitly_wait(3)
        # 释放iframe，重新回到主页上XXXXXX,iframe一定要切回来
        self.driver.switch_to.default_content()

        # self.driver.find_elements_by_class_name("l-btn-text")[0].click()
        # self.driver.find_element_by_link_text("确定").click()
        # self.driver.implicitly_wait(10)
        log.info('------- 新增公司 用例结束 --------')

    # def test03_loginout(self):
    #     self.A.LoginOut()
    #     log.info("------- 退出     用例结束 --------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)