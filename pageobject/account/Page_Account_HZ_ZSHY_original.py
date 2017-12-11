# coding:utf-8
from utils.ly_selenium import ly  # 导入4.11二次封装的类

class Page_ZSHY_original(ly):
    '''修改初期额度'''
    # 界面输入项
    original_loc = ("id", '_easyui_textbox_input7')

    def input_original(self, original):
        '''输入初期额度'''
        self.send_keys(self.original_loc, original)