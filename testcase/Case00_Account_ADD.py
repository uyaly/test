# coding:utf-8
import time
import unittest
import ddt
from pageobject.account.Page_Account import Page_Account
from selenium import webdriver
from pageobject.Page_Login import Page_Login
from utils.config import Config
from utils.log1 import Log
from pageobject.account.Page_Account_GS_ADD import Page_Account_GS_ADD
from pageobject.account.Page_Account_SCEO_ADD import Page_Account_SCEO_ADD
from pageobject.account.Page_Account_CEO_ADD import Page_Account_CEO_ADD
from pageobject.account.Page_Account_league_ADD import Page_Account_league_ADD
from pageobject.account.Page_Account_HZ_ADD import Page_Account_HZ_ADD
from pageobject.account.Page_Account_ZD_ADD import Page_Account_ZD_ADD
from pageobject.account.Page_Account_DL_ADD import Page_Account_DL_ADD
from pageobject.account.Page_Account_HY_ADD import Page_Account_HY_ADD

log = Log()
@ddt.ddt
class add(unittest.TestCase):
    u'''新增账号'''

    @classmethod
    def setUpClass(self):
        # 打开浏览器
        self.url = Config().get('URL')
        self.driver = webdriver.Firefox()
        self.l = Page_Login(self.driver)  # login参数是LoginPage的实例
        self.l.open(self.url)
        self.driver.maximize_window()
        # 页面实例
        self.A = Page_Account(self.driver)
        self.A_GS_ADD = Page_Account_GS_ADD(self.driver)
        self.A_SCEO_ADD = Page_Account_SCEO_ADD(self.driver)
        self.A_CEO_ADD = Page_Account_CEO_ADD(self.driver)
        self.A_league_ADD = Page_Account_league_ADD(self.driver)
        self.A_HZ_ADD = Page_Account_HZ_ADD(self.driver)
        self.A_ZD_ADD = Page_Account_ZD_ADD(self.driver)
        self.A_DL_ADD = Page_Account_DL_ADD(self.driver)
        self.A_HY_ADD = Page_Account_HY_ADD(self.driver)

    def test01_login(self):
        u'''管理员登录'''
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 测试结果,判断是否登录成功
        self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------管理员登录  失败-------")
        log.info("-------管理员登录           用例结束-------")

    def test02_add(self):
        u'''新增公司'''
        self.username = Config().get('GS_NAME')
        self.psw = Config().get('PASSWORD')
        # 进入模块
        self.A.IntoModule("公司")
        # 点击新增按钮
        i = self.driver.find_element_by_id("mainIframe")
        # 切换iframe
        self.driver.switch_to.frame(i)
        self.A.add()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 新增界面
        self.A_GS_ADD.input_loginid(self.username)
        time.sleep(2)
        self.A_GS_ADD.input_psw(self.psw)
        time.sleep(2)
        self.A_GS_ADD.input_psw1(self.psw)
        time.sleep(2)
        self.A_GS_ADD.input_name(self.username)
        time.sleep(2)
        self.A_GS_ADD.click_save()
        time.sleep(2)
        # 判断是否新增成功
        self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
        # 确定
        self.A_GS_ADD.click_ok()
        log.info('-------新增【公司】         用例结束-------')

    def test03_loginout(self):
        u'''管理员退出'''
        self.A.LoginOut()
        log.info("-------管理员退出           用例结束-------")

    def test11_login(self):
        u'''公司登录'''
        self.username = Config().get('GS_NAME')
        self.psw = Config().get('PASSWORD')
        self.l.login(self.username, self.psw)
        # 判断是否登录成功
        self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------公司登录        失败-------")
        log.info("-------公司登录             用例结束-------")

    def test12_add(self):
        u'''新增超级总监'''
        self.username = Config().get('SCEO_NAME')
        self.psw = Config().get('PASSWORD')
        self.loginid = Config().get('SCEO_NAME')
        self.phone = Config().get('PHONE')
        # 进入模块
        self.A.IntoModule("超级总监")
        # 点击新增按钮
        i = self.driver.find_element_by_id("mainIframe")
        self.driver.switch_to.frame(i)
        self.A.add()
        # 释放iframe
        self.driver.switch_to.default_content()
        # 新增界面
        time.sleep(2)
        self.A_SCEO_ADD.input_loginid(self.loginid)
        time.sleep(2)
        self.A_SCEO_ADD.input_psw(self.psw)
        time.sleep(2)
        self.A_SCEO_ADD.input_psw1(self.psw)
        time.sleep(2)
        self.A_SCEO_ADD.input_name(self.username)
        time.sleep(2)
        self.A_SCEO_ADD.input_phone(self.phone)
        time.sleep(2)
        self.A_SCEO_ADD.click_save()
        # 判断是否新建成功
        self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
        # 确定
        self.A_SCEO_ADD.click_ok()
        log.info('-------新增【超级总监】     用例结束-------')

    # def test13_loginout(self):
    #     u'''公司退出'''
    #     self.A.LoginOut()
    #     # log.info("-------公司退出             用例结束-------")
    #
    # def test21_login(self):
    #     u'''超级总监登录'''
    #     self.username = Config().get('SCEO_LOGINNAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.l.login(self.username, self.psw)
    #     # 判断是否登录成功
    #     self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------超级总监登录  失败-------")
    #     log.info("-------超级总监登录         用例结束-------")
    #
    # def test22_add(self):
    #     u'''新增总监'''
    #     self.username = Config().get('CEO_NAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.loginid = Config().get('CEO_NAME')
    #     self.phone = Config().get('PHONE')
    #     # 进入模块
    #     self.A.IntoModule("总监1")
    #     # 点击新增按钮
    #     i = self.driver.find_element_by_id("mainIframe")
    #     self.driver.switch_to.frame(i)
    #     self.A.add()
    #     self.driver.implicitly_wait(3)
    #     self.driver.switch_to.default_content()
    #     # 新增界面
    #     time.sleep(2)
    #     self.A_CEO_ADD.input_loginid(self.loginid)
    #     time.sleep(2)
    #     self.A_CEO_ADD.input_psw(self.psw)
    #     time.sleep(2)
    #     self.A_CEO_ADD.input_psw1(self.psw)
    #     time.sleep(2)
    #     self.A_CEO_ADD.input_name(self.username)
    #     time.sleep(2)
    #     self.A_CEO_ADD.input_phone(self.phone)
    #     time.sleep(2)
    #     self.A_CEO_ADD.click_save()
    #     # 判断是否新建成功
    #     self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
    #     # 确定
    #     self.A_CEO_ADD.click_ok()
    #     log.info('-------新增【总监】         用例结束-------')
    #
    # def test23_loginout(self):
    #     u'''超级总监退出'''
    #     self.A.LoginOut()
    #     log.info("-------超级总监退出         用例结束-------")
    #
    # def test31_login(self):
    #     u'''总监登录'''
    #     self.username = Config().get('CEO_LOGINNAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.l.login(self.username, self.psw)
    #     # 判断是否登录成功
    #     self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------总监登录       失败-------")
    #     log.info("-------总监登录             用例结束-------")
    #
    # def test32_add(self):
    #     u'''新增联盟主'''
    #     self.username = Config().get('league_NAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.loginid = Config().get('league_NAME')
    #     self.phone = Config().get('PHONE')
    #     # 进入模块
    #     self.A.IntoModule("联盟主1")
    #     # 点击新增按钮
    #     i = self.driver.find_element_by_id("mainIframe")
    #     self.driver.switch_to.frame(i)
    #     self.A.add()
    #     self.driver.switch_to.default_content()
    #     # 新增界面
    #     time.sleep(2)
    #     self.A_league_ADD.input_loginid(self.loginid)
    #     time.sleep(2)
    #     self.A_league_ADD.input_psw(self.psw)
    #     time.sleep(2)
    #     self.A_league_ADD.input_psw1(self.psw)
    #     time.sleep(2)
    #     self.A_league_ADD.input_name(self.username)
    #     time.sleep(2)
    #     self.A_league_ADD.input_phone(self.phone)
    #     time.sleep(2)
    #     self.A_league_ADD.click_save()
    #     # 判断是否新建成功
    #     self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
    #     # 确定
    #     self.A_league_ADD.click_ok()
    #     log.info('-------新增【联盟主】       用例结束-------')
    #
    # def test33_add(self):
    #     u'''新增会长'''
    #     self.username = Config().get('HZ_LOGINNAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.loginid = Config().get('HZ_NAME')
    #     self.phone = Config().get('PHONE')
    #     # 进入模块
    #     self.A.IntoModule("会长2")
    #     # 点击新增按钮
    #     i = self.driver.find_element_by_id("mainIframe")
    #     self.driver.switch_to.frame(i)
    #     self.A.add()
    #     self.driver.switch_to.default_content()
    #     # 新增界面
    #     time.sleep(3)
    #     self.A_HZ_ADD.input_club(self.username)
    #     time.sleep(2)
    #     # 滚动到底部
    #     self.driver.execute_script("$('#form>div')[0].scrollTop=500")
    #     time.sleep(2)
    #     self.A_HZ_ADD.input_loginid(self.loginid)
    #     time.sleep(2)
    #     self.A_HZ_ADD.input_psw(self.psw)
    #     time.sleep(2)
    #     self.A_HZ_ADD.input_psw1(self.psw)
    #     time.sleep(2)
    #     self.A_HZ_ADD.input_name(self.username)
    #     time.sleep(2)
    #     self.A_HZ_ADD.input_phone(self.phone)
    #     time.sleep(2)
    #     self.A_HZ_ADD.click_save()
    #     time.sleep(2)
    #     # 判断是否新建成功
    #     self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
    #     # 确定
    #     self.A_HZ_ADD.click_ok()
    #     log.info('-------新增【会长】         用例结束-------')
    #
    # def test34_loginout(self):
    #     u'''总监退出'''
    #     self.A.LoginOut()
    #     log.info("-------超级总监退出         用例结束-------")
    #
    # def test41_login(self):
    #     u'''会长登录'''
    #     self.username = Config().get('HZ_LOGINNAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.l.login(self.username, self.psw)
    #     # 判断是否登录成功
    #     self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------会长登录  失败-------")
    #     log.info("-------会长登录            用例结束-------")
    #
    # def test42_add(self):
    #     u'''新增总代理'''
    #     self.username = Config().get('ZD_NAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.loginid = Config().get('ZD_NAME')
    #     self.phone = Config().get('PHONE')
    #     # 进入模块
    #     self.A.IntoModule("总代1")
    #     # 点击新增按钮
    #     i = self.driver.find_element_by_id("mainIframe")
    #     self.driver.switch_to.frame(i)
    #     self.A.add()
    #     self.driver.switch_to.default_content()
    #     # 新增界面
    #     time.sleep(2)
    #     self.A_ZD_ADD.input_loginid(self.loginid)
    #     time.sleep(2)
    #     self.A_ZD_ADD.input_psw(self.psw)
    #     time.sleep(2)
    #     self.A_ZD_ADD.input_psw1(self.psw)
    #     time.sleep(2)
    #     self.A_ZD_ADD.input_name(self.username)
    #     time.sleep(2)
    #     self.A_ZD_ADD.input_phone(self.phone)
    #     time.sleep(2)
    #     self.A_ZD_ADD.click_save()
    #     time.sleep(2)
    #     # 判断是否新建成功
    #     self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
    #     # 确定
    #     self.A_ZD_ADD.click_ok()
    #     log.info('-------新增【总代】        用例结束-------')
    #
    # def test43_loginout(self):
    #     u'''会长退出'''
    #     self.A.LoginOut()
    #     log.info("-------会长退出            用例结束-------")
    #
    # def test51_login(self):
    #     u'''总代理登录'''
    #     self.username = Config().get('ZD_NAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.l.login(self.username, self.psw)
    #     # 判断是否登录成功
    #     self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------总代登录  失败-------")
    #     log.info("-------总代登录            用例结束-------")
    #
    # def test52_add(self):
    #     u'''新增代理'''
    #     self.username = Config().get('DL_NAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.loginid = Config().get('DL_NAME')
    #     self.phone = Config().get('PHONE')
    #     # 进入模块
    #     self.A.IntoModule("代理1")
    #     # 点击新增按钮
    #     i = self.driver.find_element_by_id("mainIframe")
    #     self.driver.switch_to.frame(i)
    #     self.A.add()
    #     self.driver.switch_to.default_content()
    #     time.sleep(2)
    #     self.A_DL_ADD.input_loginid(self.loginid)
    #     time.sleep(2)
    #     self.A_DL_ADD.input_psw(self.psw)
    #     time.sleep(2)
    #     self.A_DL_ADD.input_psw1(self.psw)
    #     time.sleep(2)
    #     self.A_DL_ADD.input_name(self.username)
    #     time.sleep(2)
    #     self.A_DL_ADD.input_phone(self.phone)
    #     time.sleep(2)
    #     self.A_DL_ADD.click_save()
    #     time.sleep(2)
    #     # 判断是否新建成功
    #     self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
    #     # 确定
    #     self.A_DL_ADD.click_ok()
    #     log.info('-------新增【代理】        用例结束-------')
    #
    # def test53_loginout(self):
    #     u'''总代退出'''
    #     self.A.LoginOut()
    #     log.info("-------总代退出            用例结束-------")
    #
    # def test61_login(self):
    #     u'''代理登录'''
    #     self.username = Config().get('DL_NAME')
    #     self.psw = Config().get('PASSWORD')
    #     self.l.login(self.username, self.psw)
    #     # 判断是否登录成功
    #     self.assertTrue((self.l.is_text_in_element(("id", "loginOut"), u"退出")), "-------代理登录  失败-------")
    #     log.info("-------代理登录            用例结束-------")
    #
    # def test62_add(self):
    #     u'''新增会员'''
    #     self.loginid = Config().get('HY_NAME')
    #     self.phone = Config().get('PHONE1')
    #     # 进入模块
    #     self.A.IntoModule("会员1")
    #     # 点击新增按钮
    #     i = self.driver.find_element_by_id("mainIframe")
    #     self.driver.switch_to.frame(i)
    #     self.A.add()
    #     self.driver.implicitly_wait(3)
    #     self.driver.switch_to.default_content()
    #     # 新增界面
    #     time.sleep(2)
    #     self.A_HY_ADD.input_loginid(self.loginid)
    #     time.sleep(2)
    #     self.A_HY_ADD.input_phone(self.phone)
    #     time.sleep(2)
    #     self.A_HY_ADD.click_save()
    #     time.sleep(2)
    #     # 判断是否新建成功
    #     self.assertTrue((self.l.is_text_in_element(("class name", "messager-body"), u"新增成功")), self.driver.find_element("class name","messager-body").text)
    #     # 确定
    #     self.A_HY_ADD.click_ok()
    #     log.info('-------新增会员    用例结束-------')
    #
    # def test63_loginout(self):
    #     u'''代理退出'''
    #     self.A.LoginOut()
    #     log.info("-------总代退出            用例结束-------")


    # @classmethod
    # def tearDownClass(self):
    #     # 关闭浏览器
    #     self.driver.quit()

# 执行测试主函数
if __name__ == '__main__':
    # 执行main全局方法，将会执行上述所有以test开头的测试方法
    unittest.main(verbosity=2)