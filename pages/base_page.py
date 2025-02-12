from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

class BasePage:
    def __init__(self,driver,wait):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator, text):
        element = self.find_element(locator)
        #element.clear()
        element.send_keys(text)

    def get_url_page(self, url):
        self.driver.get(url)

    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    def is_element_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    def visibility_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_scroll_to_finish(self, timeout=5):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        last_scroll_position = self.driver.execute_script("return window.scrollY")

        self.wait.until(
            lambda d: self.driver.execute_script("return window.scrollY") == last_scroll_position
        )

    def text_in_element(self,locator):
        return self.find_element(locator).text

    def get_element_class(self,locator,classname):
        return self.find_element(locator).get_dom_attribute(classname)


    def invisibility_element(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def drag_n_drop(self, locator1, locator2):
        draggable = self.find_element(locator1)
        droppable = self.find_element(locator2)

        actions = ActionChains(self.driver)
        (actions.click_and_hold(draggable)
         .pause(1)
         .move_to_element(droppable)
         .pause(1)
         .release()
         .perform())

    def find_elements(self,locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
