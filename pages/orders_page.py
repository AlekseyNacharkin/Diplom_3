from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Diplom_3.pages.base_page import BasePage


class OrdersListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #первый доступный заказ
    first_order = (By.XPATH,'.//a[@class="OrderHistory_link__1iNby"]')
    # состав текст
    сomposition = (By.XPATH, './/p[@class="text text_type_main-medium mb-8"]')

