import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from support.helper import data, helper_register

class Register(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://demowebshop.tricentis.com/"

    def test_register_with_valid_credential(self): #positive case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*helper_register.find_gender).click()
        driver.find_element(*helper_register.find_firstname).send_keys(data.first_name)
        driver.find_element(*helper_register.find_lastname).send_keys(data.last_name)
        driver.find_element(*helper_register.find_email).send_keys(data.valid_email)
        driver.find_element(*helper_register.find_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_repeat_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_button).click()

        success_message = driver.find_element(*helper_register.find_success_register).text
        self.assertIn(data.success_register, success_message)

    def test_register_with_registered_email(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)
        
        driver.find_element(*helper_register.find_gender).click()
        driver.find_element(*helper_register.find_firstname).send_keys(data.first_name)
        driver.find_element(*helper_register.find_lastname).send_keys(data.last_name)
        driver.find_element(*helper_register.find_email).send_keys(data.valid_email)
        driver.find_element(*helper_register.find_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_repeat_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_button).click()

        self.assertIn("/register", get_url1)

    def test_register_with_empty_gender(self): #positive case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)
        
        driver.find_element(*helper_register.find_firstname).send_keys(data.first_name)
        driver.find_element(*helper_register.find_lastname).send_keys(data.last_name)
        driver.find_element(*helper_register.find_email).send_keys("emptygendertesting1212@gmail.com")
        driver.find_element(*helper_register.find_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_repeat_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_button).click()

        success_message = driver.find_element(*helper_register.find_success_register).text
        self.assertIn(data.success_register, success_message)

    def test_register_with_empty_last_name(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*helper_register.find_gender).click()
        driver.find_element(*helper_register.find_firstname).send_keys(data.first_name)
        # driver.find_element(*helper_register.find_lastname).send_keys(data.last_name)
        driver.find_element(*helper_register.find_email).send_keys(data.valid_email)
        driver.find_element(*helper_register.find_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_repeat_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_button).click()

        error_message = driver.find_element(*helper_register.find_error_last).text
        self.assertIn(data.error_last_name, error_message)

    def test_register_with_invalid_email_format(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*helper_register.find_gender).click()
        driver.find_element(*helper_register.find_firstname).send_keys(data.first_name)
        driver.find_element(*helper_register.find_lastname).send_keys(data.last_name)
        driver.find_element(*helper_register.find_email).send_keys(data.invalid_email)
        driver.find_element(*helper_register.find_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_repeat_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_button).click()

        error_message = driver.find_element(*helper_register.find_error_email).text
        self.assertIn(data.error_email, error_message)

    def test_register_with_short_password(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*helper_register.find_gender).click()
        driver.find_element(*helper_register.find_firstname).send_keys(data.first_name)
        driver.find_element(*helper_register.find_lastname).send_keys(data.last_name)
        driver.find_element(*helper_register.find_email).send_keys(data.invalid_email)
        driver.find_element(*helper_register.find_password).send_keys(data.short_password)
        driver.find_element(*helper_register.find_repeat_password).send_keys(data.short_password)
        driver.find_element(*helper_register.find_button).click()

        error_message = driver.find_element(*helper_register.find_short_password).text
        self.assertIn(data.error_short_password, error_message)

    def test_register_with_mismatch_password(self): #negative case
        driver = self.driver
        driver.get(self.url)

        driver.find_element(By.CLASS_NAME, 'ico-register').click()
        get_url1 = driver.current_url
        self.assertIn("/register", get_url1)

        driver.find_element(*helper_register.find_gender).click()
        driver.find_element(*helper_register.find_firstname).send_keys(data.first_name)
        driver.find_element(*helper_register.find_lastname).send_keys(data.last_name)
        driver.find_element(*helper_register.find_email).send_keys(data.invalid_email)
        driver.find_element(*helper_register.find_password).send_keys(data.valid_password)
        driver.find_element(*helper_register.find_repeat_password).send_keys("mismatchpassword")
        driver.find_element(*helper_register.find_button).click()

        error_message = driver.find_element(*helper_register.find_mismatch_password).text
        self.assertIn(data.error_mismatch_password, error_message)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    