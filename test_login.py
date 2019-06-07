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

class login(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')
        
    def test_login(self):
        EMAIL= 'Z.TimGranger@gmail.com'
        PASSWORD1 = '12345678Test'
        PASSWORD2 = '1qwerty'

        print('Driver Created')
        self.driver.implicitly_wait(1000)
        # Assert on home page not logged in
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
        print('Test Started')
        self.driver.implicitly_wait(1000)
        
        # navigate to login page
        self.driver.find_element_by_xpath(home_login_btn).click()
        self.driver.implicitly_wait(1000)

        #assert user is on login page
        self.driver.find_element_by_xpath(login_ident).is_displayed()

        # Select Back Button to ensure back on login navigates back to home page
        self.driver.find_element_by_xpath(login_back_btn).click()
        self.driver.implicitly_wait(1000)
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())

        # navigate back to login page
        self.driver.find_element_by_xpath(home_login_btn).click()
        self.driver.implicitly_wait(1000)

        #assert user is on login page
        self.driver.find_element_by_xpath(login_ident).is_displayed()
        self.driver.implicitly_wait(1000)

        # enter valid email and incorrect password
        self.driver.find_element_by_xpath(login_email_field).send_keys(EMAIL)
        self.driver.find_element_by_xpath(login_password_field).send_keys(PASSWORD2)

        # click login
        self.driver.find_element_by_xpath(login_btn).click()
        self.driver.implicitly_wait(100)

        # Assert user has not navigate away from login page and error message is displayed with correct error message
        self.driver.find_element_by_xpath(login_ident).is_displayed()
        self.assertTrue(self.driver.find_element_by_xpath(login_ident).is_displayed())
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[3]'), 'Failed to log in'))
        self.driver.implicitly_wait(1000)

        # Clear password field and enter valid password
        self.driver.find_element_by_xpath(login_password_adj).clear()
        self.driver.find_element_by_xpath(login_password_adj).send_keys(PASSWORD1)
        self.driver.implicitly_wait(1000)

        # click login btn
        self.driver.find_element_by_xpath(login_btn2).click()

        # Assert user has been successfuly logged in
        self.driver.find_element_by_xpath(home_loggedin_ident)
        print('>>  User is now logged in')       
        
def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(login)
    unittest.TextTestRunner(verbosity=2).run(suite)