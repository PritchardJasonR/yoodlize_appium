import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

def click_text(self, text):
    self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).click()

def find_by_text(self, text):
    self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).is_displayed()

def visible_xpath_assert(self, element):        
    self.driver.implicitly_wait(1)
    if not self.driver.find_elements(By.XPATH, element):
        print('Element is not displayed')
    else:
        print('Element is displayed')

def visible_accessibility_id_assert(self, element):        
    self.driver.implicitly_wait(1)
    if not self.driver.find_elements(MobileBy.ACCESSIBILITY_ID, element):
        print('Element is not displayed')
    else:
        print('Element is displayed')