# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/6 15:18
@Auth ： 李江
@Company ：李江
@Function ：请输入模块功能描述
"""

def assert_utils(self,response,status_code,status):
    self.assertEqual(status_code,response.status_code)
    self.assertEqual(status,response.json().get("status"))