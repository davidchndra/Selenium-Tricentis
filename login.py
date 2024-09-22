import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from support.helper import data, helper_register, login

class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com/"

    def test_login_with_valid_credential(self):
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-login').click()
        driver.find_element(*helper_register.find_email).send_keys(data.valid_email)
        driver.find_element(*helper_register.find_password).send_keys(data.valid_password)
        driver.find_element(*login.login_button).click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    