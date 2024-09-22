from selenium.webdriver.common.by import By

class helper_register():
    find_gender = (By.ID, 'gender-male')
    find_firstname = (By.ID, 'FirstName')
    find_lastname = (By.ID, 'LastName')
    find_email = (By.ID, 'Email')
    find_password = (By.ID, 'Password')
    find_repeat_password = (By.ID, 'ConfirmPassword')
    find_button = (By.ID, 'register-button')

    find_success_register = (By.CSS_SELECTOR, '.page-title h1')

    find_error_first = (By.CSS_SELECTOR, '[data-valmsg-for="FirstName"]')
    find_error_last = (By.CSS_SELECTOR, '[data-valmsg-for="LastName"]')
    find_error_email = (By.CSS_SELECTOR, '[data-valmsg-for="Email"]')
    find_short_password = (By.CSS_SELECTOR, '[data-valmsg-for="Password"]')
    find_mismatch_password = (By.CSS_SELECTOR, '[data-valmsg-for="ConfirmPassword"]')

class data():
    first_name = "David"
    last_name = "TAK Batch 7"
    empty_name = ""

    valid_email = "davidtak_register5@gmail.com"
    invalid_email = "david_testgmail.com"

    valid_password = "password123"
    short_password = "short"

    success_register = "Register"

    error_first_name = "First name is required."
    error_last_name = "Last name is required."
    error_email = "Wrong email"
    error_short_password = "The password should have at least 6 characters."
    error_mismatch_password = "The password and confirmation password do not match."
    
class login():
    login_button = (By.CSS_SELECTOR, '.buttons')
    header_links = (By.CSS_SELECTOR, '[.header-links ul li.account]')