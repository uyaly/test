# coding:utf-8
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config, DRIVER_PATH
from selenium.webdriver.common.keys import Keys

class Page_Account_GS(ly):
    # 定位器，定位页面元素
    ADD_Button = ("id", 'add_Link')

    def ADD(self):
        self.send_keys(Keys.ENTER)

    # def DEL(self):
    # def DEL(self):
    # def DEL(self):
    #
