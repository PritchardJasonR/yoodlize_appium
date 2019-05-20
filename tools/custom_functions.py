import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from tools.page_objects import *

def click_text(self, text):
    self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).click()

def find_by_text(self, text):
    self.driver.implicitly_wait(1)
    if not self.driver.find_element_by_xpath('//*[contains(@text, "{}")]'.format(text)).is_displayed():
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def visible_xpath_assert(self, element):        
    self.driver.implicitly_wait(1)
    if not self.driver.find_elements(By.XPATH, element):
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def visible_accessibility_id_assert(self, element):        
    self.driver.implicitly_wait(1)
    if not self.driver.find_elements(MobileBy.ACCESSIBILITY_ID, element):
        print('Element is not displayed')
        return False
    else:
        print('Element is displayed')
        return True

def login(self, email, password):
    # Assert on home page not logged in
    self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
    print('User is not logged in')
    self.driver.implicitly_wait(1000)
    
    # navigate to login page
    self.driver.find_element_by_xpath(home_login_btn).click()
    self.driver.implicitly_wait(1000)

    #assert user is on login page
    self.driver.find_element_by_xpath(login_ident).is_displayed()

    # enter valid email and incorrect password
    self.driver.find_element_by_xpath(login_email_field).send_keys(email)
    self.driver.find_element_by_xpath(login_password_field).send_keys(password)

    # click login
    self.driver.find_element_by_xpath(login_btn).click()
    self.driver.implicitly_wait(100)

    visible_xpath_assert(self, element= home_loggedin_ident)
    print('user is now logged in')

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

def price_search_key(self):
    self.driver.implicitly_wait(5000)
    key_list = []
    row1xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[1]/android.view.View['
    row2xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[2]/android.view.View['
    xpathend = ']/android.view.View[1]/android.view.View[2]/android.view.View'
    for index in range(1, 50):
        path1 = f"{row1xpath}{index}{xpathend}"
        path2 = f"{row2xpath}{index}{xpathend}"
        path3 = f"{row3xpath}{index}{xpathend}"
        path4 = f"{row4xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path1)) > 0:
            self.driver.implicitly_wait(1)
            key_list.append(self.driver.find_element_by_xpath(f"{row1xpath}{index}{xpathend}").text)
            if len(self.driver.find_elements(By.XPATH, path2)) > 0:
                key_list.append(self.driver.find_element_by_xpath(f"{row2xpath}{index}{xpathend}").text)           
        else:
            break
    return key_list

def search_cards(self):
    self.driver.implicitly_wait(5000)
    search_list = []
    row1xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[1]/android.view.View['
    row2xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[2]/android.view.View['
    xpathend = ']/android.view.View[3]'
    for index in range(1, 50):
        path1 = f"{row1xpath}{index}{xpathend}"
        path2 = f"{row2xpath}{index}{xpathend}"
        self.driver.implicitly_wait(1)
        if len(self.driver.find_elements(By.XPATH, path1)) > 0:
            self.driver.implicitly_wait(1)
            search_list.append(self.driver.find_element_by_xpath(f"{row1xpath}{index}{xpathend}").text)
            if len(self.driver.find_elements(By.XPATH, path2)) > 0:
                search_list.append(self.driver.find_element_by_xpath(f"{row2xpath}{index}{xpathend}").text)   
        else:
            break
    return search_list

def search_results(self, text, results_in_list):
    if any(text in s for s in results_in_list):
        return True
    else:
        return False

def search_bar(self, text):
    self.driver.find_element_by_xpath(search_search_bar).send_keys(text)
    self.driver.find_element_by_xpath(search_search_btn).click()