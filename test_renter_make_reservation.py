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

class renter_make_reservation(unittest.TestCase):
    def setUp(self):
        self.driver = des_cap(self, device_name= 'Android')

    def test_renter_make_reservation(self):
        EMAIL_RENTER = 'Z.timgranger@gmail.com'
        EMAIL_OWNER = 'Z.shelbyproctor@gmail.com'
        PASSWORD = '12345678Test'
        SEARCH_ITEM = 'Z_Test_item_Shelby'
        R_MSG1 = 'Renter_123'
        CC_INPUT = '4242424242424242'
        CVV = '444'
        """
        Pre-condition
        Renter login then searches for item then selects it
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
        self.assertTrue(visible_xpath_assert(self, element= rent_search_item))
        click_text(self, text = '40')
        self.driver.implicitly_wait(500)
        click_text(self, text= SEARCH_ITEM)
        print('>>  Found searched for item and selected it')

        # Assert use has navigated to items info page
        print('Assert use has navigated to items info page')
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= rent_item_ident))
        self.assertTrue(find_by_text(self, text= SEARCH_ITEM))
        print('>>  User has navigated to the item searched for`s information page')

        # select back btn
        print('select back btn')
        self.driver.find_element_by_xpath(rent_item_back_btn).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= search_search_bar))
        print('>>  back btn clicked')

        """
        begin test
        """

        # Re select searched for item
        print('Re select searched for item')
        self.assertTrue(visible_xpath_assert(self, element= rent_search_item))
        click_text(self, text = '40')
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= rent_item_ident))
        self.assertTrue(find_by_text(self, text= SEARCH_ITEM))
        print('>>  User has navigated to the item searched for`s information page')

        # select request btn
        print('select request btn')
        self.driver.find_element_by_xpath(rent_item_request_btn).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= rent_calendar_ident))
        self.driver.find_element_by_xpath(rent_calendar_next_month).click()
        print('>>  Request Btn clicked and navigated to calendar page')

        # select valid calendar date and click next
        print('select valid calendar date and click next')        
        select_calendar(self)
        print('>>  Calendar day selected')
        
        # Assert user has navigated to the expected screen
        print('Assert user has navigated to the expected screen')
        self.assertTrue(find_by_text(self, text= 'About Your Rental'))
        print('>>  User has navigated to message screen')

        # Input message to send and select next btn
        print('Input message to send and select next btn')
        self.driver.find_element_by_xpath(rent_msg_field).send_keys(R_MSG1)
        self.driver.find_element_by_xpath(rent_msg_nxt_btn).click()
        self.driver.implicitly_wait(1000)
        self.assertTrue(visible_xpath_assert(self, element= rent_payment_ident))
        print('>>  next btn clicked and on payment screen')

        # assert favorite card is visible select add card
        print('assert favorite card is visible select add card')
        self.assertTrue(visible_xpath_assert(self, element= rent_payment_fav_card))
        self.driver.find_element_by_xpath(rent_payment_add_card).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= rent_add_card_ident))
        print('>>  user selected add card and was navigated to add card page successfully')


        # Now select cancel
        print('Now select cancel')
        self.driver.find_element_by_xpath(rent_add_card_cancel_btn).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= rent_payment_ident))
        print('>>  cancel btn clicked and user navigated back to payment page')


        # now reselect add card
        print('now reselect add card')
        self.assertTrue(visible_xpath_assert(self, element= rent_payment_fav_card))
        self.driver.find_element_by_xpath(rent_payment_add_card).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= rent_add_card_ident))
        print('>>  user selected add card and was navigated to add card page successfully')

        # Add card name
        print('Add card')
        file = open(PATH("plus_one.txt"), 'r')
        counter = int(file.readline())+1
        file.close()
        counter_str = str(counter)
        file = open(PATH("plus_one.txt"), 'w')
        file.write(counter_str)
        file.close()
        self.driver.find_element_by_xpath(rent_add_card_name).send_keys(f'user name{counter}')
        print('>>  Added name')

        # add card number
        print('add card number and CVV')
        self.driver.find_element_by_xpath(rent_add_card_number).send_keys(CC_INPUT)
        self.driver.find_element_by_xpath(rent_add_card_cvv).send_keys(CVV)
        print('>>  number and cvv added')

        # set month and year
        print('set month and year')
        self.driver.find_element_by_xpath(rent_add_card_month_drop_down).click()
        click_text(self, text= 'July')
        self.driver.find_element_by_xpath(rent_add_card_year_drop_down).click()
        click_text(self, text= '2023')
        print('>>  added card input')

        # now clear name field and select save btn
        print('now clear name field and try to save')
        self.driver.find_element_by_xpath(rent_add_card_name).clear()
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_xpath(rent_add_card_add_btn).click()
        self.assertTrue(visible_xpath_assert(self, element= rent_add_card_name_required_msg))
        print('>>  Required msg displayed')

        # fill name field and clear cc number field and repeat
        print('fill name field and clear cc number field and repeat')
        self.driver.find_element_by_xpath(rent_add_card_name2).send_keys(f'user name{counter}')
        self.driver.find_element_by_xpath(rent_add_card_number2).clear()
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_xpath(rent_add_card_add_btn2).click()
        self.assertTrue(visible_xpath_assert(self, element= rent_add_card_number_required_msg))
        print('>>  number required msg displayed')

        # now fill cc field with letters
        print('now fill cc field with letters')
        self.driver.find_element_by_xpath(rent_add_card_number2).send_keys('abcdefghijklmnop')
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_xpath(rent_add_card_add_btn2).click()
        self.assertTrue(visible_xpath_assert(self, element= rent_add_card_number_invalid_msg))
        print('>>  invalid msg displayed')

        # now fill number field with valid input and delete cvv field
        print('now fill number field with valid input and delete cvv field')
        self.driver.find_element_by_xpath(rent_add_card_number2).clear()
        self.driver.find_element_by_xpath(rent_add_card_number2).send_keys(CC_INPUT)
        self.driver.find_element_by_xpath(rent_add_card_cvv2).clear()
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_xpath(rent_add_card_add_btn2).click()
        self.assertTrue(visible_xpath_assert(self, element= rent_add_card_cvv_required_msg))
        print('>>  cvv err message displayed')

        # fill cvv and save card
        print('fill cvv and save card')
        self.driver.find_element_by_xpath(rent_add_card_cvv2).clear()
        self.driver.find_element_by_xpath(rent_add_card_cvv2).send_keys(CVV)
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(500)
        self.driver.find_element_by_xpath(rent_add_card_add_btn2).click()
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element = rent_payment_ident))
        print('>>  user has completed adding new card')

        # now assert newcard was added and select it
        print('now assert newcard was added and select it')
        self.driver.implicitly_wait(1500)
        click_text(self, text= 'Select a different card')
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= rent_select_card_ident))
        self.driver.implicitly_wait(500)
        click_text(self, text= f'user name{counter}')
        print('>>  added card selected')

        # assert that created card is selected and click next
        print('assert that created card is selected and click next')
        self.assertTrue(find_by_text(self, text= f'user name{counter}'))
        click_text(self, text= 'Next')
        print('>>  added card is visible and next was clicked')

        # Assert user is on final page and select the next button
        print('Assert user is on final page and select the next button')
        self.assertTrue(visible_xpath_assert(self, element= rent_final_ident))
        click_text(self, text= 'Next')
        print('>>  User made it to final rent page and selected next button')

        # assert user made it to rental success page
        print('assert user made it to rental success page')
        self.assertTrue(visible_xpath_assert(self, element= rent_success_ident))

        # Now assert Owner recieved SMS notification
        print(' Now assert Owner recieved SMS notification')
        check_SMS(self)
        print('>>  SMS Was displayed as expected and back on Yoodlize app')

        # Logout and assert user is on home page
        print('Logout and assert user is on home page')
        log_out(self)
        self.driver.implicitly_wait(500)
        self.assertTrue(visible_xpath_assert(self, element= home_ident))
        print('>>  User is now logged out and on homepage')

        # Login as Owner
        print('Login as Owner')
        login(self, email= EMAIL_OWNER, password= PASSWORD)
        self.assertTrue(visible_xpath_assert(self, element= home_loggedin_ident))
        print('>>  Owner is now logged in')

        # Assert inbox has a notification indicator then navigate to inbox
        print('Assert inbox has a notification indicator then navigate to inbox')
        self.assertTrue(visible_xpath_assert(self, element= home_inbox_notification))
        self.driver.find_element_by_xpath(home_inbox).click()
        print('>>  New msg notification was displayed and user clicked to navigate to inbox')

        # assert inbox is displayed and select new notification
        print('assert inbox is displayed and select new notification')
        self.assertTrue(visible_xpath_assert(self, element= inbox_ident))
        self.driver.find_element_by_xpath(inbox_pending_notification).click()
        print('>> User selected new msg')

        # assert user was navigated to message screen reads msg and denys request
        print('assert user was navigated to message screen reads msg and denys request')
        self.assertTrue(visible_xpath_assert(self, element= inbox_msging_ident))
        msg_text = self.driver.find_element_by_xpath(inbox_msging_msg1).text
        self.assertEqual(msg_text, R_MSG1)
        self.driver.find_element_by_xpath(inbox_msging_deny).click()

        # assert user was navigated back to inbox main page
        print('assert user was navigated back to inbox main page')
        self.assertTrue(visible_xpath_assert(self, element= inbox_ident))
        print('>>  user is now back on inbox main page')

        # Refresh page and asser pending placeholder is not visible
        print('Refresh page and asser pending placeholder is not visible')
        self.driver.swipe(start_x=150, start_y=350, end_x=150, end_y=1800, duration=600)
        self.driver.implicitly_wait(500)
        self.assertFalse(visible_xpath_assert(self, element= inbox_pending_notification))
        print('Request was successfully denied')

        # Now Navigate to yahoo and verify email\notification the request was denyed
        denial_email(self)
        print('User is back on yoodlize app test is now complete')
        
        print('test complete')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(renter_make_reservation)
    unittest.TextTestRunner(verbosity=2).run(suite)