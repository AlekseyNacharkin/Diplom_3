from Diplom_3.constants import *
from Diplom_3.pages.personal_account_page import PersonalAccountPage
from Diplom_3.pages.ribbon_page import BaseRibbonPage
from Diplom_3.pages.orders_page import OrdersListPage
import allure


class TestOrdersList:

    @allure.title("Тест открытия списка заказов")
    def test_opening_orders_list(self,driver,get_user_value,authorization):
        ribbon = BaseRibbonPage(driver)
        ribbon.click(BaseRibbonPage.orders_list_button)
        assert driver.current_url == BaseRibbonPage.order_list_url

    @allure.title("Тест открытия окна состава заказанного бургера")
    def test_order_details(self,driver,create_order):
        base_ribbon = BaseRibbonPage(driver)
        base_ribbon.click(BaseRibbonPage.orders_list_button)
        order_list = OrdersListPage(driver)
        order_list.click(OrdersListPage.first_order)
        assert order_list.text_in_element(OrdersListPage.сomposition) == ConstantsOrdersList.ASSERTION_TEXT_COMPOSITION #вот в этом тесте изменен символ первый символ на латиницу, видимо специальный баг

    @allure.title("Проверка того, что созданный заказ в статусе 'В работе'")
    def test_order_in_status_in_progress(self,driver,create_order): #тест не всегда стабильно проходит
        base_ribbon = BaseRibbonPage(driver)
        base_ribbon.click(BaseRibbonPage.orders_list_button)
        order_list = OrdersListPage(driver)
        counter_completed_orders_of_all_time, counter_completed_orders_today, order_id = create_order
        assert order_list.located_order_in_state(OrdersListPage.list_orders_in_state_in_progress, order_id) == order_id

    @allure.title("Тест изменения счетчика заказов за все время")
    def test_change_counter_completed_of_all_time(self,driver,create_order):
        base_ribbon = BaseRibbonPage(driver)
        base_ribbon.click(BaseRibbonPage.orders_list_button)
        order_list = OrdersListPage(driver)
        counter_completed_orders_of_all_time, counter_completed_orders_today, order_id = create_order
        assert int(order_list.text_in_element(OrdersListPage.counter_orders_of_all_time)) > int(counter_completed_orders_of_all_time)

    @allure.title("Тест изменения счетчика заказов за сегодня")
    def test_change_counter_completed_today(self, driver, create_order):# тест единожды упал, видимо не успел сосчитать каунтер
        base_ribbon = BaseRibbonPage(driver)
        base_ribbon.click(BaseRibbonPage.orders_list_button)
        order_list = OrdersListPage(driver)
        counter_completed_orders_of_all_time, counter_completed_orders_today, order_id = create_order
        assert int(order_list.text_in_element(OrdersListPage.counter_orders_completed_today)) > int(counter_completed_orders_today)

    @allure.title("Проверка наличия созданного заказа и в личном кабинете и в ленте заказов")
    def test_order_in_personal_account(self,driver,create_order):
        base_ribbon = BaseRibbonPage(driver)
        base_ribbon.click(BaseRibbonPage.personal_account_button)
        personal_account = PersonalAccountPage(driver)
        personal_account.click(PersonalAccountPage.orders_history_button)
        order_in_personal_account_history = personal_account.text_in_element(PersonalAccountPage.identificator_of_order)
        order_list = OrdersListPage(driver)
        order_list.get_url_page(OrdersListPage.order_list_url)
        assert order_in_personal_account_history == order_list.located_order_in_state(OrdersListPage.identificator_of_order_in_orders_list,order_in_personal_account_history)