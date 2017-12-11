# coding:utf-8
from selenium.webdriver.common.keys import Keys
from utils.config import Config
from utils.ly_selenium import ly  # 导入4.11二次封装的类
from selenium.webdriver.support.wait import WebDriverWait
import time
class Page_Account(ly):
    # 定位器，定位页面元素
    loginout_loc = ("id", 'loginOut')
    # 账号管理
    Account_loc4 = ("xpath", ".//*[@id='navi']/div/div/div[4]/div/a/em")
    Account_loc1 = ("xpath", ".//*[@id='navi']/div/div/div[1]/div/a/em")
    Account_loc2 = ("xpath", ".//*[@id='navi']/div/div/div[2]/div/a/em")
    # 子模块
    GS_loc1 = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[1]/a")
    SCEO_loc2 = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[2]/a")
    CEO_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[3]/a")
    CEO_loc1 = ("xpath", ".//*[@id='navi']/div/div/div[1]/ul/li/a")
    LEA_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[4]/a")
    LEA_loc1 = ("xpath", ".//*[@id='navi']/div/div/div[2]/ul/li[1]/a")
    HZ_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[5]/a")
    HZ_loc2 = ("xpath", ".//*[@id='navi']/div/div/div[2]/ul/li[2]/a")
    ZD_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[6]/a")
    ZD_loc1 = ("xpath", ".//*[@id='navi']/div/div/div[2]/ul/li[1]/a")
    DL_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[7]/a")
    DL_loc1 = ("xpath", ".//*[@id='navi']/div/div/div[1]/ul/li[1]/a")
    ZSHY_loc3 = ("xpath", ".//*[@id='navi']/div/div/div[1]/ul/li[3]/a")
    ZSHY_loc4 = ("xpath", ".//*[@id='navi']/div/div/div[2]/ul/li[4]/a")
    HY_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[8]/a")
    HY_loc1 = ("xpath", ".//*[@id='navi']/div/div/div[1]/ul/li[1]/a")
    HY_loc2 = ("xpath", ".//*[@id='navi']/div/div/div[1]/ul/li[2]/a")
    # 功能按钮，增删改查
    ADD_Button = ("id", 'add_Link')
    DEL_Button = ("id", 'del_Link')
    EDIT_Button = ("id", 'edit_Link')
    QUERY_Button = ("id", 'a_query')
    ZXED_Button = ("id", 'originalAmount_Link')
    FFHS_Button = ("id", 'recoveryAmount_Link')
    # 删除一行
    row_loc = ("class name", "datagrid-row")    # 待删行
    save_button = ("class name", 'l-btn-text')    # 保存
    ok_button = ("link text", '确定')    # 确定
    psw = Config().get('PASSWORD')
    # 初始额度
    HZ_ZSHY_loc = ("field", "OriginalAmount")    # 会长登录，直属会员
    # 查询
    account_loc = ("id", 'a_query')
    # 弹出窗口文字
    alert_text = ("class name", "messager-body")

    def IntoModule(self, module):
        '''进入模块'''
        # 等待时长10秒，默认0.5秒询问一次
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("loginOut"))

        if (module == "帐号4公司1"):
            self.click(self.Account_loc4)
            time.sleep(1)
            self.click(self.GS_loc1)

        elif (module == "帐号4超级总监2"):
            self.click(self.Account_loc4)
            time.sleep(1)
            self.click(self.SCEO_loc2)

        # 超级总监登录进入总监子模块
        elif (module == "帐号1总监1"):
            self.click(self.Account_loc1)
            time.sleep(1)
            self.click(self.CEO_loc1)

        # 总监登录，操作联盟主
        elif (module == "帐号2联盟主1"):
            self.click(self.Account_loc2)
            time.sleep(1)
            self.click(self.LEA_loc1)

        # 总监登录,操作会长
        elif (module == "帐号2会长2"):
            self.click(self.Account_loc2)
            time.sleep(1)
            self.click(self.HZ_loc2)

        # 会长登录，操作总代
        elif (module == "帐号2总代1"):
            self.click(self.Account_loc2)
            time.sleep(1)
            self.click(self.ZD_loc1)
        elif (module == "帐号2直属会员4"):
            self.click(self.Account_loc2)
            time.sleep(1)
            self.click(self.ZSHY_loc4)
        elif (module == "总代1"):
            self.click(self.ZD_loc1)

        # 总代登录，操作代理和删直属会员
        elif (module == "帐号1代理1"):
            self.click(self.Account_loc1)
            time.sleep(1)
            self.click(self.DL_loc1)
        elif (module == "帐号1直属会员3"):
            self.click(self.Account_loc1)
            time.sleep(1)
            self.click(self.ZSHY_loc3)
        elif (module == "代理1"):
            self.click(self.DL_loc1)

        # 代理登录，增删会员（包含直属会员）
        elif (module == "帐号1会员1"):
            self.click(self.Account_loc1)
            time.sleep(1)
            self.click(self.HY_loc1)
        else:
            self.click(self.Account_loc4)
            self.click(self.HY_loc)

    def LoginOut(self):
        '''退出'''
        self.click(self.loginout_loc)

    def add(self):
        '''点击新增按钮'''
        self.send_keys_botton(self.ADD_Button, Keys.ENTER)

    def delete(self):
        '''点击删除按钮'''
        self.send_keys_botton(self.DEL_Button, Keys.ENTER)

    def edit(self):
        '''点击修改按钮'''
        self.send_keys_botton(self.EDIT_Button, Keys.ENTER)

    def query(self):
        '''点击查询按钮'''
        self.send_keys_botton(self.QUERY_Button, Keys.ENTER)

    def original(self):
        '''点击增修额度按钮'''
        self.send_keys_botton(self.ZXED_Button, Keys.ENTER)

    def recovery(self):
        '''点击发放与回收按钮'''
        self.send_keys_botton(self.FFHS_Button, Keys.ENTER)

    def select_row(self, username):
        '''选中列表待删行'''
        b = False
        row = self.find_elements(self.row_loc)
        try:
            for n in range(len(row)):
                # print row[n].text
                if username in row[n].text:
                    row[n].click()
                    b = True
                    return b
            if b == False:
                return False
        except Exception as msg:
            print("Error:%s" % msg)

    # def select_row(self, username):
    #     '''查找列表中的初期额度'''
    #     b = False
    #     row = self.find_elements(self.row_loc)
    #     try:
    #         for n in range(len(row)):
    #             # print row[n].text
    #             if username in row[n].text:
    #                 row[n].click()
    #                 b = True
    #                 return b
    #         if b == False:
    #             return False
    #     except Exception as msg:
    #         print("Error:%s" % msg)

    def click_save(self):
        '''保存'''
        self.click(self.save_button)

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)

    def input_account(self, username):
        '''输入查询账号'''
        self.send_keys(self.account_loc, username)
