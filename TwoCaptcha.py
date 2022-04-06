#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from twocaptcha import TwoCaptcha


class Captcha:

    token = open('./token.txt').readline().strip()
    solver = TwoCaptcha(os.getenv('APIKEY_2CAPTCHA', token))

    def __init__(self, captcha_image_path):
        self.captcha_image_path = captcha_image_path

    # code
    def getCode(self):
        captachResult = self.solver.normal(self.captcha_image_path)
        captchaCode = captachResult['code']
        return captchaCode

    # saludo
    def hola(self):
        print("hola")
