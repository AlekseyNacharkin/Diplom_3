from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Diplom_3.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    base_url = "https://stellarburgers.nomoreparties.site"
    login_url = "https://stellarburgers.nomoreparties.site/login"

    #Поле email
    email_field = (By.XPATH,"//input[@name='name']")
    # Поле пароль
    password_field = (By.XPATH,'.//input[@type="password"]')
    #кнопка скрытия/раскрытия пароля
    eyes_button = (By.XPATH,"//div[@class='input__icon input__icon-action']")
    # предок кнопки скрытия/раскрытия пароля в дефолтном состоянии (для теста)
    parent_element_eyes_button_in_default_state = (By.XPATH,'//div[@class="input__icon input__icon-action"]/ancestor::div[@class="input pr-6 pl-6 input_type_password input_size_default"]')
    # предок кнопки скрытия/раскрытия пароля в активном состоянии (для теста)
    parent_element_eyes_button_in_active_state = (By.XPATH,'//div[@class="input__icon input__icon-action"]/ancestor::div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
    #кнопка восстановить пароль
    restore_password_button = (By.XPATH,'.//a[@href="/forgot-password"]')
    #кнопка войти в аккаунт
    login_button = (By.XPATH,"//button[contains(text(),'Войти')]")









