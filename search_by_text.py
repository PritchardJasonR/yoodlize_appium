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
       
class search_by_text(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')
        
    def test_search_by_text(self):
     
        """
        Search by text function
        """
        FULL_NAME = 'Test item1'
        PARTIAL = 'Test'
        CASE_SENSITIVE1 = 'ccoon'
        CASE_SENSITIVE2 = 'test rock'



        print('Driver Created')

        self.driver.implicitly_wait(1000)
        
        # Assert on home page not logged in
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
        print('Test Started')
        self.driver.implicitly_wait(1000)
        """
         Test Searching by text from home page not logged in
        """
        # Test Searching by text from home page not logged in
        print('Test Searching by text from home page not logged in')
        self.driver.find_element_by_xpath(home_search_bar).send_keys('Test Rock')
        self.driver.find_element_by_xpath(home_search_btn).click()
        self.driver.implicitly_wait(1000)
        print('>>  selected search btn')

        # Reviewing Results
        print('Reviewing Results')
        find_by_text(self, text='Test Rock')
        print(">>  searching from home screen currently is unreliable")

        # fill search bar
        print('fill search bar')
        self.driver.find_element_by_xpath(search_search_bar).send_keys(FULL_NAME)
        self.driver.find_element_by_xpath(search_search_btn).click()
        self.driver.find_element_by_xpath(search_search_bar).clear()
        self.driver.implicitly_wait(300)
        self.assertTrue(find_by_text(self, text= FULL_NAME))
        print('>>  At Least One Result Is Displayed With Exact Text That Was Searched For')

        # Search by partial text
        print('Search by partial text')
        search_bar(self, text= PARTIAL)
        self.driver.implicitly_wait(300)
        self.assertTrue(find_by_text(self, text= FULL_NAME))
        self.driver.implicitly_wait(300)
        find_by_text(self, text= 'rock')

        print('>> At Least One Result Is Displayed With partial Text That Was Searched For')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        # 
        print('')
        print('>> ')

        
        print('test complete')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(search_by_text)
    unittest.TextTestRunner(verbosity=2).run(suite)