# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/6 18:35
@Auth ： 李江
@Company ：李江
@Function ：请输入模块功能描述
"""
import app
import requests
class LoginAPI():
    def __init__(self):
        self.getImgCode_url = app.BASE_URL +'/common/public/verifycode1/'
        self.getSendSms_url = app.BASE_URL +'/member/public/sendSms'

        #图片验证码请求接口
    def getImgCode(self,session,r):
        url = self.getImgCode_url + r
        response = session.get(url)
        return response


    #获取短信验证码

    def getSendSms(self,session,phone,imgVerifyCode):
        data = {"phone": phone,"imgVerifyCode": imgVerifyCode,"type": "reg"}
        response = session.post(self.getSendSms_url,data=data)
        return response
