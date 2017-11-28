# coding:utf-8
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config, DRIVER_PATH
from selenium.webdriver.common.keys import Keys

class Page_Account(ly):
    # 定位器，定位页面元素
    loginout_loc = ("id", 'loginOut')
    Account_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/div/a/em")
    GS_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[1]/a")
    SCEO_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[2]/a")
    CEO_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[3]/a")
    LEA_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[4]/a")
    HZ_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[5]/a")
    ZD_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[6]/a")
    DL_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[7]/a")
    HY_loc = ("xpath", ".//*[@id='navi']/div/div/div[4]/ul/li[8]/a")
    # 功能按钮，增删改查
    ADD_Button = ("id", 'add_Link')
    DEL_Button = ("id", 'del_Link')
    EDIT_Button = ("id", 'edit_Link')
    QUERY_Button = ("id", 'a_query')
    # 删除一行
    company_loc = ("class name", 'datagrid-row')    # 待删行
    ok_button = ("link text", '确定')    # 确定
    gs_name = Config().get('GS_NAME')
    psw = Config().get('PASSWORD')
    # 查询
    account_loc = ("id", 'a_query')

    def IntoModule(self, module):
        '''进入模块'''
        self.click(self.Account_loc)
        if (module == "公司"):
            self.click(self.GS_loc)
        elif (module == "超级总监"):
            self.click(self.SCEO_loc)
        elif (module == "总监"):
            self.click(self.CEO_loc)
        elif (module == "联盟主"):
            self.click(self.GS_loc)
        elif (module == "公司"):
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

    def select_row(self, username):
        '''选中列表中一行'''
        company = self.find_elements(self.company_loc)
        # print company[1]
        for i in company:
            if (company[i].text == username):
                self.click(self.company_loc)
            else:
                print "没有查到"

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)

    def input_account(self, username):
        '''输入查询账号'''
        self.send_keys(self.account_loc, username)