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

class TestConstructorPage:

    def test_opening_ingredient_description(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        constructor_page.click(ConstructorPage.fluorescentic_bun)
        assert "Флюоресцентная булка R2-D3" in constructor_page.text_in_element(ConstructorPage.description_window)


    def test_closet_ingredient_description(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        constructor_page.click(ConstructorPage.fluorescentic_bun)
        constructor_page.click(ConstructorPage.button_closed_description_window)
        assert not constructor_page.visibility_element(ConstructorPage.description_window)

    def test_counter_buns(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        assert int(constructor_page.text_in_element(ConstructorPage.counter_fluorescentic_bun)) == 0
        constructor_page.drag_n_drop(ConstructorPage.fluorescentic_bun,ConstructorPage.drop_place)
        assert int(constructor_page.text_in_element(ConstructorPage.counter_fluorescentic_bun)) == 2

    def test_order_placement(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        constructor_page.drag_n_drop(ConstructorPage.fluorescentic_bun, ConstructorPage.drop_place)
        constructor_page.click(ConstructorPage.order_placement_button)
        assert constructor_page.is_displayed(ConstructorPage.qwerty)


