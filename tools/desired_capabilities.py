import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

def des_cap(self, device_name):
     
    PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
    desired_caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "deviceName": f'{device_name}',
    "app": PATH('..\\app\\yoodlize.apk'),
    "appPackage": "com.yoodlize.test",
    "appWaitActivity": "*",
    "autoGrantPermissions": "true"
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5000)

    return driver
