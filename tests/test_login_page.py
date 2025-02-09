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

class TestLoginPage():

    def test_show_user_password(self,driver):
        login_page = LoginPage(driver)
        login_page.get_url_page(LoginPage.login_url)
        login_page.send_keys(LoginPage.email_field,"Алексей")
        login_page.send_keys(LoginPage.password_field,"123456")
        login_page.click(LoginPage.email_field)
        login_page.click(LoginPage.eyes_button)
        assert login_page.is_displayed(LoginPage.parent_element_eyes_button_in_active_state)

    def test_restore_password(self,driver):
        login_page = LoginPage(driver)
        login_page.get_url_page(LoginPage.login_url)
        login_page.click(LoginPage.restore_password_button)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.click(ForgotPasswordPage.email_field_in_default_state)
        forgot_password_page.send_keys(ForgotPasswordPage.email_field_in_active_state,"ASDFVBXCVXCVG@GMAIL.COM")
        forgot_password_page.click(ForgotPasswordPage.restore_button)# открывается ссылка https://stellarburgers.nomoreparties.site/reset-password
        restore_password_page = RestorePasswordPage(driver)
        restore_password_page.find_element(RestorePasswordPage.save_button)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/reset-password"


