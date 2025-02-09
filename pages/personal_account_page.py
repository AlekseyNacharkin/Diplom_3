from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Diplom_3.pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    personal_account_url = "https://stellarburgers.nomoreparties.site/account/profile"

    #кнопка личного аккаунта в риббоне
    personal_account_button = (By.XPATH,"//p[contains(text(),'Личный Кабинет')]")
    #кнопка профиль
    profile_button = (By.XPATH,"//a[contains(text(),'Профиль')]")
