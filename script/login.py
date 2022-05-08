# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/6 21:43
@Auth ： 李江
@Company ：李江
@Function ：请输入模块功能描述
"""

import unittest
import requests
from api.loginAPI import LoginAPI
import random

from utils import assert_utils


class login(unittest.TestCase):
    phone1 = '13760153292'
    imgCode='8888'
    def setUp(self) -> None:
        self.login_api = LoginAPI()
        self.session = requests.Session()

    def tearDown(self) -> None:
        self.session.close()

#获取注册图片验证码（随机小数）
    def test01_get_img_code_random_float(self):
        r = random.random()
        response = self.login_api.getImgCode(self.session,str(r))
        self.assertEqual(200,response.status_code)
#获取注册图片验证码（随机整数）
    def test02_get_img_code_random_int(self):
        r = random.randint(1000000,9999999)
        response = self.login_api.getImgCode(self.session,str(r))
        self.assertEqual(200,response.status_code)

#获取短信验证码成功
    def test03_get_sms_code(self):
        r = random.random()
        respones = self.login_api.getImgCode(self.session, str(r))
        self.assertEqual(200, respones.status_code)

        response = self.login_api.getSendSms(self.session,self.phone1,self.imgCode)
        assert_utils(self,response,200,200)