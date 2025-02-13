from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from Diplom_3.pages.base_page import BasePage


class ConstructorPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    constructor_url = "https://stellarburgers.nomoreparties.site/"
    # флюорисцентная булка
    fluorescentic_bun = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    # окно описания ингредиента
    description_window = (By.XPATH, ".//p[@class='text text_type_main-medium mb-8']")
    # кнопка закрытия окна описания ингредиента
    button_closed_description_window = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    #каунтер булочек флюорисцентных
    counter_fluorescentic_bun = (By.XPATH,'.//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]//p[@class="counter_counter__num__3nue1"]')
    # место для перетаскивания конструктора бургера (куда будет производиться драгндроп)
    drop_place = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    #кнопка оформления заказа
    order_placement_button = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    # проверка отображения элемента при заказе
    identificator_of_order = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    # проверка состояния класса (xpath класса)
    modal_class_before_order = (By.XPATH,'.//section[@class="Modal_modal__P3_V5"]')
    # проверка состояния класса после нажатия (xpath класса)
    modal_class_before_order = (By.XPATH, './/section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]')
    # соус спайси
    spicy_x_sauce = (By.XPATH,'.//a[@href="/ingredient/61c0c5a71d1f82001bdaaa72"]')
    # биокотлета
    biocotlet = (By.XPATH,'.//a[@href="/ingredient/61c0c5a71d1f82001bdaaa71"]')
    # кнопка закрытия деталей заказа (оформленного)
    button_closed_description_order = (By.XPATH,'.//button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"][ancestor::section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]]')