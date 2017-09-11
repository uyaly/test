# coding:utf-8
from pageobject.account.Page_Account import Page_Account
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config


class Page_Account_GS_DEL(ly):

    company_loc = ("id", 'datagrid-row-r1-2-0')    # 待删行

    ok_button = ("link text", '确定')    # 确定
    username = Config().get('GS_NAME')
    psw = Config().get('PASSWORD')


    def select_row(self, username):
        '''选中行'''
        company = self.find_elements(self.company_loc)
        for i in company:
            if (company[i] == username):
                self.click(self.company_loc)

    def click_del(self):
        '''删除'''
        self.A = Page_Account(self.driver)
        self.A.delete()

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)
