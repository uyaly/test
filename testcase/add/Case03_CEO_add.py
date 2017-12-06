# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from pageobject.account.Page_Account_CEO_ADD import Page_Account_CEO_ADD
from utils.config import Config
from utils.log1 import Log

log = Log()


@ddt.ddt
class addCEO(unittest.TestCase):
    u'''超级总监登录，新增总监'''


    @classmethod
    def setUpClass(self):
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.A = Page_Account(self.driver)
        self.A_CEO_ADD = Page_Account_CEO_ADD(self.driver)

        self.l.open(self.url)
        # 浏览器最大化,
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)


    def test01_login(self):
        u'''超级总监登录'''
        self.username = Config().get('SCEO_LOGINNAME')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 测试结果,判断是否登录成功
        self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------超级总监登录  失败-------")
        log.info("-------超级总监登录  用例结束-------")

    def test02_add(self):
        u'''新增总监'''
        self.username = Config().get('CEO_NAME')
        self.psw = Config().get('PASSWORD')
        self.loginid = Config().get('CEO_NAME')
        self.phone = Config().get('PHONE')

        self.driver.implicitly_wait(10)
        # 进入模块
        self.A.IntoModule("总监1")
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
        self.A_CEO_ADD.input_loginid(self.loginid)
        time.sleep(3)
        self.A_CEO_ADD.input_psw(self.psw)
        time.sleep(3)
        self.A_CEO_ADD.input_psw1(self.psw)
        time.sleep(3)
        self.A_CEO_ADD.input_name(self.username)
        time.sleep(3)
        self.A_CEO_ADD.input_phone(self.phone)
        time.sleep(3)
        self.A_CEO_ADD.click_save()
        # 判断是否新建成功
        self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
        # 确定
        self.A_CEO_ADD.click_ok()
        log.info('-------新增总监    用例结束-------')


    @classmethod
    def tearDownClass(self):
        # 关闭浏览器
        self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)