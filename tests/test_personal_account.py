from Diplom_3.pages.login_page import LoginPage
from Diplom_3.pages.personal_account_page import PersonalAccountPage
from Diplom_3.pages.ribbon_page import BaseRibbonPage
import allure


class TestPersonalAccount:
    @allure.title("Тест открытия личного кабинета")
    def test_opening_personal_account(self,get_user_value,driver,authorization):
        ribbon = BaseRibbonPage(driver)
        ribbon.click(BaseRibbonPage.personal_account_button)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.is_displayed(PersonalAccountPage.profile_button)
        assert driver.current_url == personal_account_page.personal_account_url

    @allure.title("Тест открытия истории заказов")
    def test_opening_orders_history(self,get_user_value,driver,authorization):
        ribbon = BaseRibbonPage(driver)
        ribbon.click(BaseRibbonPage.personal_account_button)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.is_displayed(PersonalAccountPage.orders_history_button)
        assert driver.current_url == PersonalAccountPage.personal_account_url

    @allure.title("Тест логаута через личный кабинет")
    def test_logout_from_personal_account(self,get_user_value,driver,authorization):
        ribbon = BaseRibbonPage(driver)
        ribbon.click(BaseRibbonPage.personal_account_button)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click(PersonalAccountPage.logout_button)
        login_page = LoginPage(driver)
        login_page.is_displayed(LoginPage.login_button)
        assert driver.current_url == LoginPage.login_url
