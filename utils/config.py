# coding:utf-8
import os
from utils.file_reader import YamlReader

BASE_PATH = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
CONFIG_FILE = BASE_PATH + '\\config\\conf.yaml'
DATA_PATH = BASE_PATH + '\\data\\'
DRIVER_PATH = BASE_PATH + '\\drivers\\'
LOG_PATH = BASE_PATH + '\\report\\'


class Config:
    u'''读取配置'''
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)
