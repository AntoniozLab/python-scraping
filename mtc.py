#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from PIL import Image
from time import sleep
import requests
from selenium.webdriver.chrome.options import Options

import sys
import os
from base64 import b64encode
from selenium.webdriver.common.by import By

from AntiCaptcha import Captcha

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

opts = Options()
opts.add_argument(
    'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/59.0.3071.115 Safari/537.36')

browser = webdriver.Chrome('./chromedriver.exe', chrome_options=opts)

url = 'https://scppp.mtc.gob.pe'
browser.get(url)

try:
    dni = open("./dni.txt").readline().strip()
    injectDNI = 'document.getElementById("txtNroDocumento").value="' + \
        dni + '";'
    browser.execute_script(injectDNI)

    # Get captcha
    sleep(1)
    captcha_image = "./captcha.png"
    captachBox = browser.find_element(By.ID, "imgCaptcha")
    location = captachBox.location
    size = captachBox.size
    browser.save_screenshot("screenshoot.png")

    x = location['x']
    y = location['y']
    w = size['width'] - 30
    h = size['height']
    width = x + w
    height = y + h

    im = Image.open('screenshoot.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(captcha_image)

    captchaResolver = Captcha('./captcha.png')
    captchaCode = captchaResolver.getCode()

    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    request = requests.get("https://scppp.mtc.gob.pe/", headers=headers)

    injectCaptcha = 'document.getElementById("txtCaptcha").value="' + \
        captchaCode + '";'

    # Ejecuto los scripts con selenium
    browser.execute_script(injectCaptcha)

    submit_button = browser.find_element(
        by=By.XPATH, value='//a[@id="ibtnBusqNroDoc"]')
    submit_button.click()

    # Extraigo la informacion detras del captcha
    sleep(1)
    content = browser.find_element(
        By.XPATH, '//span[@id="lblAdministrado"]')
    print(content.text)

except Exception as e:

    print(e)
