from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)


    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def click_element(self, locator):
        self.wait_element(locator)
        self.driver.find_element(*locator).click()

    def element_send_keys(self, text, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
        element=self.driver.find_element(*locator)
        element.send_keys(text)

    def scroll_by_amount(self, x_offset, y_offset):
        self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x_offset, y_offset)

    def get_text(self, locator):
        return self.wait_element(locator).text
