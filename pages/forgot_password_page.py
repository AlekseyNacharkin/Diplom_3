from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Diplom_3.pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    forgot_password_url = "https://stellarburgers.nomoreparties.site/forgot-password"

    #кнопка "Восстановить"
    restore_button = (By.XPATH,"//button[contains(text(),'Восстановить')]")
    #поле email в дефолтном состоянии
    email_field_in_default_state = (By.XPATH,'//div[@class="input pr-6 pl-6 input_type_text input_size_default"]')
    # поле email в активном состоянии
    email_field_in_active_state = (By.XPATH,"//input[@name='name']")