# coding:utf-8
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config, DRIVER_PATH

class Page_Login(ly):
    # 定位器，定位页面元素
    username_loc = ("id", 'txtaccount')  # 输入账号
    password_loc = ("id", 'txtpassword')
    submit_loc = ("id", 'btlogin')
    #
    # username = "kaka"
    # password = "a123"

    def input_username(self, username):
        '''输入账号框'''
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        '''输入密码框'''
        self.send_keys(self.password_loc, password)

    def click_submit(self):
        '''登录按钮'''
        self.click(self.submit_loc)

    def login(self, username, password):
        '''登录方法'''
        self.input_username(username)
        self.input_password(password)
        self.click_submit()