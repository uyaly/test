# coding:utf-8
import unittest
from utils.config import Config
from selenium import webdriver
from testcase.Case01_login import Login
from pageobject.Page_Login import LoginPage


class AdminLogin(unittest.TestCase):
    '''管理员登录场景'''

    def setUp(self):
        pass
    def test_01(self):
        self.username = Config().get('ADMIN')
        self.psw = Config().get('PASSWORD')
        self.login = Login().s_adminlogin  # login参数是LoginPage的实例
        self.login.login(self.username, self.psw)


if __name__ == "__main__":
    unittest.main()
