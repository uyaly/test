# coding:utf-8
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config, DRIVER_PATH

class Page_Account_CEO_ADD(ly):
    '''总监新增'''
    # 新增界面输入项
    loginid_loc = ("id", '_easyui_textbox_input1')
    password_loc = ("id", '_easyui_textbox_input5')
    password1_loc = ("id", '_easyui_textbox_input6')
    name_loc = ("id", '_easyui_textbox_input2')
    phone_loc = ("id", '_easyui_textbox_input3')

    # 新增界面按钮
    save_button = ("class name", 'l-btn-text')    # 保存
    ok_button = ("link text", '确定')   #   确定

    # username = Config().get('CEO_LOGINNAME')
    # psw = Config().get('PASSWORD')
    # loginid = Config().get('CEO_NAME')
    # phone = Config().get('PHONE')

    def input_loginid(self, loginid):
        '''输入账号'''
        self.send_keys(self.loginid_loc, loginid)

    def input_psw(self, psw):
        '''输入密码'''
        self.send_keys(self.password_loc, psw)

    def input_psw1(self, psw):
        '''输入确认密码'''
        self.send_keys(self.password1_loc, psw)

    def input_name(self, username):
        '''输入名字'''
        self.send_keys(self.name_loc, username)

    def input_phone(self, phone):
        '''输入名字'''
        self.send_keys(self.phone_loc, phone)

    def click_save(self):
        '''保存'''
        self.click(self.save_button)

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)
