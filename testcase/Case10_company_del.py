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
from selenium.webdriver.support.wait import WebDriverWait

log = Log()

@ddt.ddt
class delcompany(unittest.TestCase):
    u'''管理员登录删除公司'''

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
        # 等待时长10秒，默认0.5秒询问一次
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("kw")).send_keys("yoyo")

        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        self.assertTrue(self.driver.current_url == "http://47.52.77.154:8015/Default/Index", "-------管理员登录失败-------")
        log.info('-------管理员登录    用例结束-------')

    def test02_delcompany(self):
        '''删除公司'''
        self.username = Config().get('GS_NAME')
        self.psw = Config().get('PASSWORD')
        self.driver.implicitly_wait(10)
        # 进入模块
        self.A.IntoModule("公司")
        self.driver.implicitly_wait(30)
        # 切换ifream
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 选中一行,删除
        # try:
        # self.assertTrue(self.A.select_row(self.username), "-------删除公司失败-------")
        company = self.driver.find_elements_by_class_name('datagrid-row')
        n = 0
        for n in range(len(company)):
            if self.username in company[n].text:
                company[n].click()
                self.A.delete()
        #
        # except:
        #


        # 释放iframe
        self.driver.switch_to.default_content()
        #     # 确定按钮
        #     self.A.click_ok()
        #     log.info('-------删除公司    用例结束-------')

    # def test03_loginout(self):
    #     '''管理员退出'''
    #     self.A.LoginOut()
    #     self.assertTrue(self.driver.current_url == "http://47.52.77.154:8015/Default/Login", "-------管理员退出失败-------")
    #     log.info("-------管理员退出  用例结束-------")

    # @classmethod
    # def tearDownClass(self):
    #     # 关闭浏览器
    #     self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)