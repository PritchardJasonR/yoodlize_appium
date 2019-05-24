import os
import unittest
import re
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
       
class search_by_price(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')
        
    def test_search_by_price(self):

        """
        Search by price function
        1. set price perams
        2. turn results into ints
        3. compare the results are in perams
        4. do for high, then low then high and low togeather
        """
        print('Driver Created')

        self.driver.implicitly_wait(1000)
        
        # Assert on home page not logged in
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
        self.driver.implicitly_wait(1000)
        """
        Search by price TC
        """
        # Test Searching by category
        print('Test Searching by category has STARTED')
        self.driver.find_element_by_xpath(home_search_btn).click()
        self.driver.implicitly_wait(1000)
        print('>>  selected search btn')

        # Assert user has navigated to search screen
        self.assertTrue(find_by_text(self, text= 'Near me'))
        print('>>  User is navigated to search page')

        # Navigate to advanced search page
        print('Navigate to advanced search page')
        self.driver.find_element_by_xpath(search_advanced_btn).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= search_adv_ident))
        print('>>  Advanced search options are displayed')
        
        # assert min value is set to 1
        print('assert min value is set to 1')
        min_value = self.driver.find_element_by_xpath(search_adv_price_min_indicator).text
        self.assertEqual(min_value, '1')
        print('>>  Min value is set to 1')

        # Lower Maximum price to $20
        print('set maximum value to 20')
        self.driver.swipe(start_x=950, start_y=1450, end_x=275, end_y=1450, duration=2300)
        self.driver.implicitly_wait(1000)
        max_value = self.driver.find_element_by_xpath(search_adv_price_max_indicator).text
        self.assertEqual(max_value, '20')
        print('>>  Max value is set to 20')

        # select filter save btn
        print('select filter save btn')
        self.driver.find_element_by_xpath(search_adv_save_all_filters).click()
        print('>>  filters Saved')

        # assert on results page with at least one result
        print('assert on results page with at least one result')
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= price_card1))
        self.driver.implicitly_wait(500)
        print('>>  At least on result is displayed')

        # run cust func for fun
        price_check = price_search_key(self)
        print(price_check)
        for price_ints in price_check:
            price_check.rstrip(str(["$","/day"]))
        print(price_ints)
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        # 
        print('')
        print('>>  ')

        







def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(search_by_price)
    unittest.TextTestRunner(verbosity=2).run(suite)