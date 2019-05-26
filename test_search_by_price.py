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

        # get list for prices
        print('getting list for prices')
        price_check = price_search_key(self)
        print(price_check)

        # convert list to ints and assert < 20 as set by filter
        print('convert list to ints and assert < 20 as set by filter')
        prices = [price_int.strip("$/day") for price_int in price_check]
        results = list(map(int, prices))
        for each in results:
            assert each <= 20      
        print('>>  no result was greater then $20 max limit set for price search ')

        # Now set max to $5
        print('Now set max to $5')
        self.driver.find_element_by_xpath(search_advanced_btn).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= search_adv_ident))
        min_value = self.driver.find_element_by_xpath(search_adv_price_min_indicator).text
        self.assertEqual(min_value, '1')
        print('>>  Min value is set to 1')
        
        print('setting maximum value to 5')
        self.driver.swipe(start_x=275, start_y=1450, end_x=149, end_y=1450, duration=1400)
        self.driver.implicitly_wait(1000)
        max_value = self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[19]').text
        self.assertEqual(max_value, '5')
        print('>>  Max value is set to 5')
        
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

        # get list for prices
        print('getting list for prices')
        price_check = price_search_key(self)
        print(price_check)

        # convert list to ints and assert < 20 as set by filter
        print('convert list to ints and assert < 20 as set by filter')
        prices = [price_int.strip("$/day") for price_int in price_check]
        results = list(map(int, prices))
        for each in results:
            assert each <= 5      
        print('>>  no result was greater then $5 max limit set for price search ')

        print('Now set max back to 100 and test min filter')
        self.driver.find_element_by_xpath(search_advanced_btn).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= search_adv_ident))
        min_value = self.driver.find_element_by_xpath(search_adv_price_min_indicator).text
        self.assertEqual(min_value, '1')
        print('>>  Min value is set to 1')
        
        print('setting maximum value to 100')
        self.driver.swipe(start_x=149, start_y=1450, end_x=959, end_y=1450, duration=1400)
        self.driver.implicitly_wait(1000)
        max_value = self.driver.find_element_by_xpath(search_adv_price_max_indicator).text
        self.assertEqual(max_value, '100')
        print('>>  Max value is set to 100')

        """
        now test min filter
        """
        # Now set min value to 90
        print('Now set min value to 90')
        self.driver.swipe(start_x=125, start_y=1450, end_x=883, end_y=1450, duration=1400)
        min_value = self.driver.find_element_by_xpath(search_adv_price_min_indicator).text
        self.assertEqual(min_value, '90')
        print('>>  min value is now set to 90')

        # select filter save btn
        print('select filter save btn')
        self.driver.find_element_by_xpath(search_adv_save_all_filters).click()
        print('>>  min filter Saved')

        # assert on results page with at least one result
        print('assert on results page with at least one result')
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= price_card1))
        self.driver.implicitly_wait(500)
        print('>>  At least on result is displayed')

        # get list for prices
        print('getting list for prices')
        price_check = price_search_key(self)
        print(price_check)

        # convert list to ints and assert 90 < 100 as set by filter
        print('convert list to ints and assert 100 < 90 as set by filter')
        prices = [price_int.strip("$/day") for price_int in price_check]
        results = list(map(int, prices))
        for each in results:
            assert each <= 100
            assert each >= 90     
        print('>>  no result was greater then $90 min limit set for price search and less than 100 for max ')

        # now set max to 90 aswell
        print('now set min and max to 40')
        self.driver.find_element_by_xpath(search_advanced_btn).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= search_adv_ident))
        min_value = self.driver.find_element_by_xpath(search_adv_price_min_indicator).text
        self.assertEqual(min_value, '90')
        print('>>  Min value is set to 90')
        
        print('setting minimum and  maximum value to 40')
        self.driver.swipe(start_x=883, start_y=1450, end_x=455, end_y=1450, duration=1500)
        self.driver.implicitly_wait(1000)
        self.driver.swipe(start_x=959, start_y=1450, end_x=415, end_y=1450, duration=1500)
        self.driver.implicitly_wait(1000)
        min_value = self.driver.find_element_by_xpath(search_adv_price_min_indicator).text
        self.assertEqual(min_value, '40')
        max_value = self.driver.find_element_by_xpath(search_adv_price_max_indicator).text
        self.assertEqual(max_value, '40')
        print('>>  Max and min value is set to 40')

        # select filter save btn
        print('select filter save btn')
        self.driver.find_element_by_xpath(search_adv_save_all_filters).click()
        print('>>  min filter Saved')

        # assert on results page with at least one result
        print('assert on results page with at least one result')
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= price_card1))
        self.driver.implicitly_wait(500)
        print('>>  At least on result is displayed')

        # get list for prices
        print('getting list for prices')
        price_check = price_search_key(self)
        print(price_check)

        # convert list to ints and assert <  as set by filter
        print('convert list to ints and assert 40 < 40  as set by filter')
        prices = [price_int.strip("$/day") for price_int in price_check]
        results = list(map(int, prices))
        for each in results:
            assert each == 40     
        print('>>  all results equal 40')

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