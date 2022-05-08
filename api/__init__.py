# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/6 15:16
@Auth ： 李江
@Company ：李江
@Function ：请输入模块功能描述
"""
from app import init_log_config
import logging


init_log_config()
logging.info('info')
logging.debug('debug')