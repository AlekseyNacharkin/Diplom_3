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
from Diplom_3.pages.constructor_page import ConstructorPage
from Diplom_3.pages.ribbon_page import BaseRibbonPage
from Diplom_3.pages.orders_page import OrdersListPage

class TestOrdersList:

    def test_opening_orders_list(self,driver,get_user_value,authorization):
        ribbon = BaseRibbonPage(driver)
        ribbon.click(BaseRibbonPage.orders_list_button)
        assert driver.current_url == BaseRibbonPage.order_list_url

    def test_order_details(self,driver,create_order):
        base_ribbon = BaseRibbonPage(driver)
        base_ribbon.click(BaseRibbonPage.orders_list_button)
        order_list = OrdersListPage(driver)
        order_list.click(OrdersListPage.first_order)
        assert order_list.text_in_element(OrdersListPage.сomposition) == "Cостав" #вот в этом тесте изменен символ первый символ на латиницу, видимо специальный баг
        