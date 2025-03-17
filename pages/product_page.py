from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):

    PRODUCT = (By.ID, 'productTitle') #ÜRÜN İSMİ BURADA ALINACAK
    PRODUCT_ABOUT_PART = (By.CSS_SELECTOR,'.a-size-base-plus.a-text-bold') #ÜRÜNÜN HAKKINDA KISMI,ÜRÜN SAYFASINDA OLDUĞUNU DOĞRULAMAK İÇİN
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button') #SEPETE EKLEME BUTONU
    VERIFY_ADD_TO_CARD = (By.CSS_SELECTOR, '.a-size-medium-plus') #SEPETE EKLENDİ
    GO_TO_CART_BUTTON= (By.ID, 'nav-cart') #sepete gitme butonu
    verify_about_part='Bu ürün hakkında'
    verify_text="Samsung"
    add_to_card_verify="eklendi"



    def scroll_by_amount(self, x_offset, y_offset):
        self.driver.execute_script("window.scrollBy(arguments[0], arguments[1]);", x_offset, y_offset)

    def get_product_about(self):
        return self.get_text(self.PRODUCT_ABOUT_PART)

    def scroll_page_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def get_product_text(self):
        return self.get_text(self.PRODUCT)

    def click_add_to_card_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def get_verify_add_to_card(self):
        return self.get_text(self.VERIFY_ADD_TO_CARD)

    def click_to_cart(self):
        self.click_element(self.GO_TO_CART_BUTTON)







