# coding:utf-8
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config, DRIVER_PATH


class Page_Account_GS_ADD(ly):

    loginid_loc = ("id", '_easyui_textbox_input1')
    password_loc = ("id", '_easyui_textbox_input6')
    password1_loc = ("id", '_easyui_textbox_input7')
    name_loc = ("id", '_easyui_textbox_input2')
    # 新增，先iframe
    # ifr_loc = ("id", 'mainIframe')
    save_button = ("class name", 'l-btn-text')    # 保存
    ok_button = ("link text", '确定')   #   确定
    username = Config().get('GS_NAME')
    psw = Config().get('PASSWORD')

    def input_loginid(self, username):
        '''输入账号'''
        self.send_keys(self.loginid_loc, username)

    def input_psw(self, psw):
        '''输入密码'''
        self.send_keys(self.password_loc, psw)

    def input_psw1(self, psw):
        '''输入确认密码'''
        self.send_keys(self.password1_loc, psw)

    def input_name(self, username):
        '''输入名字'''
        self.send_keys(self.name_loc, username)

    def click_save(self):
        '''保存'''
        self.click(self.save_button)

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)
