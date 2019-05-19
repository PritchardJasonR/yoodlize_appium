import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from tools.other_des_caps import des_cap
from tools.custom_functions import *
from tools.page_objects import *

# Returns abs path relative to this file instead of cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
       
class owner_list_item(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')
        
    def test_owner_list_item(self):
        EMAIL= 'Z.timgranger@gmail.com'
        PASSWORD = '12345678Test'
        title = 'Auto Rock1'
        description = 'This rock is posted automatically and should be deleted before anyone sees me!'
        cust_rules1 = 'Do Not Look At Me'
        cust_rules2 = 'I am ser1ous!'
        """
        List an item with 3 photos, check err messaging, and delete when completed
        """
        print('Driver Created')
        self.driver.implicitly_wait(1000)
        # Assert on home page not logged in
        self.assertTrue(self.driver.find_element_by_xpath(home_ident).is_displayed())
        print('Test Started')
        
        # Login to a previously created account
        login(self, email= EMAIL, password= PASSWORD)

        # select to list an item and assert user has navigated to appropriate page
        print('select to list an item and assert user has navigated to appropriate page')
        self.driver.find_element_by_xpath(home_add_listing).click()
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, list_home_ident), "Hi! Let's make use of your unused stuff."))

        # select back btn assert user is navigated appropriately
        print('select back btn assert user is navigated appropriately')
        self.driver.implicitly_wait(1000)
        sleep(1)
        TouchAction(self.driver).tap(x=65, y=145).perform()
        self.driver.implicitly_wait(1000)
        visible_xpath_assert(self, element= home_loggedin_ident)

        # select list item again
        print('select list item again')
        self.driver.find_element_by_xpath(home_add_listing).click()
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, list_home_ident), "Hi! Let's make use of your unused stuff."))
        self.driver.find_element_by_xpath(list_start_btn).click()
        
        # procees to begining listing an item process
        print('Asserting user navigated to First Page for Listing')
        visible_xpath_assert(self, element= list_page1_ident)
        self.assertTrue(EC.text_to_be_present_in_element((By.XPATH, list_page1_ident), "Great! Now let's describe your item."))

        # Set Title
        print('Setting Title')
        self.driver.find_element_by_xpath(list_page1_item_title).send_keys(title)

        # set description
        print('setting description')
        self.driver.find_element_by_xpath(list_page1_item_description).send_keys(description)

        # setting Category
        print('setting Category to electronics')
        self.driver.find_element_by_id(list_page1_category_drop).click()
        self.driver.implicitly_wait(1000)
        click_text(self, text= 'Electronics')

        # Now delete title to proc an err msg
        print('Now delete title and and verif next button non functional')
        self.driver.find_element_by_xpath(list_page1_item_title).clear()
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_xpath(list_page1_save_next_btn).click()

        # Assert user is not navigated away
        print('Assert user is not navigated away')
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_xpath(list_page1_ident).is_displayed()

        # Fill title field and delete description field and again select next btn
        print('Fill title field and delete description field and again select next btn')
        self.driver.find_element_by_xpath(list_page1_item_title).send_keys(title)
        self.driver.find_element_by_xpath(list_page1_item_description).clear()
        self.driver.find_element_by_xpath(list_page1_save_next_btn).click()

        # Assert user is not navigated away
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_xpath(list_page1_ident).is_displayed()

        # fill description and select next btn
        print('fill description and select next btn')
        self.driver.find_element_by_xpath(list_page1_item_description).send_keys(description)
        self.driver.find_element_by_xpath(list_page1_save_next_btn).click()


        print('')

        print('')

        print('')

        print('')

        print('')

        print('')

        print('')

        print('')

        print('')

        print('')

        print('')


        
        print('test complete')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(owner_list_item)
    unittest.TextTestRunner(verbosity=2).run(suite)