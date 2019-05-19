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
        business_equip_list = search_cards(self)
    

        # Electronics category filter
        print('Electronics category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        # select Electronics filter
        self.driver.find_element_by_xpath(search_categories_eletronics).click()
        self.driver.implicitly_wait(300)
        electronics_list = search_cards(self)
        if len(electronics_list) > 0:
            self.assertNotEqual(business_equip_list, electronics_list)
            print('>>  business and electonics returned different results')
        else:
            print('>>  Filter returned no results')
        
     
        # Recreational Vehicles category filter
        print('Recreational Vehicles category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        # select Recreational Vehicles filter
        self.driver.find_element_by_xpath(search_categories_rec_vehicles).click()
        self.driver.implicitly_wait(300)
        rec_veh = search_cards(self)
        if len(rec_veh) > 0:
            self.assertNotEqual(rec_veh ,business_equip_list)
            self.assertNotEqual(rec_veh, electronics_list)
            print('>>  Recreational Vehicles reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')
        
        # clothing category filter
        print('clothing category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        # select Clothing filter
        self.driver.find_element_by_xpath(search_categories_clothing).click()
        self.driver.implicitly_wait(300)
        cloth_list = search_cards(self)
        if len(cloth_list) > 0:
            self.assertNotEqual(cloth_list ,business_equip_list)
            self.assertNotEqual(cloth_list, electronics_list)
            self.assertNotEqual(cloth_list, rec_veh)
            print('>>  Clothing filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')
        

        # Home and Kitchen category filter
        print('Home and Kitchen category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_home_n_kitchen).click()
        self.driver.implicitly_wait(300)
        home_n_kitchen_list = search_cards(self)
        if len(home_n_kitchen_list) > 0:
            self.assertNotEqual(home_n_kitchen_list ,business_equip_list)
            self.assertNotEqual(home_n_kitchen_list, electronics_list)
            self.assertNotEqual(home_n_kitchen_list, rec_veh)
            self.assertNotEqual(home_n_kitchen_list, cloth_list)
            print('>>  Home and Kitchen filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')
        
        
        # Lawn and Garden category filter
        print('Lawn and Garden category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_lawn_n_garden).click()
        self.driver.implicitly_wait(300)
        lawn_n_garden_list = search_cards(self)
        if len(lawn_n_garden_list) > 0:
            self.assertNotEqual(lawn_n_garden_list ,business_equip_list)
            self.assertNotEqual(lawn_n_garden_list, electronics_list)
            self.assertNotEqual(lawn_n_garden_list, rec_veh)
            self.assertNotEqual(lawn_n_garden_list, cloth_list)
            self.assertNotEqual(lawn_n_garden_list, home_n_kitchen_list)
            print('>>  Clothing filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')
        

        # Outdoor gear category filter
        print('Outdoor gear category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_outdoor_gear).click()
        self.driver.implicitly_wait(300)
        outdoor_list = search_cards(self)
        if len(outdoor_list) > 0:
            self.assertNotEqual(outdoor_list ,business_equip_list)
            self.assertNotEqual(outdoor_list, electronics_list)
            self.assertNotEqual(outdoor_list, rec_veh)
            self.assertNotEqual(outdoor_list, cloth_list)
            self.assertNotEqual(outdoor_list, home_n_kitchen_list)
            self.assertNotEqual(outdoor_list, lawn_n_garden_list)
            print('>>  Outdoor gear filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')
        
        # Party and wedding Equip
        print('Party and wedding Equip')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_party_n_wedding).click()
        self.driver.implicitly_wait(300)
        party_n_wedding = search_cards(self)
        if len(party_n_wedding) > 0:
            self.assertNotEqual(party_n_wedding, business_equip_list)
            self.assertNotEqual(party_n_wedding, electronics_list)
            self.assertNotEqual(party_n_wedding, rec_veh)
            self.assertNotEqual(party_n_wedding, cloth_list)
            self.assertNotEqual(party_n_wedding, home_n_kitchen_list)
            self.assertNotEqual(party_n_wedding, lawn_n_garden_list)
            self.assertNotEqual(party_n_wedding, outdoor_list)
            print('>>  Party and wedding filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')
        

        # Venues category filter
        print('Venues category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_venues).click()
        self.driver.implicitly_wait(300)
        venues_list = search_cards(self)
        if len(venues_list) > 0:
            self.assertNotEqual(venues_list, business_equip_list)
            self.assertNotEqual(venues_list, electronics_list)
            self.assertNotEqual(venues_list, rec_veh)
            self.assertNotEqual(venues_list, cloth_list)
            self.assertNotEqual(venues_list, home_n_kitchen_list)
            self.assertNotEqual(venues_list, lawn_n_garden_list)
            self.assertNotEqual(venues_list, outdoor_list)
            self.assertNotEqual(venues_list, party_n_wedding)
            print('>>  Venues filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')
        

        # Local Experts category filter
        print('Local Experts category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_local_experts).click()
        self.driver.implicitly_wait(300)
        local_experts_list = search_cards(self)
        if len(local_experts_list) > 0:
            self.assertNotEqual(local_experts_list, business_equip_list)
            self.assertNotEqual(local_experts_list, electronics_list)
            self.assertNotEqual(local_experts_list, rec_veh)
            self.assertNotEqual(local_experts_list, cloth_list)
            self.assertNotEqual(local_experts_list, home_n_kitchen_list)
            self.assertNotEqual(local_experts_list, lawn_n_garden_list)
            self.assertNotEqual(local_experts_list, outdoor_list)
            self.assertNotEqual(local_experts_list, party_n_wedding)
            self.assertNotEqual(local_experts_list, venues_list)
            print('>>  Local Experts filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')

        # Expirences category filter
        print('Expirences category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_experiences).click()
        self.driver.implicitly_wait(300)
        expirences_list = search_cards(self)
        if len(expirences_list) > 0:
            self.assertNotEqual(expirences_list, business_equip_list)
            self.assertNotEqual(expirences_list, electronics_list)
            self.assertNotEqual(expirences_list, rec_veh)
            self.assertNotEqual(expirences_list, cloth_list)
            self.assertNotEqual(expirences_list, home_n_kitchen_list)
            self.assertNotEqual(expirences_list, lawn_n_garden_list)
            self.assertNotEqual(expirences_list, outdoor_list)
            self.assertNotEqual(expirences_list, party_n_wedding)
            self.assertNotEqual(expirences_list, venues_list)
            self.assertNotEqual(expirences_list, local_experts_list)
            print('>>  Expirences filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')


        # Sporting Equip category filter
        print('Sporting Equip category filter')
        self.driver.find_element_by_xpath(search_categories_btn).click()
        self.driver.implicitly_wait(300)
        self.assertTrue(visible_xpath_assert(self, element= search_categories_ident))
        self.driver.find_element_by_xpath(search_categories_sporting_equip).click()
        self.driver.implicitly_wait(300)
        sporting_equip_list = search_cards(self)
        if len(sporting_equip_list) > 0:
            self.assertNotEqual(sporting_equip_list, business_equip_list)
            self.assertNotEqual(sporting_equip_list, electronics_list)
            self.assertNotEqual(sporting_equip_list, rec_veh)
            self.assertNotEqual(sporting_equip_list, cloth_list)
            self.assertNotEqual(sporting_equip_list, home_n_kitchen_list)
            self.assertNotEqual(sporting_equip_list, lawn_n_garden_list)
            self.assertNotEqual(sporting_equip_list, outdoor_list)
            self.assertNotEqual(sporting_equip_list, party_n_wedding)
            self.assertNotEqual(sporting_equip_list, venues_list)
            self.assertNotEqual(sporting_equip_list, local_experts_list)
            self.assertNotEqual(sporting_equip_list, expirences_list)
            print('>>  Expirences filter reutnred different results from previous lists')
        else:
            print('>>  Filter returned no results')

        print(business_equip_list)
        print(electronics_list)
        print(rec_veh)
        print(lawn_n_garden_list)
        print(home_n_kitchen_list)
        print(sporting_equip_list)
        print(local_experts_list)
        print(venues_list)
        print(expirences_list)
        print(cloth_list)
        print(outdoor_list)
        print(party_n_wedding)

        
        print('test complete as passed')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(search_by_categories)
    unittest.TextTestRunner(verbosity=2).run(suite)