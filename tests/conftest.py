from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium import webdriver
from Diplom_3.pages.api_client import APIClient
from Diplom_3.pages.constructor_page import ConstructorPage
from Diplom_3.pages.login_page import LoginPage


@pytest.fixture(params=["chrome"])#, "firefox"])
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
    response = api_client.registration_user(data={"name": "Влад","email": "mezenov@gmail.com","password": "mezenov321"})
    email = "mezenov@gmail.com"
    password = "mezenov321"
    yield email,password
    authorization_user = api_client.authorization_user(data={"email": "mezenov@gmail.com", "password": "mezenov321"})
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
    # time.sleep(5)
    constructor_page.wait_for_scroll_to_finish()
    constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)

@pytest.fixture
def create_order(driver,authorization):
    constructor_page = ConstructorPage(driver)
    constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
    constructor_page.drag_n_drop(ConstructorPage.fluorescentic_bun, ConstructorPage.drop_place)