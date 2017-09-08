# coding:utf-8
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config, DRIVER_PATH
from selenium.webdriver.common.keys import Keys

class Page_Account(ly):
    # 定位器，定位页面元素
    loginout_loc = ("id", 'loginOut')
    Account_loc = ("xpath", ".//*[@id='navi']/div/div/div[3]/div/a/em")
    GS_loc = ("xpath", ".//*[@id='navi']/div/div/div[3]/ul/li[1]/a")
    HZ_loc = ("xpath", ".//*[@id='navi']/div/div/div[3]/ul/li[2]/a")
    ZD_loc = ("xpath", ".//*[@id='navi']/div/div/div[3]/ul/li[3]/a")
    DL_loc = ("xpath", ".//*[@id='navi']/div/div/div[3]/ul/li[4]/a")
    HY_loc = ("xpath", ".//*[@id='navi']/div/div/div[3]/ul/li[5]/a")
    # 功能按钮，增删改查
    ADD_Button = ("id", 'add_Link')
    DEL_Button = ("id", 'del_Link')
    EDIT_Button = ("id", 'edit_Link')
    QUERY_Button = ("id", 'a_query')

    def IntoModule(self, module):
        '''进入模块'''
        self.click(self.Account_loc)
        if (module == "公司"):
            self.click(self.GS_loc)
        elif (module == "会长"):
            self.click(self.HZ_loc)
        elif (module == "总代"):
            self.click(self.ZD_loc)
        elif (module == "代理"):
            self.click(self.DL_loc)
        else:
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
