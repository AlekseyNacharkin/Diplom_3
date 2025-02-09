import time

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium import webdriver
from Diplom_3.pages.login_page import LoginPage
from Diplom_3.pages.forgot_password_page import ForgotPasswordPage
from Diplom_3.pages.restore_password_page import RestorePasswordPage
from Diplom_3.pages.personal_account_page import PersonalAccountPage

class TestPersonalAccount:

    def test_opening_personal_account(self,get_user_value,driver):
        login_page = LoginPage(driver)
        login_page.get_url_page(LoginPage.login_url)
        email, password = get_user_value
        login_page.send_keys(LoginPage.email_field,email)
        login_page.send_keys(LoginPage.password_field,password)
        login_page.click(LoginPage.login_button)
        personal_account_page = PersonalAccountPage(driver)
        time.sleep(5)
        personal_account_page.wait_for_scroll_to_finish()
        personal_account_page.is_element_clickable(PersonalAccountPage.personal_account_button)
        personal_account_page.click(PersonalAccountPage.personal_account_button)
        personal_account_page.is_displayed(PersonalAccountPage.profile_button)
        assert driver.current_url == personal_account_page.personal_account_url