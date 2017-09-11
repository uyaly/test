# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from pageobject.account.Page_Account_HZ_ADD import Page_Account_HZ_ADD
from utils.config import Config
from utils.log1 import Log

log = Log()


@ddt.ddt
class addcompany(unittest.TestCase):
    u'''登录'''


    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.A = Page_Account(self.driver)
        self.A_HZ_ADD = Page_Account_HZ_ADD(self.driver)

        # self.driver.get(self.url)
        self.l.open(self.url)
        # 浏览器最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def test01_login(self):
        '''公司登录'''
        self.username = Config().get('GS_NAME')
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
        print("-------公司登录  成功-------")
        log.info("-------公司登录  用例结束-------")

    def test02_addcompany(self):
        '''新增会长'''
        self.username = Config().get('HZ_LOGINNAME')
        self.psw = Config().get('PASSWORD')
        self.loginid = Config().get('HZ_NAME')
        self.phone = Config().get('PHONE')

        self.driver.implicitly_wait(10)
        # 进入模块
        self.A.IntoModule("会长")
        self.driver.implicitly_wait(30)
        # 点击新增按钮
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        # 感谢QQ：326186713 流年斑驳XXXXXX,input标签中的按钮要用send_keys(Keys.ENTER)来点击
        self.A.add()
        self.driver.implicitly_wait(3)
        # 释放iframe，重新回到主页上XXXXXX,iframe一定要切回来
        self.driver.switch_to.default_content()
        # 新增界面
        time.sleep(3)
        self.A_HZ_ADD.input_club(self.username)
        time.sleep(3)
        # 滚动到底部
        self.driver.execute_script("$('#form>div')[0].scrollTop=500")
        time.sleep(3)
        self.A_HZ_ADD.input_loginid(self.loginid)
        time.sleep(3)
        self.A_HZ_ADD.input_psw(self.psw)
        time.sleep(3)
        self.A_HZ_ADD.input_psw1(self.psw)
        time.sleep(3)
        self.A_HZ_ADD.input_name(self.username)
        time.sleep(3)
        self.A_HZ_ADD.input_phone(self.phone)
        time.sleep(3)
        self.A_HZ_ADD.click_save()
        self.A_HZ_ADD.click_ok()
        log.info('-------新增会长    用例结束-------')

    def test03_loginout(self):
        '''退出'''
        self.A.LoginOut()
        log.info("-------公司退出  用例结束-------")

    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)