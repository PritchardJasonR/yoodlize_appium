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
       
class owner_list_item(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')
        
    def test_owner_list_item(self):
        EMAIL= 'Z.timgranger@gmail.com'
        PASSWORD = '12345678Test'
        title = 'Auto_Living_Room'
        description = 'This Living Room is posted automatically and should be deleted before anyone sees me!'
        PRICE = '40'
        RULES1 = 'Do Not Look At Me'
        RULES2 = 'I am ser1ous!'
        LABEL = 'Test Address'
        STREET = '123 Fake St.'
        CITY = 'Arcata'
        STATE = 'CA'
        ZIP = '95521'

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
        print('>> Description filled next was clicked')

        # assert photo ident is displayed and the text is as expected
        print('assert photo ident is displayed and the text is as expected')
        self.assertTrue(visible_xpath_assert(self, element= list_photo_ident))
        photo_ident_text = self.driver.find_element_by_xpath(list_photo_ident).text
        self.assertEqual(photo_ident_text, "Let's make it pretty add some photos!")
        print('>>  User navigated to correct page')

        # click photos and Add 1 photo, and take one with caMERA
        print('click photos and Add 2 photos, and take one with caMERA')
        self.driver.find_element_by_xpath(list_photo_photo_btn).click()
        self.driver.implicitly_wait(500)
        click_text(self, text= 'raccoon.png')

        print('>>  selected first photo')
       
        # now complete photo upload
        sleep(2)
        TouchAction(self.driver).tap(x=996, y=136).perform()
        self.driver.implicitly_wait(1000)
        self.assertTrue(visible_xpath_assert(self, element= list_photo_ident))
        print('>>  User is back on main photo page')

        # now add photo via camera
        print('now add photo via camera')
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_xpath(list_photo_camera).click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('Shutter').is_displayed()
        self.driver.find_element_by_accessibility_id('Shutter').click()
        self.driver.find_element_by_accessibility_id('Done').is_displayed()
        self.driver.find_element_by_accessibility_id('Done').click()
        sleep(3)
        TouchAction(self.driver).tap(x=996, y=136).perform()
        self.driver.implicitly_wait(1000)
        self.assertTrue(visible_xpath_assert(self, element= list_photo_ident))
       
        # Now delete first photo added and select next
        print('Now delete first photo added and select next')
        sleep(1)
        self.driver.find_element_by_xpath(list_photo1_delete).click()
        self.assertFalse(visible_xpath_assert(self, element= list_photo2_placeholder))
        self.driver.find_element_by_xpath(list_photo_save_next).click()
        print('Photo deleted and user navigated to next page')

        # Assert user is on address page and text is displayed
        print('Assert user is on address page and text is displayed')
        self.assertTrue(visible_xpath_assert(self, element= list_address_ident))
        address_ident_text = self.driver.find_element_by_xpath(list_address_ident).text
        print('>>  User is on address page')

        # Select preset address
        #-- Edge cases will be executed in a later test
        print('Select preset address')
        click_text(self, text= 'Tims House')
        self.driver.implicitly_wait(1000)
        self.driver.find_element_by_xpath(list_address_save).click()
        print('>>  preset address clicked')

        # assert user has navigated to price page
        print('assert user has navigated to price page')
        self.assertTrue(visible_xpath_assert(self, element= list_price_ident))
        self.driver.find_element_by_xpath(list_price_field).send_keys(PRICE)
        self.driver.find_element_by_xpath(list_price_next_btn).click()
        print('>>  price entered and next btn clicked')

        # Assert user navigated to correct page
        self.assertTrue(visible_xpath_assert(self, element= list_rules_ident))
        print('>>  user is on rules page')

        # add 2 rules
        print('add 2 rules')
        self.driver.find_element_by_xpath(list_rules_field).send_keys(RULES1)
        self.driver.find_element_by_xpath(list_rules_add).click()
        self.driver.find_element_by_xpath(list_rules_field).send_keys(RULES2)
        self.driver.find_element_by_xpath(list_rules_add).click()
        print('>>  2 rules added')

        # now assert the rules were added and displayed correctly
        print('now assert the rules were added and displayed correctly')
        rule1 = self.driver.find_element_by_xpath(rules_text1).text
        rule2 = self.driver.find_element_by_xpath(rules_text2).text
        self.assertEqual(rule1, RULES1)
        self.assertEqual(rule2, RULES2)
        self.driver.find_element_by_xpath(list_rules_save_btn).click()
        print('>>  rules are displayed correctly and next btn clicked')

        # assert user has navigated to the review page
        print('assert user has navigated to the review page')
        self.assertTrue(visible_xpath_assert(self, element= list_review_ident))
        print('>>  user is on correct page')

        # Assert information entered is now displayed
        print('Assert information entered is now displayed')
        review_title = self.driver.find_element_by_xpath(list_review_title).text
        review_price = self.driver.find_element_by_xpath(list_review_price).text
        review_description = self.driver.find_element_by_xpath(list_review_description).text
        review_rule1 = self.driver.find_element_by_xpath(list_review_rules1).text
        review_rule2 = self.driver.find_element_by_xpath(list_review_rules2).text
        self.assertTrue(visible_xpath_assert(self, element= list_review_title))
        self.assertEqual(review_price, f'${PRICE}.00 per day')
        self.assertEqual(review_description, description)
        self.assertEqual(review_rule1, f'• {RULES1}')
        self.assertEqual(review_rule2, f'• {RULES2}')
        

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

        
        print('test complete')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(owner_list_item)
    unittest.TextTestRunner(verbosity=2).run(suite)