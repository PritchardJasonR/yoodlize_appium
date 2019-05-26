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

    def test_message_back_n_forth(self):
        EMAIL_RENTER = 'Z.timgranger@gmail.com'
        EMAIL_OWNER = 'Z.ShelbyProctor@gmail.com'
        PASSWORD = '12345678Test'
        SEARCH_ITEM = 'Auto Rock1'
        R_MSG1 = 'Renter_123'
        R_MSG2 = 'Renter_321'
        O_MSG1 = 'Owner_123'
        O_MSG2 = 'Owner_321'
        """
        first. renter login then message an items owner
        """
        print('Driver Created')
        self.driver.implicitly_wait(1000)
        
        # Assert on home page not logged in
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
        print('Test Started')
        
        # Login to a previously created account
        print('Logging in to renter account')
        login(self, email= EMAIL_RENTER, password= PASSWORD)

        # Assert user is now logged in
        self.assertTrue(visible_xpath_assert(self, element= home_loggedin_ident))
        print('Renter is logged in')

        # Navigate to the browse page and search for item user is considering renting
        print('Navigate to the browse page and search for item user is considering renting')
        self.driver.find_element_by_xpath(home_search_btn).click()
        self.driver.implicitly_wait(1000)
        print('>>  selected search btn')

        # Assert User is on Search Page
        self.assertTrue(visible_xpath_assert(self, element= search_search_bar))
        print('>>  User is on search page')

        # now search for item by text
        self.driver.find_element_by_xpath(search_search_bar).send_keys(SEARCH_ITEM)
        self.driver.find_element_by_xpath(search_search_btn).click()
        self.driver.implicitly_wait(500)
        print('>>  Searching for item')

        # looking for result
        self.assertTrue(find_by_text(self, text= SEARCH_ITEM))
        click_text(self, text = SEARCH_ITEM)
        print('>>  Found searched for item and selected it')


        print('test complete')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(create_account)
    unittest.TextTestRunner(verbosity=2).run(suite)