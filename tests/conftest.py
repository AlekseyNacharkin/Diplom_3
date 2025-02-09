from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
from selenium import webdriver
from Diplom_3.pages.api_client import APIClient

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
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