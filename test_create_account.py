import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from tools.desired_capabilities import des_cap
from tools.custom_functions import *
from tools.page_objects import *

# Returns abs path relative to this file instead of cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class create_account(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')
        
    def test_create_account(self):
        EMAIL= 'Z.TimGrang@gmail.gov'
        PASSWORD1 = '12345678Test'
        PASSWORD2 = '12345678Test'
        FNAME = 'Tim'
        LNAME = 'Granger'
        PHONE = '8018450809'

        print('Driver Created')

        self.driver.implicitly_wait(1000)
        # Assert on home page not logged in
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
        print('Test Started')
        self.driver.implicitly_wait(1000)
        
        # navigate to create account page by way of "Register" button
        self.driver.find_element_by_xpath(home_register_btn).click()
        self.driver.implicitly_wait(1000)

        # assert user is on create account page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()

        # Select Back Button to ensure back on login navigates back to home page
        self.driver.find_element_by_xpath(create_back_btn).click()
        self.driver.implicitly_wait(1000)
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())

        # navigate back to create account page by way of "Register" button
        self.driver.find_element_by_xpath(home_register_btn).click()
        self.driver.implicitly_wait(1000)

        #assert user is on create account page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # enter valid info for all fields
        self.driver.find_element_by_xpath(create_email_field).send_keys(EMAIL)
        self.driver.find_element_by_xpath(create_password_field).send_keys(PASSWORD1)
        self.driver.find_element_by_xpath(create_re_password_field).send_keys('aaaa')
        self.driver.fine_element_by_xpath(create_first_name_field)
        self.driver.fine_element_by_xpath(create_last_name_field)

        # click create btn
        self.driver.find_element_by_xpath(create_account_btn).click()
        self.driver.implicitly_wait(100)

        # assert error message is displayed
        self.assertTrue(self.driver.find_elements_by_id(create_err_popup).is_displayed())
        self.assertTrue(EC.text_to_be_present_in_element((By.ID,'android:id/message'), 'Passwords must match'))
        self.driver.find_element_by_id(create_popup_ok_btn).click()

        # Assert user has not navigated away from creation page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # Clear password field and enter valid password
        self.driver.find_element_by_xpath(create_re_password_field).clear()
        self.driver.find_element_by_xpath(create_re_password_field).send_keys(PASSWORD2)

        # click create btn
        self.driver.find_element_by_xpath(create_account_btn).click()
        self.driver.implicitly_wait(100)

        # assert age error message is displayed
        self.assertTrue(self.driver.find_elements_by_id(create_err_popup).is_displayed())
        self.assertTrue(EC.text_to_be_present_in_element((By.ID,'android:id/message'), 'Please verify your age'))
        self.driver.find_element_by_id(create_popup_ok_btn).click()

        # Assert user has not navigated away from creation page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # click i'm 18 btn
        self.driver.find_element_by_xpath(create_im_18).click()

        # clear email and enter invalid email field
        self.driver.find_element_by_xpath(create_email_field).clear()
        self.driver.find_element_by_xpath(create_email_field).send_keys('Z.timgranger#gmail..com')

        # click create btn
        self.driver.find_element_by_xpath(create_account_btn).click()
        self.driver.implicitly_wait(100)

        # assert email error message is displayed
        self.assertTrue(self.driver.find_elements_by_id(create_err_popup).is_displayed())
        self.assertTrue(EC.text_to_be_present_in_element((By.ID,'android:id/message'), 'Please enter a valid email address.'))
        self.driver.find_element_by_id(create_popup_ok_btn).click()

        # Assert user has not navigated away from creation page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # clear email and enter valid email field
        self.driver.find_element_by_xpath(create_email_field).clear()
        self.driver.find_element_by_xpath(create_email_field).send_keys(EMAIL)

        # clear First Name and select create
        self.driver.find_element_by_xpath(create_first_name_field).clear()
        self.driver.find_element_by_xpath(create_account_btn).click()
        self.driver.implicitly_wait(100)

        # assert first name error message is displayed
        self.assertTrue(self.driver.find_elements_by_id(create_err_popup).is_displayed())
        self.assertTrue(EC.text_to_be_present_in_element((By.ID,'android:id/message'), 'Please enter your first name.'))
        self.driver.find_element_by_id(create_popup_ok_btn).click()

        # Assert user has not navigated away from creation page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # fill first name with Valid input and clear last name
        self.driver.find_element_by_xpath(create_first_name_field).send_keys(FNAME)
        self.driver.find_element_by_xpath(create_last_name_field).clear()
        self.driver.find_element_by_xpath(create_account_btn).click()
        self.driver.implicitly_wait(100)

        # assert last name error message is displayed
        self.assertTrue(self.driver.find_elements_by_id(create_err_popup).is_displayed())
        self.assertTrue(EC.text_to_be_present_in_element((By.ID,'android:id/message'), 'Please enter your last name.'))
        self.driver.find_element_by_id(create_popup_ok_btn).click()

        # Assert user has not navigated away from creation page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # fill last name with Valid input and clear password
        self.driver.find_element_by_xpath(create_last_name_field).send_keys(LNAME)
        self.driver.find_element_by_xpath(create_password_field).clear()
        self.driver.find_element_by_xpath(create_account_btn).click()
        self.driver.implicitly_wait(100)

        # assert password error message is displayed
        self.assertTrue(self.driver.find_elements_by_id(create_err_popup).is_displayed())
        self.assertTrue(EC.text_to_be_present_in_element((By.ID,'android:id/message'), 'Password must be at least 8 characters.'))
        self.driver.find_element_by_id(create_popup_ok_btn).click()

        # Assert user has not navigated away from creation page
        self.driver.find_element_by_xpath(create_account_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # fill password field with Valid input complete creation
        self.driver.find_element_by_xpath(create_password_field).send_keys(PASSWORD1)
        self.driver.find_element_by_xpath(create_account_btn).click()
        self.driver.implicitly_wait(100)

        # skip Onboarding.
        find_by_text(self, text= 'Add your picture')
        click_text(self, text= "I'll do this later")

        # assert user has been navigated to next page with warning msg
        find_by_text(self, 'Welcome to')
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[9]'), "Before you can list or rent items, we need to verify your identity. Let's get started!"))
        
        # navigate to next screen by clicking next
        click_text(self, text= 'Next')

        # Assert user has been navigated to next screen to link email
        find_by_text(self, text= 'Verify your email')

        # select the I'll do this later
        click_text(self, text= "I'll do this later")
        
        # Assert user has been navigated to photo page
        find_by_text(self, text= 'Add your picture')

        # Navigate to next page to accept terms
        find_by_text(self, text= 'Accept our terms')
        click_text(self, text= 'Next')

        #assert user did not leave page until terms are accepted
        find_by_text('Read Terms of Service')

        #select to accept the terms
        self.driver.find_element_by_xpath(onboard_accept_terms_box).click()

        # Assert user has navigated to last onboarding page
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[8]'), "Congrats on joining the Yoodlize community. We’ve got a quick tutorial to show you how it works."))
        
        # finalize onboarding process
        click_text(self, text= "I'll do this later")

        # assert user has been taken to login page
        self.driver.find_element_by_xpath(login_ident).is_displayed()
        
        print('test complete')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(create_account)
    unittest.TextTestRunner(verbosity=2).run(suite)