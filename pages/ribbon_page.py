from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Diplom_3.pages.base_page import BasePage


class BaseRibbonPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    order_list_url = "https://stellarburgers.nomoreparties.site/feed"

    # кнопка личного аккаунта в риббоне
    personal_account_button = (By.XPATH, './/a[@href="/account"]')
    # кнопка ленты заказов в риббоне
    orders_list_button = (By.XPATH, './/a[@href="/feed"]')
    # кнопка конструктор в риббоне
    constructor_button = (By.XPATH,'.//a[@xpath="1"]')
