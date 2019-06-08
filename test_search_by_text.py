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
        FULL_NAME = 'Z_Test_item_Shelby'
        PARTIAL1 = 'Z_Test'
        partial_lowercase = 'est_item'
        full_lowercase = 'z_test_item2'
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
        self.driver.find_element_by_xpath(home_search_bar).send_keys('Z_Test_item_Shelby')
        self.driver.implicitly_wait(300)
   
        # Reviewing Results
        print('Reviewing Results')
        find_by_text(self, text='Z_Test_item_Shelby')
        self.driver.find_element_by_xpath(home_search_btn2).click()
        print(">>  Item searched for is displayed")

        # fill search bar
        print('fill search bar')
        self.driver.find_element_by_xpath(search_search_bar).send_keys(FULL_NAME)
        self.driver.find_element_by_xpath(search_search_btn).click()
        slay_list = search_cards(self)
        self.driver.implicitly_wait(300)
        print(slay_list)
        self.assertTrue(search_results(self, text= FULL_NAME, results_in_list= slay_list))
        self.assertTrue(find_by_text(self, text= FULL_NAME))
        print('>>  At Least One Result Is Displayed With Exact Text That Was Searched For')
        
        # Search by partial text
        print('Search by partial text')
        search_bar(self, text= PARTIAL1)
        self.driver.implicitly_wait(300)
        play_list = search_cards(self)
        print(play_list)
        self.driver.implicitly_wait(300)
        self.assertTrue(search_results(self, text= PARTIAL1, results_in_list= play_list))
        
        print('>> At Least One Result Is Displayed With partial Text That Was Searched For')

        # search by partial lower case
        print('search by partial lower case')
        search_bar(self, text= partial_lowercase)
        self.driver.implicitly_wait(300)
        play_list = search_cards(self)
        print(play_list)
        self.driver.implicitly_wait(300)
        self.assertTrue(search_results(self, text= partial_lowercase, results_in_list= play_list))
        print('>> partial_lowercase results found ')

        # Full Lower Case Looking for single result
        print('Full Lower Case Looking for single result')
        search_bar(self, text= full_lowercase)
        self.driver.implicitly_wait(300)
        play_list = search_cards(self)
        print(play_list)
        self.driver.implicitly_wait(300)
        self.assertEqual(len(play_list), 1)
        print('>> only one result was found ')

        print('test complete as passed')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(search_by_text)
    unittest.TextTestRunner(verbosity=2).run(suite)