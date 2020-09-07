import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import time

class HomePageTest(unittest.TestCase):

    # setup 
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_wms_local(self):
        driver = self.driver
        driver.get("http://localhost:8060/rp/login")
        time.sleep(2)

        loginUserName = driver.find_element_by_id('loginUserName')
        loginUserName.clear()
        loginUserName.send_keys('super')

        loginPassword = driver.find_element_by_id('loginPassword')
        loginPassword.clear()
        loginPassword.send_keys('SUPER')

        loginButton = driver.find_element_by_id('loginButton')
        loginButton.click()
        time.sleep(20)

        driver.find_element_by_id('ext-comp-1017-btnIconEl').click()
        driver.find_element_by_link_text('INVENTORY').click()
        time.sleep(10)
    

    # close the window
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'test_wms'))