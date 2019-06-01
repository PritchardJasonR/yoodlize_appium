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
    self.driver.find_element_by_xpath(profile_ident).is_displayed()
    click_text(self, text= 'Sign Out')
    self.driver.implicitly_wait(1000)
    self.driver.find_element_by_xpath(home_ident).is_displayed()

def denial_email(self):
    """
    @ Gets the randomized activity, and navigates to yahoo app
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
    i = 1
    while visible_xpath_assert(self, element= '//android.widget.TextView[@content-desc="Subject. Your reservation request was declined by the owner. Double tap to open, double-tap and hold to select"]') == False:
        sleep(3)
        self.driver.swipe(start_x=750, start_y=1250, end_x=750, end_y=1750, duration=800)
        print(f'swipe{i}')
        i+1
    self.driver.implicitly_wait(60000)


    # Verify New Email exists and Grab the text from message
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/mail_item_unread_indicator').is_displayed())
    sent_text = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Subject. Your reservation request was sent to the owner. Double tap to open, double-tap and hold to select"]').text
    denial_text = self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Subject. Your reservation request was declined by the owner. Double tap to open, double-tap and hold to select"]').text

    #assert Email is notifing user that request was denyed
    self.assertEqual(sent_text, 'Your reservation request was sent to the owner')
    self.assertEqual(denial_text, 'Your reservation request was declined by the owner')

    # Long Press selector to delete message
    self.assertTrue(self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Multi-select checkbox. Not checked. For emails from Today"])[1]').is_displayed())
    self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="Multi-select checkbox. Not checked. For emails from Today"])[1]').click()

    # Delete Message
    self.assertTrue(self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="More options"])[1]').is_displayed())
    self.driver.find_element_by_xpath('(//android.widget.ImageView[@content-desc="More options"])[1]').click()

    # Assert eMail Was deleted
    self.assertTrue(self.driver.find_element_by_id('com.yahoo.mobile.client.android.mail:id/empty_view_text').is_displayed())

    # go back to yoodlize app
    print('Navigating back to yoodlize app Denial email was displayed as expected')
    self.driver.start_activity('com.yoodlize.test', activity)


def price_search_key(self):
    self.driver.implicitly_wait(5000)
    key_list = []
    row1xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[1]/android.view.View['
    row2xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[6]/android.view.View/android.view.View/android.view.View[2]/android.view.View['
    xpathend = ']/android.view.View[1]/android.view.View[2]/android.view.View'
    for index in range(1, 50):
        path1 = f"{row1xpath}{index}{xpathend}"
        path2 = f"{row2xpath}{index}{xpathend}"
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

def select_calendar(self):
            i = 1
            path = f"{calendar_days}{i}{calendar_days_end}"
            while visible_xpath_assert(self, element= path) == True:
                self.driver.implicitly_wait(10)
                self.driver.find_element_by_xpath(path).click()
                i+1
                self.driver.find_element_by_xpath(rent_calendar_next_btn).click()
                if i == 32:
                    self.driver.find_element_by_xpath(rent_calendar_next_month).click()
                    i = 1
                elif self.assertTrue(find_by_text(self, text= 'About Your Rental')):
                    break

def check_SMS(self):
    # Navigate to SMS application
    self.driver.implicitly_wait(1000)
    SEARCH_ITEM = 'Z_Test_item_Shelby'
    activity = self.driver.current_activity
    self.driver.start_activity("com.adhoclabs.burner", ".BurnerMainDrawerActivity")
    print('Switching Application To Check SMS Message!')

    #Assert User Successfully Navigated to App HomePage 
    self.assertTrue(self.driver.find_element_by_id('com.adhoclabs.burner:id/main_content').is_displayed())

    # Identify New Message Notification and click
    new_msg = self.driver.find_element_by_id('com.adhoclabs.burner:id/call_status')
    self.assertTrue(new_msg.is_displayed())

    # Read Message
    msg = self.driver.find_element_by_id('com.adhoclabs.burner:id/call_status')

    # Grab the text from message
    msg_text = self.driver.find_element_by_id('com.adhoclabs.burner:id/call_status').text
    
    self.assertEqual(msg_text, f'Yoodlize: Someone would like to rent your {SEARCH_ITEM}')

    # Long Press selector to delete message
    actions = TouchAction(self.driver)
    actions.long_press(msg)
    actions.perform()

    # Actually Delete message
    delte_msg = self.driver.find_element_by_id('com.adhoclabs.burner:id/buttonDefaultPositive')
    self.assertTrue(delte_msg.is_displayed())
    delte_msg.click()

    # assert the message was successfully deleted
    self.assertTrue(EC.invisibility_of_element_located((By.ID, 'com.adhoclabs.burner:id/call_status')))
    print('Message Successfully Deleted!')

    print(f'Navigating back to Yoodlize app')
    self.driver.start_activity('com.yoodlize.test', activity)