from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from Diplom_3.pages.base_page import BasePage


class OrdersListPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    order_list_url = "https://stellarburgers.nomoreparties.site/feed"
    #первый доступный заказ
    first_order = (By.XPATH,'.//a[@class="OrderHistory_link__1iNby"]')
    # состав текст
    сomposition = (By.XPATH, './/p[@class="text text_type_main-medium mb-8"]')
    # список заказов в работе
    list_orders_in_state_in_progress = (By.XPATH,'.//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li')
    # каунтер заказов за все время
    counter_orders_of_all_time = (By.XPATH,'.//p[contains(text(), "Выполнено за все время:")]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    # каунтер заказов за сегодня
    counter_orders_completed_today = (By.XPATH,'.//p[contains(text(), "Выполнено за сегодня:")]/following-sibling::p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    # идентификатор заказа (всех 50 отображаемых заказов)
    identificator_of_order_in_orders_list = (By.XPATH,'.//p[@class="text text_type_digits-default"]')

    def located_order_in_state(self, locator, text):
        elements = self.find_elements(locator)
        for element in elements:
            if text in element.text:
                return text
        return None


