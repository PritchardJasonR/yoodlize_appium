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
        
        make_reservation(self)

        print('test complete')

def takeDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(create_account)
    unittest.TextTestRunner(verbosity=2).run(suite)