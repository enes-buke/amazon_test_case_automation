from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT = (By.ID, 'productTitle')
    BUY_NOW_BUTTON=(By.ID, 'buy-now-button')
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
    VERIFY_ADD_TO_CARD = (By.CSS_SELECTOR, '.a-size-medium-plus')
    GO_TO_CART_BUTTON= (By.ID, 'nav-cart')
    verify_text="Samsung"
    add_to_card_verify="Sepete eklendi"


    def get_product_text(self):
        return self.get_text(self.PRODUCT)

    def click_add_to_card_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def get_verify_add_to_card(self):
        return self.get_text(self.VERIFY_ADD_TO_CARD)

    def click_to_cart(self):
        self.click_element(self.GO_TO_CART_BUTTON)







