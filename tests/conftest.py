import time

import pytest
from selenium import webdriver
from Diplom_3.api_client.api_client import APIClient
from Diplom_3.pages.constructor_page import ConstructorPage
from Diplom_3.pages.login_page import LoginPage
from Diplom_3.pages.orders_page import OrdersListPage
from Diplom_3.constants import *

@pytest.fixture(params=["chrome","firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def get_user_value():
    api_client = APIClient()
    response = api_client.registration_user(data=ForFixtures.USERVALUE)
    email = ForFixtures.USERVALUE.get("email")
    password = ForFixtures.USERVALUE.get("password")
    yield email,password
    authorization_user = api_client.authorization_user(data={"email": email, "password": password})
    authorization_user_token = authorization_user.json().get("accessToken")
    authorization_user_token
    api_client.delete_user(authorization=authorization_user_token)

@pytest.fixture
def authorization(get_user_value,driver):
    login_page = LoginPage(driver)
    login_page.get_url_page(LoginPage.login_url)
    email, password = get_user_value
    login_page.send_keys(LoginPage.email_field, email)
    login_page.send_keys(LoginPage.password_field, password)
    login_page.click(LoginPage.login_button)
    constructor_page = ConstructorPage(driver)
    constructor_page.wait_for_scroll_to_finish()
    constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)

@pytest.fixture
def create_order(driver,authorization):
    order_list = OrdersListPage(driver)
    order_list.get_url_page(OrdersListPage.order_list_url)
    counter_completed_orders_of_all_time = order_list.text_in_element(OrdersListPage.counter_orders_of_all_time)
    counter_completed_orders_today = order_list.text_in_element(OrdersListPage.counter_orders_completed_today)
    constructor_page = ConstructorPage(driver)
    constructor_page.get_url_page(ConstructorPage.constructor_url)
    constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
    constructor_page.drag_n_drop(ConstructorPage.fluorescentic_bun, ConstructorPage.drop_place)
    constructor_page.drag_n_drop(ConstructorPage.fluorescentic_bun, ConstructorPage.drop_place)
    constructor_page.drag_n_drop(ConstructorPage.biocotlet, ConstructorPage.drop_place)
    constructor_page.drag_n_drop(ConstructorPage.spicy_x_sauce, ConstructorPage.drop_place)
    constructor_page.click(ConstructorPage.order_placement_button)
    timeout = 10
    start_time = time.time()

    while True:
        order_id = constructor_page.text_in_element(ConstructorPage.identificator_of_order)
        if order_id != '9999':
            break
        if time.time() - start_time > timeout:
            raise TimeoutError("Order ID не появился в течение 10 секунд")
        time.sleep(0.5)
    constructor_page.click(ConstructorPage.button_closed_description_order)
    yield counter_completed_orders_of_all_time,counter_completed_orders_today,order_id