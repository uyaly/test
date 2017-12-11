# coding:utf-8
from utils.ly_selenium import ly  # 导入4.11二次封装的类

class Page_ZSHY_distribution(ly):
    '''修改发放与回收'''
    # 界面输入项
    distribution_loc = ("id", '_easyui_textbox_input9')

    def input_distribution(self, distribution):
        '''输入'''
        self.send_keys(self.distribution_loc, distribution)

