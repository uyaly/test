# coding:utf-8
import os
from utils.file_reader import YamlReader
from utils.file_reader import ExcelUtil
import xlrd

BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
CONFIG_FILE = BASE_PATH + '\\config\\conf.yaml'
DATA_FILE = BASE_PATH + '\\data\\testdata.xlsx'
DRIVER_PATH = BASE_PATH + '\\drivers\\'
LOG_PATH = BASE_PATH + '\\report\\'
sheetName = "original"

class Config:
    u'''读取配置'''
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)

class Data:
    u'''读取数据'''
    def __init__(self):
        # self.data = ExcelUtil(data).data
        self.data = xlrd.open_workbook(DATA_FILE)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    # def get(self, element, index=0):
    #     return self.data[index].get(element)

    def get(self, element, index=0):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
                return r