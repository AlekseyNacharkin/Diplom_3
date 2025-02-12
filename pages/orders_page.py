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
    # список заказов в работе
    list_orders_in_state_in_progress = (By.XPATH,'.//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li')



    def located_order_in_state_in_progress(self,locator,text):
        elements = self.find_elements(locator)
        for element in elements:
            if text in element.text:
                return element
        return None


