# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/6 15:17
@Auth ： 李江
@Company ：李江
@Function ：请输入模块功能描述
"""
import logging
from logging import handlers
import os,time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL="http://user-p2p-test.itheima.net"
#BASE_URL = "http://user-p2p-test.itheima.net"
#初始化日志配置
def init_log_config():
    #1、初始化日志对象
    logger = logging.getLogger()
    #2、设置日志级别
    logger.setLevel(logging.INFO)
    #3、创建控制台日志处理器和文件日志处理器
    sh = logging.StreamHandler()

    logfile = BASE_DIR + os.sep + "log" + os.sep + "p2p.log"
    fh = logging.handlers.TimedRotatingFileHandler(logfile,when='M',interval=5,backupCount=5,encoding='UTF-8')
    #4、设置日志格式，创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    #5、将格式化器设置到日志器中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    #6、将日志处理器添加到日志对象
    logger.addHandler(sh)
    logger.addHandler(fh)