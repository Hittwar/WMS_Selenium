#Libraries import

import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import time

# Testing Set
class HomePageTest(unittest.TestCase):

    # setup driver
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_wms_local(self):
        driver = self.driver
        #Web Service to test
        driver.get("http://localhost:8060/rp/login")
        time.sleep(2)

        #field ID for user
        loginUserName = driver.find_element_by_id('loginUserName')
        loginUserName.clear()
        loginUserName.send_keys('super')

        #field ID for Password
        loginPassword = driver.find_element_by_id('loginPassword')
        loginPassword.clear()
        loginPassword.send_keys('SUPER')

        #field ID for button
        loginButton = driver.find_element_by_id('loginButton')
        loginButton.click()
        time.sleep(20)

        #element ID for Menu 
        driver.find_element_by_id('ext-comp-1017-btnIconEl').click()
        #element ID with name Inventory
        driver.find_element_by_link_text('INVENTORY').click()
        time.sleep(10)
    

    # close the window
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'test_wms'))