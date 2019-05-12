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

def log_out(self):
    print('logging out')
    self.driver.find_element_by_xpath(home_profile).click()
    self.driver.implicitly_wait(1000)

    # Assert successfully navigated to profile page and select log out
    self.driver.find_element_by_xpath(profile_ident)
    self.driver.find_element_by_xpath(profile_logout).click()
    self.driver.implicitly_wait(1000)
    self.driver.find_element_by_xpath(home_ident).is_displayed()

def do_email_verif(self):
    """
    @ Gets the randomized activity, and navigates to yahoo app
    @ Looks at e-mail gets the recoverycode and deletes the e-mail
    @ navigates back to legrand app with the recovery code
    """
    # Store App Activity and navigate to Yahoo app
    self.driver.implicitly_wait(1000)
    activity = self.driver.current_activity
    self.driver.hide_keyboard()
    self.driver.implicitly_wait(1000)
    self.driver.start_activity("com.yahoo.mobile.client.android.mail", "com.yahoo.mobile.client.android.mail.activity.MainActivity")
    print('Switching Application To Check Email Message and get the password recovery code!')
    
    #verify user has successfully navigated to yahoo application
    self.driver.implicitly_wait(5000)
    self.driver.hide_keyboard()
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_list').is_displayed())
    while not self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_item_unread_indicator').is_displayed():
        sleep(5)
        self.driver.swipe(start_x=750, start_y=1250, end_x=750, end_y=1750, duration=800)
    self.driver.implicitly_wait(60000)


    # Verify New Email exists and Grab the text from message
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_item_unread_indicator').is_displayed())
    email_text = self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_item_text').text

    # seperate the message to get the Recovery code 
    recov_code = email_text.split()[3]
    # print that the code was successfully identified 
    print(recov_code)

    # Long Press selector to delete message
    self.assertTrue(self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Multi-select checkbox. Not checked. For emails from Today"])[1]').is_displayed())
    self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Multi-select checkbox. Not checked. For emails from Today"])[1]').click()

    # Delete Message
    self.assertTrue(self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="More options"])[1]').is_displayed())
    self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="More options"])[1]').click()

    # Assert eMail Was deleted
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/empty_view_text').is_displayed())

    # go back to yoodlize app
    print(f'Navigating back to Legrand app your Recoverycode is {recov_code}')
    self.driver.start_activity('com.yoodlize', activity)

    return recov_code