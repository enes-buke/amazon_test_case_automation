from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.CSS_SELECTOR, '#twotabsearchtextbox')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '#nav-search-submit-button')


    def close_cookies(self):
        try:
            self.driver.execute_script("document.getElementById('sp-cc-accept').click();")
        except Exception as e:
            print(f"The cookie pop-up didn't appear...: {e}")

    def send_keys_samsung(self):
        self.element_send_keys('samsung', self.SEARCH_BOX)

    def click_search_button(self):
        self.click_element(self.SEARCH_BUTTON)


