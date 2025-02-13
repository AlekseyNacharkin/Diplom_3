from Diplom_3.constants import *
from Diplom_3.pages.constructor_page import ConstructorPage
import allure

class TestConstructorPage:

    @allure.title("Тест открытия окна ингредиента")
    def test_opening_ingredient_description(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        constructor_page.click(ConstructorPage.fluorescentic_bun)
        assert ConstantsConstructorPage.FLUORESCENTIC_BUN in constructor_page.text_in_element(ConstructorPage.description_window)

    @allure.title("Тест закрытия окна ингредиента")
    def test_closet_ingredient_description(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        constructor_page.click(ConstructorPage.fluorescentic_bun)
        constructor_page.click(ConstructorPage.button_closed_description_window)
        assert not constructor_page.visibility_element(ConstructorPage.description_window)

    @allure.title("Тест изменения счетчика ингредиента после его добавления в бургер")
    def test_counter_buns(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        assert int(constructor_page.text_in_element(ConstructorPage.counter_fluorescentic_bun)) == 0
        constructor_page.drag_n_drop(ConstructorPage.fluorescentic_bun,ConstructorPage.drop_place)
        assert int(constructor_page.text_in_element(ConstructorPage.counter_fluorescentic_bun)) == 2

    @allure.title("Тест окна создания оформленного заказа")
    def test_order_placement(self,driver,get_user_value,authorization):
        constructor_page = ConstructorPage(driver)
        constructor_page.is_displayed(ConstructorPage.fluorescentic_bun)
        constructor_page.drag_n_drop(ConstructorPage.fluorescentic_bun, ConstructorPage.drop_place)
        constructor_page.click(ConstructorPage.order_placement_button)
        assert ConstantsConstructorPage.CLASSNAME_FOR_ASSERT in constructor_page.get_element_class(ConstructorPage.modal_class_before_order,ConstantsConstructorPage.CLASS)


