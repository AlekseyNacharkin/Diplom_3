from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Diplom_3.pages.base_page import BasePage


class RestorePasswordPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    restore_password_url = "https://stellarburgers.nomoreparties.site/reset-password"

    #кнопка "Сохранить"
    save_button = (By.XPATH,"//button[contains(text(),'Сохранить')]")
