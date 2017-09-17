# coding:utf-8
from testcase.ly_selenium import ly  # 导入4.11二次封装的类
from utils.config import Config, DRIVER_PATH


class Page_Account_GS_ADD(ly):

    loginid_loc = ("id", '_easyui_textbox_input1')
    password_loc = ("id", '_easyui_textbox_input6')
    password1_loc = ("id", '_easyui_textbox_input7')
    name_loc = ("id", '_easyui_textbox_input2')
    # 弹出窗口元素
    save_button = ("css", "span.l-btn-text")    # 保存
    ok_button = ("class name","l-btn-text")    # 确定
    # ok_button = ("class name","l-btn-small")    # 确定
    close_button = ("css","a.panel-tool-close")    # 关闭
    cancle_button = ("link text", '取  消')    # 取消
    alart_win = ("class name", "messager-window")        #  系统提示窗口

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

        result = EC.alert_is_present()(driver)
        if result:
            print result.text
            result.accept()
        else:
            print "alert 未弹出！"

        # ok = self.l.is_visibility(self.driver.find_elements_by_class_name("messager-window"))
        # print ok
        # if ok == False:
        #     print "新增公司失败，用户名被占用"
        #     self.A.click_close()
        # else:
        #     print "新建公司成功"
        #     self.A.click_ok()

    def click_close(self):
        '''取消'''
        self.click(self.close_button)

    # def alert(self):
    #     '''保存'''
    #     if self.is_alert_present()
    #     if self.is_text_in_value(self.ok_button, "确定"):
    #         print "新建公司成功"
    #         self.click_ok()
    #         return True
    #     # elif:
    #     else:
    #         print "新增公司失败，用户名被占用"
    #         self.click_close()
    #         return False

    def click_ok(self):
        '''确定'''
        self.click(self.ok_button)