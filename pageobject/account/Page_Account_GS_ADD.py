# coding:utf-8
from utils.ly_selenium import ly  # 导入4.11二次封装的类


class Page_Account_GS_ADD(ly):
    '''公司新增'''
    loginid_loc = ("id", '_easyui_textbox_input1')
    password_loc = ("id", '_easyui_textbox_input6')
    password1_loc = ("id", '_easyui_textbox_input7')
    name_loc = ("id", '_easyui_textbox_input2')
    # 弹出窗口元素
    save_button = ("css", "span.l-btn-text")    # 保存
    ok_button = ("class name","l-btn-text")    # 确定
    # ok_button = ("class name","l-btn-small")    # 确定
    close_button = ("class name","panel-tool-close")    # 关闭
    # cancle_button = ("link text", '取  消')    # 取消
    alart_win = ("class name", "messager-window")        #  系统提示窗口

    # username = Config().get('GS_NAME')
    # psw = Config().get('PASSWORD')

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


    def click_close(self):
        '''取消'''
        try:
            self.is_located(self.close_button)
            self.click(self.close_button)
        except:
            print u"查找弹出窗口元素异常"


    def alert(self):
        '''新建成功，点击弹出界面按钮；新建不成功，关闭新建界面'''
        try:
            al = self.is_located(self.alart_win)
            if al is not False:
                # 新建公司成功
                self.click_ok()
                return True
            else:
                # 新建公司失败
                self.click_close()
                return False
        except:
            self.click_close()
            return False
            print u"查找弹出窗口元素异常"

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)