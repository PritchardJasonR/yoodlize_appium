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
       
class search_by_categories(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')
        
    def test_search_by_categories(self):
     
        """
        Search by categories function
        """
        print('Driver Created')

        self.driver.implicitly_wait(1000)
        
        # Assert on home page not logged in
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
        self.driver.implicitly_wait(1000)
        """
        Search by category TC
        """
        # Test Searching by category
        print('Test Searching by category has STARTED')
        self.driver.find_element_by_xpath(home_search_btn).click()
        self.driver.implicitly_wait(1000)
        print('>>  selected search btn')

        # Assert user has navigated to search screen
        self.assertTrue(find_by_text(self, text= 'Near me'))
        print('>>  User is navigated to search page')

        # select categories filter
        print('select categories filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        # select Business equipment filter
        self.driver.find_element_by_xpath(search_categories_business_equip).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
    

        # Electronics category filter
        print('Electronics category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        # select Business equipment filter
        self.driver.find_element_by_xpath(search_categories_eletronics).click()
        self.driver.implicitly_wait(300)
        if  not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
     
        # Recreational Vehicles category filter
        print('Recreational Vehicles category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        # select Recreational Vehicles filter
        self.driver.find_element_by_xpath(search_categories_rec_vehicles).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        
        # clothing category filter
        print('clothing category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        # select Clothing filter
        self.driver.find_element_by_xpath(search_categories_clothing).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        

        # Home and Kitchen category filter
        print('Home and Kitchen category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_home_n_kitchen).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        
        
        # Lawn and Garden category filter
        print('Lawn and Garden category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_lawn_n_garden).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        

        # Outdoor gear category filter
        print('Outdoor gear category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_outdoor_gear).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        

        # Party and wedding Equip
        print('Party and wedding Equip')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_party_n_wedding).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        

        # Venues category filter
        print('Venues category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_venues).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        

        # Local Experts category filter
        print('Local Experts category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_local_experts).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        

        # Expirences category filter
        print('Expirences category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_experiences).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        

        # Sporting Equip category filter
        print('Sporting Equip category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_sporting_equip).click()
        self.driver.implicitly_wait(300)
        if not self.assertTrue(visible_xpath_assert(self, element= search_card1)):
            print('>>  There were no results for category')
        else:
            print('>>  At Least One Result Is Displayed in the category')
        
        
        print('test complete as passed')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(search_by_categories)
    unittest.TextTestRunner(verbosity=2).run(suite)